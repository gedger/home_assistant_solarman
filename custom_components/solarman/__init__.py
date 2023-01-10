"""The Solarman Collector integration."""

import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.const import CONF_NAME

from .const import *

_LOGGER = logging.getLogger(__name__)

PLATFORMS: list[str] = ["sensor"]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Solarman Collector from a config entry."""
    _LOGGER.debug(f'__init__.py:async_setup_entry({entry.as_dict()})')
    hass.config_entries.async_setup_platforms(entry, PLATFORMS)
    entry.async_on_unload(entry.add_update_listener(update_listener))
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    _LOGGER.debug(f'__init__.py:async_unload_entry({entry.as_dict()})')
    unload_ok = await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    return unload_ok


async def update_listener(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """Handle options update."""
    _LOGGER.debug(f'__init__.py:update_listener({entry.as_dict()})')
    hass.data[DOMAIN][entry.entry_id].config(entry)
    entry.title = entry.options[CONF_NAME]

async def async_migrate_entry(hass, config_entry: ConfigEntry):
    """Migrate old entry."""
    _LOGGER.debug("Migrating from version %s", config_entry.version)

    if config_entry.version == 1:
        """ handle the new config entry migration """
        new = {**config_entry.data, CONF_DAYLIGHT_ONLY: DEFAULT_DAYLIGHT_ONLY}
        config_entry.version = 2
        hass.config_entries.async_update_entry(config_entry, data=new)

    _LOGGER.info("Migration to version %s successful", config_entry.version)

    return True