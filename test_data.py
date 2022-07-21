import constants as const
email_format = "{}\n{}\n"
controller_format = '{}, {}\n'
controller_header = 65261

INFER_BREACH_INPUT_OUTPUT = [
    {
        const.VALUE: 20,
        const.LOWER_LIMIT: 50,
        const.UPPER_LIMIT: 100,
        const.RESULT: const.TOO_LOW
    },
    {
        const.VALUE: 70,
        const.LOWER_LIMIT: 50,
        const.UPPER_LIMIT: 100,
        const.RESULT: const.NORMAL
    },
    {
        const.VALUE: 110,
        const.LOWER_LIMIT: 50,
        const.UPPER_LIMIT: 100,
        const.RESULT: const.TOO_HIGH
    }]

CLASSIFICATION_INPUT_OUTPUT = [
    {
        const.COOLING_TYPE: const.HI_ACTIVE_COOLING,
        const.VALUE: -20,
        const.RESULT: const.TOO_LOW
    },
    {
        const.COOLING_TYPE: const.MED_ACTIVE_COOLING,
        const.VALUE: 20,
        const.RESULT: const.NORMAL
    },
    {
        const.COOLING_TYPE: const.PASSIVE_COOLING,
        const.VALUE: 40,
        const.RESULT: const.TOO_HIGH
    }
]

COOLING_LIMIT_INPUT_OUTPUT = [
    {
        const.COOLING_TYPE : const.PASSIVE_COOLING,
        const.RESULT: (35, 0)
    },
    {
        const.COOLING_TYPE : const.MED_ACTIVE_COOLING,
        const.RESULT: (40, 0)
    },
    {
        const.COOLING_TYPE : const.HI_ACTIVE_COOLING,
        const.RESULT: (45, 0)
    }
]

CHECK_ALERT_INPUT_OUTPUT = [
    {
        const.COOLING_TYPE : const.PASSIVE_COOLING,
        const.ALERT_TARGET: const.EMAIL_ALERT,
        const.VALUE: 30,
        const.RESULT: "{}\n".format(const.NO_BREACH)
    },
    {
        const.COOLING_TYPE : const.MED_ACTIVE_COOLING,
        const.ALERT_TARGET: const.EMAIL_ALERT,
        const.VALUE: 70,
        const.RESULT: email_format.format(f'To: {const.RECEPIENT}', const.EMAIL_HIGH_TEMPERATURE)
    },
    {
        const.COOLING_TYPE : const.HI_ACTIVE_COOLING,
        const.ALERT_TARGET: const.CONTROLLER_ALERT,
        const.VALUE: 70,
        const.RESULT: controller_format.format(controller_header, const.TOO_HIGH)
   
    }
]

ALERT_INPUT_OUTPUT = [
    {
        const.ALERT_TARGET: const.EMAIL_ALERT,
        const.BREACH_TYPE: const.TOO_HIGH,
        const.RESULT: email_format.format(f'To: {const.RECEPIENT}', const.EMAIL_HIGH_TEMPERATURE)
    },
    {
        const.ALERT_TARGET: const.EMAIL_ALERT,
        const.BREACH_TYPE: const.TOO_LOW,
        const.RESULT: email_format.format(f'To: {const.RECEPIENT}', const.EMAIL_LOW_TEMPERATURE)
    },
    {
        const.ALERT_TARGET: const.CONTROLLER_ALERT,
        const.BREACH_TYPE: const.TOO_HIGH,
        const.RESULT: controller_format.format(controller_header, const.TOO_HIGH)
    },
    {
        const.ALERT_TARGET: const.CONTROLLER_ALERT,
        const.BREACH_TYPE: const.TOO_LOW,
        const.RESULT: controller_format.format(controller_header, const.TOO_LOW)
    },
    {
        const.ALERT_TARGET: "TO_SMS",
        const.BREACH_TYPE: const.TOO_LOW,
        const.RESULT: "{}\n".format(const.UNSUPPORTED_ALERT_TARGET)
    }
]