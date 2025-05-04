import time_german as tg
import time_conversion as tc

uhr_str = "Uhr"


def get_digital_time_phrase(hour, minute):
    full_time_phrase = []

    full_time_phrase.append(tg.get_number(hour))
    full_time_phrase.append(uhr_str)

    # -- When Time is like 12:00
    if minute != 0:
        full_time_phrase.append(tg.get_number(minute))

    return tc.get_string_name(full_time_phrase)

