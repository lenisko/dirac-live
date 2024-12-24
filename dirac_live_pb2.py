# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: dirac_live.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""

from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder

_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC, 5, 27, 2, "", "dirac_live.proto"
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(
    b'\n\x10\x64irac_live.proto\x12\x0c\x64io.endpoint\x1a\x1bgoogle/protobuf/empty.proto"!\n\x04UUID\x12\x0b\n\x03low\x18\x01 \x01(\x04\x12\x0c\n\x04high\x18\x02 \x01(\x04"\xbd\x01\n\nDeviceInfo\x12\x14\n\x0cmanufacturer\x18\x01 \x01(\t\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x12\n\nmodel_name\x18\x03 \x01(\t\x12 \n\x18unique_device_identifier\x18\x04 \x01(\t\x12\x14\n\x0cnum_speakers\x18\x05 \x01(\x05\x12\x10\n\x08num_mics\x18\x06 \x01(\x05\x12\x18\n\x10num_filter_slots\x18\x07 \x01(\x05\x12\x13\n\x0bsystem_name\x18\x08 \x01(\t"\x8f\x01\n\x0cSlotMetadata\x12\x1d\n\x15\x65ndpoint_manufacturer\x18\x01 \x01(\t\x12\x16\n\x0e\x65ndpoint_model\x18\x02 \x01(\t\x12)\n\rendpoint_uuid\x18\x03 \x01(\x0b\x32\x12.dio.endpoint.UUID\x12\x1d\n\x15required_capabilities\x18\x04 \x03(\x03"\xf8\x02\n\x08SlotInfo\x12\x12\n\nslot_index\x18\x01 \x01(\x05\x12\x0c\n\x04name\x18\x02 \x01(\t\x12\x18\n\x10\x66ilter_type_name\x18\x03 \x01(\t\x12\x12\n\nnum_inputs\x18\x04 \x01(\x05\x12\x13\n\x0bnum_outputs\x18\x05 \x01(\x05\x12\x11\n\tmax_delay\x18\x06 \x01(\x05\x12\x10\n\x08min_gain\x18\x07 \x01(\x02\x12\x10\n\x08max_gain\x18\x08 \x01(\x02\x12\x14\n\x0cnum_sections\x18\t \x01(\x05\x12\x15\n\rcreation_time\x18\n \x01(\x03\x12%\n\tunique_id\x18\x0b \x01(\x0b\x32\x12.dio.endpoint.UUID\x12\x13\n\x0b\x64\x65scription\x18\x0c \x01(\t\x12\x1b\n\x13sub_sampling_factor\x18\r \x03(\x05\x12\x17\n\x0fis_trial_filter\x18\x0e \x01(\x08\x12\x31\n\rslot_metadata\x18\x0f \x01(\x0b\x32\x1a.dio.endpoint.SlotMetadata"\x8b\x01\n\rOperationMode\x12\x14\n\x0cgain_enabled\x18\x01 \x01(\x08\x12\x15\n\rdelay_enabled\x18\x02 \x01(\x08\x12\x19\n\x11\x66iltering_enabled\x18\x03 \x01(\x08\x12\x17\n\x0fmeasure_enabled\x18\x04 \x01(\x08\x12\x19\n\x11streaming_enabled\x18\x05 \x01(\x08"#\n\rSlotInfoIndex\x12\x12\n\nslot_index\x18\x01 \x01(\x05\x32\xba\x03\n\x0e\x45ndpointDevice\x12\x41\n\rGetDeviceInfo\x12\x16.google.protobuf.Empty\x1a\x18.dio.endpoint.DeviceInfo\x12\x42\n\x0bGetSlotInfo\x12\x1b.dio.endpoint.SlotInfoIndex\x1a\x16.dio.endpoint.SlotInfo\x12\x44\n\rGetActiveSlot\x12\x16.google.protobuf.Empty\x1a\x1b.dio.endpoint.SlotInfoIndex\x12\x44\n\rSetActiveSlot\x12\x1b.dio.endpoint.SlotInfoIndex\x1a\x16.google.protobuf.Empty\x12G\n\x10GetOperationMode\x12\x16.google.protobuf.Empty\x1a\x1b.dio.endpoint.OperationMode\x12L\n\x10SetOperationMode\x12\x1b.dio.endpoint.OperationMode\x1a\x1b.dio.endpoint.OperationModeb\x06proto3'
)

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, "dirac_live_pb2", _globals)
if not _descriptor._USE_C_DESCRIPTORS:
    DESCRIPTOR._loaded_options = None
    _globals["_UUID"]._serialized_start = 63
    _globals["_UUID"]._serialized_end = 96
    _globals["_DEVICEINFO"]._serialized_start = 99
    _globals["_DEVICEINFO"]._serialized_end = 288
    _globals["_SLOTMETADATA"]._serialized_start = 291
    _globals["_SLOTMETADATA"]._serialized_end = 434
    _globals["_SLOTINFO"]._serialized_start = 437
    _globals["_SLOTINFO"]._serialized_end = 813
    _globals["_OPERATIONMODE"]._serialized_start = 816
    _globals["_OPERATIONMODE"]._serialized_end = 955
    _globals["_SLOTINFOINDEX"]._serialized_start = 957
    _globals["_SLOTINFOINDEX"]._serialized_end = 992
    _globals["_ENDPOINTDEVICE"]._serialized_start = 995
    _globals["_ENDPOINTDEVICE"]._serialized_end = 1437
# @@protoc_insertion_point(module_scope)
