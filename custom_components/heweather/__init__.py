"""和风天气集成."""
import logging
import asyncio
from datetime import timedelta

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

from .const import DOMAIN

_LOGGER = logging.getLogger(__name__)

PLATFORMS = ["weather", "sensor"]


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """设置和风天气组件."""
    hass.data.setdefault(DOMAIN, {})
    return True


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """设置来自配置流的和风天气."""
    hass.data.setdefault(DOMAIN, {})
    
    # 存储配置条目
    hass.data[DOMAIN][entry.entry_id] = entry.data
    
    # 配置每个平台
    for platform in PLATFORMS:
        hass.async_create_task(
            hass.config_entries.async_forward_entry_setup(entry, platform)
        )
    
    # 添加更新监听器
    entry.async_on_unload(entry.add_update_listener(async_update_options))
    
    return True


async def async_update_options(hass: HomeAssistant, entry: ConfigEntry) -> None:
    """当用户更新选项时处理."""
    await hass.config_entries.async_reload(entry.entry_id)


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """卸载和风天气条目."""
    unload_ok = all(
        await asyncio.gather(
            *[
                hass.config_entries.async_forward_entry_unload(entry, platform)
                for platform in PLATFORMS
            ]
        )
    )
    
    # 移除条目
    if unload_ok:
        hass.data[DOMAIN].pop(entry.entry_id)
    
    return unload_ok 