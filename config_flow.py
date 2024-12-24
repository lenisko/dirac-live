"""Config flow for the Dirac Live integration."""

from __future__ import annotations

import logging
from typing import Any

import voluptuous as vol

from homeassistant.config_entries import ConfigFlow, ConfigFlowResult
from homeassistant.const import CONF_HOST
from homeassistant.core import HomeAssistant
from homeassistant.exceptions import HomeAssistantError

from .client import DiracLiveClient
from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_HOST): str,
    }
)


async def validate_input(hass: HomeAssistant, data: dict[str, Any]) -> dict[str, Any]:  # noqa: D103
    try:
        client = DiracLiveClient(address=data[CONF_HOST], port=45222)
        client.connect()
        device = client.get_device_info()
    except Exception as e:  # noqa: BLE001
        _LOGGER.error("Failed to initialize Dirac Live client: %s", e)
        raise CannotConnect  # noqa: B904
    finally:
        client.close()

    return {"name": device.name, "model": device.model}


class ConfigFlow(ConfigFlow, domain=DOMAIN):
    """Handle a config flow for Dirac Live."""

    VERSION = 1

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> ConfigFlowResult:
        """Handle the initial step."""
        errors: dict[str, str] = {}
        if user_input is not None:
            # Check if a device with the same host is already configured
            for entry in self._async_current_entries():
                if entry.data[CONF_HOST] == user_input[CONF_HOST]:
                    return self.async_abort(reason="already_configured")

            if not errors:
                try:
                    info = await validate_input(self.hass, user_input)
                except CannotConnect:
                    errors["base"] = "cannot_connect"
                except Exception:
                    _LOGGER.exception("Unexpected exception")
                    errors["base"] = "unknown"
                else:
                    # when name is different than model use it
                    title: str = (
                        f"{info['name']} ({info['model']})"
                        if info["name"] != info["model"]
                        else info["name"]
                    )
                    return self.async_create_entry(title=title, data=user_input)

        return self.async_show_form(
            step_id="user",
            data_schema=STEP_USER_DATA_SCHEMA,
            errors=errors,
            description_placeholders={
                "host": user_input.get(CONF_HOST, "") if user_input else ""
            },
        )


class CannotConnect(HomeAssistantError):
    """Error to indicate we cannot connect."""
