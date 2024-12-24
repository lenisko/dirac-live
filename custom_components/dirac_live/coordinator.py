"""InPost API data coordinator."""

import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator

from .client import DiracLiveClient
from .const import DOMAIN, SCAN_INTERVAL

_LOGGER = logging.getLogger(__name__)

type DiracLiveConfigEntry = ConfigEntry[DiracLiveUpdateCoordinator]


class DiracLiveUpdateCoordinator(DataUpdateCoordinator):
    """Class to manage fetching Dirac Live data."""

    def __init__(self, hass: HomeAssistant, address: str, port: str) -> None:
        """Initialize the data update coordinator."""

        self.client = DiracLiveClient(address, port)
        super().__init__(
            hass,
            _LOGGER,
            name=DOMAIN,
            update_interval=SCAN_INTERVAL,
        )

    def _update_data(self) -> dict[str, float]:
        data: dict[str, float] = {}
        try:
            self.client.connect()
            remote_data = self.client.get_device_info()
        except Exception as e:
            _LOGGER.debug("No response from Dirac Live device: %s", e)
            self.client.close()
        finally:
            data["name"] = remote_data.name
            data["model"] = remote_data.model
            data["filtering_enabled"] = remote_data.filtering_enabled
            data["filter_slots"] = remote_data.filter_slots
            data["actve_filter"] = remote_data.actve_filter
            data["filters"] = remote_data.filters

        return data

    async def _async_update_data(self) -> dict[str, float]:
        """Update Dirac Live data in the executor."""
        return await self.hass.async_add_executor_job(self._update_data)
