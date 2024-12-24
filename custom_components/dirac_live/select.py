"""Select platform for Dirac Live."""

import logging

from homeassistant.components.select import SelectEntity
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
    """Set up the platforms."""
    coordinator: DiracLiveUpdateCoordinator = hass.data[DOMAIN][entry.entry_id]
    async_add_entities([DiracLiveFilterSelect(coordinator)])


class DiracLiveFilterSelect(SelectEntity):
    """Representation of a select entity for filter selection."""

    def __init__(self, coordinator: DiracLiveUpdateCoordinator) -> None:
        """Initialize the select entity."""
        self.coordinator = coordinator
        self._attr_name = f"{coordinator.data.get('name', 'DiracLive')} Active Filter"
        self._attr_unique_id = f"{coordinator.data.get('name', DOMAIN)}_active_filter"
        self._attr_entity_category = EntityCategory.CONFIG

    @property
    def options(self) -> list[str]:
        """Return the list of available filter options."""
        filters = self.coordinator.data.get("filters", [])
        return [f.name for f in filters]

    @property
    def current_option(self) -> str | None:
        """Return the currently active filter."""
        active_filter = self.coordinator.data.get("actve_filter")
        return active_filter.name if active_filter else None

    async def async_select_option(self, option: str) -> None:
        """Set the active filter."""
        try:
            filters = self.coordinator.data.get("filters", [])
            selected_filter = next(f for f in filters if f.name == option)
            slot_index = selected_filter.index
            await self.coordinator.hass.async_add_executor_job(
                self.coordinator.client.set_active_slot, slot_index
            )
            # Update coordinator data to reflect changes immediately
            self.coordinator.data["actve_filter"] = selected_filter
            await self.coordinator.async_request_refresh()
        except StopIteration:
            _LOGGER.error("Invalid filter option: %s", option)
        except Exception as e:
            _LOGGER.error("Failed to set active filter: %s", e)

    async def async_update(self) -> None:
        """Update the state of the entity."""
        await self.coordinator.async_request_refresh()
