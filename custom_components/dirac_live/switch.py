"""Switch platform for Dirac Live."""

import logging
from typing import Any

from homeassistant.components.switch import SwitchEntity
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity import EntityCategory
from homeassistant.helpers.entity_platform import AddEntitiesCallback

from .const import DOMAIN
from .coordinator import DiracLiveUpdateCoordinator

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant, entry: ConfigEntry, async_add_entities: AddEntitiesCallback
) -> None:
    """Set up the switch platform."""
    coordinator: DiracLiveUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]

    async_add_entities([DiracLiveFilteringSwitch(coordinator)])


class DiracLiveFilteringSwitch(SwitchEntity):
    """Representation of a switch to control filtering_enabled."""

    def __init__(self, coordinator: DiracLiveUpdateCoordinator) -> None:
        """Initialize the switch entity."""
        self.coordinator = coordinator
        self._attr_name = (
            f"{coordinator.data.get('name', 'DiracLive')} Filtering Enabled"
        )
        self._attr_unique_id = (
            f"{coordinator.data.get('name', DOMAIN)}_filtering_enabled"
        )
        self._attr_entity_category = EntityCategory.CONFIG

    @property
    def is_on(self) -> bool:
        """Return the status of the filtering_enabled switch."""
        return self.coordinator.data.get("filtering_enabled", False)

    async def async_turn_on(self, **kwargs: Any) -> None:
        """Turn on filtering."""
        try:
            await self.coordinator.hass.async_add_executor_job(
                self.coordinator.client.set_operation_mode, True
            )
            # Update coordinator data to reflect changes immediately
            self.coordinator.data["filtering_enabled"] = True
            await self.coordinator.async_request_refresh()
        except Exception as e:
            _LOGGER.error("Failed to enable filtering: %s", e)

    async def async_turn_off(self, **kwargs: Any) -> None:
        """Turn off filtering."""
        try:
            await self.coordinator.hass.async_add_executor_job(
                self.coordinator.client.set_operation_mode, False
            )
            self.coordinator.data["filtering_enabled"] = False
            await self.coordinator.async_request_refresh()
        except Exception as e:
            _LOGGER.error("Failed to disable filtering: %s", e)

    async def async_update(self) -> None:
        """Update the state of the entity."""
        await self.coordinator.async_request_refresh()
