import constants as const
class Alert:
    def __init__(self, breach_type) -> None:
        self.breach_type = breach_type

    def send_to_controller(self):
        header = 0xfeed
        print(f'{header}, {self.breach_type}')

    def send_mail(self, message):
        print(f'To: {const.RECEPIENT}')
        print(message)

    def send_to_email(self):
        if self.breach_type == const.TOO_LOW:
            message = const.EMAIL_LOW_TEMPERATURE
        else:
            message = const.EMAIL_HIGH_TEMPERATURE
        self.send_mail(message)
        