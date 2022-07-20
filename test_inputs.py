import constants as const

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

ALERT_INPUT_OUTPUT = [
    {
        const.COOLING_TYPE : const.PASSIVE_COOLING,
        const.ALERT_TARGET: const.EMAIL_ALERT,
        const.VALUE: 30,
        const.RESULT: "No Breach\n"
    },
    {
        const.COOLING_TYPE : const.MED_ACTIVE_COOLING,
        const.ALERT_TARGET: const.EMAIL_ALERT,
        const.VALUE: 70,
        const.RESULT: "{}\n{}\n".format(f'To: {const.RECEPIENT}', 'Hi, the temperature is too high')
    },
    {
        const.COOLING_TYPE : const.HI_ACTIVE_COOLING,
        const.ALERT_TARGET: const.CONTROLLER_ALERT,
        const.VALUE: 70,
        const.RESULT: '65261, TOO_HIGH\n'
   
    }
]