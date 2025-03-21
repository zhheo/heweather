"""和风天气集成的常量."""

DOMAIN = "heweather"
DEFAULT_NAME = "和风天气"

# 配置项
CONF_LOCATION = "location"
CONF_KEY = "key"
CONF_DISASTERLEVEL = "disasterlevel"
CONF_DISASTERMSG = "disastermsg"

# 默认值
DEFAULT_DISASTERLEVEL = "3"
DEFAULT_DISASTERMSG = "allmsg"

# 灾害等级
DISASTER_LEVEL = {
    "Cancel": 0,
    "None": 0,
    "Unknown": 0,
    "Standard": 1,
    "Minor": 2,
    "Moderate": 3,
    "Major": 4,
    "Severe": 5,
    "Extreme": 6
}

# 属性
ATTR_UPDATE_TIME = "更新时间"
ATTR_SUGGESTION = "建议"
ATTRIBUTION = "来自和风天气的天气数据" 