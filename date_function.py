import time_german as tg
import db as db
from datetime import datetime
import random


def validate_date():
    return True


def validate_date_answer(dd, mm, answer):
    dates_dict = get_date_dict()
    expected = dates_dict[int(dd)] + ' ' + dates_dict[int(mm)]
    print(answer)
    print(expected)
    print(answer == expected)
    return expected == answer


def create_date_answer_article(dd, mm):
    dates_dict = get_date_dict()
    answer_list = [dates_dict[dd]+'n', dates_dict[mm]+'n']

    return answer_list


def get_dates_from_db():
    cur = db.get_db().cursor()
    res = cur.execute('select id, date, sound from dates ')
    db.close_db()

    return res


def get_dates():
    res = get_dates_from_db()

    datelist = []
    for re in res:
        datelist.append(re)

    return datelist


def get_date():
    year = random.randint(2001, 2018)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    created_date = datetime(year, month, day)

    return created_date


def get_date_dict():
    dates = get_dates()
    datadict = {}

    for date in dates:
        datadict.update({date[0]: date[1]})

    return datadict
