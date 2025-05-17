from __future__ import division

import introduction
import time_conversion as tc
import official_time as ot
import duration_data as dd
import modal_verben as mv
import verben as vb
import duration as du
import personal_pronoun as pp
from datetime import time
import random
import re
import logging
import db


def get_time(time):
    if check_input_value(time) is not None:
        input_time = time.split(':')
        hours = int(input_time[0])
        minutes = int(input_time[1])

        final_list = [ot.get_digital_time_phrase(hours, minutes)]
        final_list.extend(tc.get_german_time_phrase(hours%12, minutes))

        return final_list
    else:
        return None


def get_rotate(time):
    input_time = time.split(':')
    hours = int(input_time[0])
    minutes = int(input_time[1])
    add_hours = float(0.5) * minutes

    rotate_list = [(hours % 12) / 12 * 360 + add_hours, minutes / 60 * 360]

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


def get_modal_questions():
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

        return tc.get_string_name(answer)
    else:
        return None


def get_verbs(items):
    """Fetch verbs matching the specified criteria.
    
    Args:
        items: A list containing regular, separable, and prefix flags.
        
    Returns:
        A list of tuples containing verb information.
        
    Raises:
        sqlite3.Error: If there is a database error.
    """
    try:
        conn = db.get_db()
        cursor = conn.cursor()
        
        query = '''
            SELECT verb, regular, separable, prefixt, pf.perfect, pf.help, meaning 
            FROM verbs vb 
            INNER JOIN perfects pf ON vb.id = pf.id 
            WHERE regular = ? AND separable = ? AND prefixt = ?
        '''
        
        # Execute query
        cursor.execute(query, (items[0], items[1], items[2]))
        
        # Fetch all results
        results = cursor.fetchall()
        
        # No need to close the database connection manually, 
        # the teardown function will handle it
        
        return results
    except Exception as e:
        logging.error(f"Error fetching verbs: {e}")
        raise


def get_all_verbs():
    """Fetch all verbs from the database.
    
    Returns:
        A list of tuples containing all verbs.
        
    Raises:
        sqlite3.Error: If there is a database error.
    """
    try:
        conn = db.get_db()
        cursor = conn.cursor()
        
        query = '''
            SELECT verb, regular, separable, prefixt, pf.perfect 
            FROM verbs vb 
            INNER JOIN perfects pf ON vb.id = pf.id
        '''
        
        # Execute query
        cursor.execute(query)
        
        # Fetch all results
        results = cursor.fetchall()
        
        # No need to close the database connection manually, 
        # the teardown function will handle it
        
        return results
    except Exception as e:
        logging.error(f"Error fetching all verbs: {e}")
        raise


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

import articles as art

def get_articles():
      return art.articles_dict

def get_nouns():
      return art.nouns

def check_article_answer(noun, article_type, answer):
      expected = art.articles_dict[art.nouns[noun]][article_type]
      return answer.lower() == expected.lower()


def get_questions():
    return introduction.questions

def get_answers():
    return introduction.answers
