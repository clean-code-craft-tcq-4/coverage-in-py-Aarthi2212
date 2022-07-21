from alert_type_factory import AlertTypeFactory
import constants as const

def infer_breach(value, lower_limit, upper_limit):
  breach_type = const.NORMAL
  if value < lower_limit:
    breach_type = const.TOO_LOW
  elif value > upper_limit:
    breach_type = const.TOO_HIGH
  return breach_type

def set_cooling_limits(cooling_type):
  upper_limit = 0
  lower_limit = 0
  limits = const.COOLING_LIMITS.get(cooling_type, None)
  if limits is not None:
    upper_limit =  limits.get(const.UPPER_LIMIT)
    lower_limit = limits.get(const.LOWER_LIMIT)
  return upper_limit, lower_limit

def classify_temperature_breach(cooling_type, temperature_in_celsius):
  upper_limit, lower_limit = set_cooling_limits(cooling_type)
  return infer_breach(temperature_in_celsius, lower_limit, upper_limit)

def alert(alert_target, breach_type):
  alert_type_factory = AlertTypeFactory(breach_type)
  alert_type = alert_type_factory.get_alert_type(alert_target)
  if alert_type != None:
    alert_type()
  else:
    print(const.UNSUPPORTED_ALERT_TARGET)

def check_and_alert_breach(alert_target, battery, temperature_in_celsius):
  breach_type =\
    classify_temperature_breach(battery.get(const.COOLING_TYPE), temperature_in_celsius)
  if breach_type not in [const.NORMAL, None]:
    alert(alert_target, breach_type)
  else:
    print(const.NO_BREACH)
