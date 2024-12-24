"""The Dirac Live integration."""

from __future__ import annotations

from homeassistant.const import CONF_HOST, Platform
from homeassistant.core import HomeAssistant

from .const import DOMAIN
from .coordinator import DiracLiveConfigEntry, DiracLiveUpdateCoordinator

PLATFORMS: list[Platform] = [Platform.SELECT, Platform.SWITCH]


async def async_setup_entry(hass: HomeAssistant, entry: DiracLiveConfigEntry) -> bool:  # noqa: D103
    address = entry.data[CONF_HOST]

    coordinator = DiracLiveUpdateCoordinator(hass, address, 45222)
    await coordinator.async_config_entry_first_refresh()

    if DOMAIN not in hass.data:
        hass.data[DOMAIN] = {}
    hass.data[DOMAIN][entry.entry_id] = coordinator

    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)

    return True


async def async_unload_entry(hass: HomeAssistant, entry: DiracLiveConfigEntry) -> bool:  # noqa: D103
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
