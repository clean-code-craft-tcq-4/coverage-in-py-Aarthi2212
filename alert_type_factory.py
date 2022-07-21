import constants as const
from alert import Alert
class AlertTypeFactory:
    def __init__(self, breach_type) -> None:
        self.alert = Alert(breach_type)
    def get_alert_type(self, alert_target):
        alert_type = {
            const.CONTROLLER_ALERT: self.alert.send_to_controller,
            const.EMAIL_ALERT: self.alert.send_to_email
        }
        return alert_type.get(alert_target, None)