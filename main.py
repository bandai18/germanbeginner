from __future__ import division
import TimeConversion as tc
import officialTime as ot
import durationData as dd
import modalverben as mv
import verben as vb
import duration as du
import personalpronoun as pp
from datetime import time
import random
import re
import db as db


def get_time(time):
    if check_input_value(time) is not None:
        input_time = time.split(':')
        hh = int(input_time[0])
        mm = int(input_time[1])

        final_list = [ot.get_digital_time_phrase(hh, mm)]
        final_list.extend(tc.get_german_time_phrase(hh%12, mm))

        return final_list
    else:
        return None


def get_rotate(time):
    input_time = time.split(':')
    hh = int(input_time[0])
    mm = int(input_time[1])
    addhh = float(0.5) * mm

    rotate_list = [(hh % 12) / 12 * 360 + addhh, mm / 60 * 360]

    return rotate_list


def check_input_value(time):
    match = re.search(r'^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$', time)
    print(match)
    if match is not None:
        return time
    else:
        return None


def get_practice_time_value():
    hh = random.randint(0, 23)
    mm = random.randint(0, 59)

    t = time(hh, mm)
    time_display = '{:%H:%M}'.format(t)

    return time_display


def get_duration():

   return dd.activity_dictionary


def get_modalverb():

    return mv.modal_dictionary


def get_pronoun():

    return mv.pronoun_tuple


def get_modalquestions():
    num = len(mv.modal_questions)
    index = random.randint(0, num-1)

    return mv.modal_questions[index]


def evaluate_answer(enteredanswer, modal):

    return enteredanswer == modal


def get_duration_answer(subject):
    answer = []

    if subject != '':
        answer.append(subject)
        answer.append("dauert")
        temp_answer = du.get_duration_from_dict(subject)
        if temp_answer is not None:
            answer.append(temp_answer)
        else:
            return None
        answer.append(dd.stunden_dictionary.get('plural'))

        return tc.getStringName(answer)
    else:
        return None


def get_verbs(items):
    cur = db.get_db().cursor()
    res = cur.execute('select verb, regular, separable, prefixt, pf.perfect, pf.help, meaning from verbs vb ' +
                      'inner join perfects pf on vb.id = pf.id ' +
                      'where regular == {0} and separable == {1} and prefixt == {2}'
                      .format(items[0], items[1], items[2]))
    db.close_db()

    return res


def get_allverbs():
    cur = db.get_db().cursor()
    res = cur.execute('select verb, regular, separable, prefixt, pf.perfect from verbs vb ' +
                      'inner join perfects pf on vb.id = pf.id ')
    db.close_db()

    return res


def get_verb_question(verbs):
    verblist = []
    for verb in verbs:
        verblist.append(verb)

    num = len(verblist)
    index = random.randint(0, num-1)
    question = vb.modal_questions[verblist[index][0]]

    return question


def get_verb_same_question(verb):
    question = vb.modal_questions[verb]

    return question


def evaluate_perfect(past, pastkey, perfect, perfectkey):
    if past == pastkey and perfect == perfectkey:
        return "True"
    else:
        return "False"


def get_pronoun_nominative():

    return pp.pronoun


def get_pronoun_table():

    pronoun = pp.pronoun
    titles = ['nominative', 'akkusative', 'dative']
    keys = ['singular-one', 'singular-two', 'singular-three-m',
    'singular-three-f', 'singular-three-n', 'plural-one', 'plural-two',
    'plural-three', 'formal']
    table = []

    for key in keys:
        row = []
        for title in titles:
            row.append(pronoun[title][key])
        table.append(row)

    return table
