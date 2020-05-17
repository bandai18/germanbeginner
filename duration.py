import duration_data as dd


def get_duration_from_dict(subject):
    obj = dd.activity_dictionary.get(subject)

    if obj is None:
        return None
    else:
        return obj.get("duration")


def get_hour_word(duration):

    return dd.activity_dictionary.get(duration)

