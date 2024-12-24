# pip install grpcio grpcio-tools
# python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. dirac_live.proto

from dataclasses import dataclass
import logging

from google.protobuf.empty_pb2 import Empty
import grpc

from .dirac_live_pb2 import DeviceInfo, OperationMode, SlotInfo, SlotInfoIndex
from .dirac_live_pb2_grpc import EndpointDeviceStub

_LOGGER = logging.getLogger(__name__)


@dataclass
class Filter:
    """A class representing Filter Information."""

    index: int
    name: str


@dataclass
class Device:
    """A class representing Device Information."""

    name: str
    model: str
    filtering_enabled: bool
    filter_slots: int
    actve_filter: Filter
    filters: list[Filter]


class DiracLiveClient:
    """Basic Dirac Live client used to communicate over gRPC."""

    def __init__(self, address: str, port: int) -> None:  # noqa: D107
        self.channel: grpc.Channel = None
        self.stub: EndpointDeviceStub = None
        self.address: str = address
        self.port: int = port

    def connect(self):
        self.channel = grpc.insecure_channel(f"{self.address}:{self.port}")
        self.stub = EndpointDeviceStub(self.channel)

    def get_device_info(self) -> Device:  # noqa: D102
        device_info: DeviceInfo = self.stub.GetDeviceInfo(Empty())
        operation_mode: OperationMode = self._get_operation_mode()
        active_slot: int = self.stub.GetActiveSlot(Empty()).slot_index

        filters: list = []
        for slot_index in range(device_info.num_filter_slots):
            slot_info: SlotInfo = self.stub.GetSlotInfo(
                SlotInfoIndex(slot_index=slot_index)
            )
            filters.append(Filter(index=slot_info.slot_index, name=slot_info.name))

        device: Device = Device(
            name=device_info.name,
            model=device_info.model_name,
            filtering_enabled=operation_mode.filtering_enabled,
            filter_slots=device_info.num_filter_slots,
            actve_filter=filters[active_slot],
            filters=filters,
        )

        return device

    def set_active_slot(self, slot_index: int) -> None:  # noqa: D102
        self.stub.SetActiveSlot(SlotInfo(slot_index=slot_index))
        _LOGGER.info(
            f"Set active slot to {slot_index}"  # noqa: G004
        )

    def set_operation_mode(self, filtering_enabled: bool) -> None:  # noqa: D102
        # make sure to apply previous values to not break a sync
        operation_mode: OperationMode = self._get_operation_mode()
        if operation_mode.filtering_enabled == filtering_enabled:
            return

        self.stub.SetOperationMode(
            OperationMode(
                gain_enabled=operation_mode.gain_enabled,
                delay_enabled=operation_mode.delay_enabled,
                filtering_enabled=filtering_enabled,
            )
        )
        _LOGGER.info(
            f"Swapped Operation mode from {operation_mode.filtering_enabled} to {filtering_enabled}"  # noqa: G004
        )

    def _get_operation_mode(self) -> OperationMode:
        return self.stub.GetOperationMode(Empty())

    def close(self) -> None:  # noqa: D102
        self.channel.close()
