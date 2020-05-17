import time_german as tg
import time_conversion as tc

uhr_str = "Uhr"


def get_digital_time_phrase(hour, minute):
    fullTimePhrase = []

    fullTimePhrase.append(tg.getNumber(hour))
    fullTimePhrase.append(uhr_str)

    # -- When Time is like 12:00
    if minute != 0:
        fullTimePhrase.append(tg.getNumber(minute))

    return tc.getStringName(fullTimePhrase)

