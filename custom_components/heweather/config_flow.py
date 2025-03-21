"""和风天气集成的配置流程."""
import logging
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
import homeassistant.helpers.config_validation as cv
from homeassistant.const import CONF_NAME

from .const import (
    DOMAIN,
    CONF_LOCATION,
    CONF_KEY,
    CONF_DISASTERLEVEL,
    CONF_DISASTERMSG,
    DEFAULT_NAME,
    DEFAULT_DISASTERLEVEL,
    DEFAULT_DISASTERMSG,
)

_LOGGER = logging.getLogger(__name__)

class HeweatherFlowHandler(config_entries.ConfigFlow, domain=DOMAIN):
    """处理和风天气配置流程."""

    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_CLOUD_POLL

    async def async_step_user(self, user_input=None):
        """处理用户输入的配置."""
        errors = {}

        if user_input is not None:
            # 检查是否已经配置了相同location的实例
            await self.async_set_unique_id(user_input[CONF_LOCATION])
            self._abort_if_unique_id_configured()
            
            # 确保disasterlevel是字符串类型
            if CONF_DISASTERLEVEL in user_input:
                user_input[CONF_DISASTERLEVEL] = str(user_input[CONF_DISASTERLEVEL])
            
            return self.async_create_entry(
                title=user_input.get(CONF_NAME, DEFAULT_NAME),
                data=user_input,
            )

        # 显示表单
        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required(CONF_NAME, default=DEFAULT_NAME): str,
                    vol.Required(CONF_LOCATION): str,
                    vol.Required(CONF_KEY): str,
                    vol.Required(CONF_DISASTERLEVEL, default=int(DEFAULT_DISASTERLEVEL)): vol.All(
                        vol.Coerce(int), vol.Range(min=1, max=6)
                    ),
                    vol.Required(CONF_DISASTERMSG, default=DEFAULT_DISASTERMSG): vol.In(
                        ["title", "allmsg"]
                    ),
                }
            ),
            errors=errors,
        )

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        """获取选项流."""
        return HeweatherOptionsFlowHandler(config_entry)


class HeweatherOptionsFlowHandler(config_entries.OptionsFlow):
    """处理和风天气选项流程."""

    def __init__(self, config_entry):
        """初始化选项流程."""
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        """管理选项."""
        if user_input is not None:
            # 更新数据
            data = {**self.config_entry.data}
            # 如果用户修改了location或key，也要更新数据
            if CONF_LOCATION in user_input:
                data[CONF_LOCATION] = user_input[CONF_LOCATION]
            if CONF_KEY in user_input:
                data[CONF_KEY] = user_input[CONF_KEY]
            
            # 确保disasterlevel是字符串类型
            if CONF_DISASTERLEVEL in user_input:
                user_input[CONF_DISASTERLEVEL] = str(user_input[CONF_DISASTERLEVEL])
                data[CONF_DISASTERLEVEL] = str(user_input[CONF_DISASTERLEVEL])
            
            # 保存更新后的数据
            self.hass.config_entries.async_update_entry(
                self.config_entry, data=data
            )
            
            return self.async_create_entry(title="", data=user_input)

        # 获取当前的disasterlevel值，确保在表单中显示为整数
        current_disasterlevel = self.config_entry.options.get(
            CONF_DISASTERLEVEL, 
            self.config_entry.data.get(CONF_DISASTERLEVEL, DEFAULT_DISASTERLEVEL)
        )
        if isinstance(current_disasterlevel, str):
            current_disasterlevel = int(current_disasterlevel)
        
        # 显示配置表单
        return self.async_show_form(
            step_id="init",
            data_schema=vol.Schema(
                {
                    vol.Required(
                        CONF_LOCATION,
                        default=self.config_entry.data.get(CONF_LOCATION),
                    ): str,
                    vol.Required(
                        CONF_KEY,
                        default=self.config_entry.data.get(CONF_KEY),
                    ): str,
                    vol.Required(
                        CONF_DISASTERLEVEL,
                        default=current_disasterlevel
                    ): vol.All(vol.Coerce(int), vol.Range(min=1, max=6)),
                    vol.Required(
                        CONF_DISASTERMSG,
                        default=self.config_entry.options.get(
                            CONF_DISASTERMSG, 
                            self.config_entry.data.get(CONF_DISASTERMSG, DEFAULT_DISASTERMSG)
                        ),
                    ): vol.In(["title", "allmsg"]),
                }
            ),
        ) 