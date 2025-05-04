import time_german as tg
import time_conversion as tc

uhr_str = "Uhr"


def get_digital_time_phrase(hour, minute):
    fullTimePhrase = []

    fullTimePhrase.append(tg.get_number(hour))
    fullTimePhrase.append(uhr_str)

    # -- When Time is like 12:00
    if minute != 0:
        fullTimePhrase.append(tg.get_number(minute))

    return tc.get_string_name(fullTimePhrase)

