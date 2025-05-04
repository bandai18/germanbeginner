import time_german as tg
import db as db
from datetime import datetime
import random
import logging


def validate_date():
    return True


def validate_date_answer(dd, mm, answer):
    try:
        dates_dict = get_date_dict()
        expected = dates_dict[int(dd)] + ' ' + dates_dict[int(mm)]
        return expected == answer
    except Exception as e:
        logging.error(f"Error validating date answer: {e}")
        return False


def create_date_answer_article(dd, mm):
    try:
        dates_dict = get_date_dict()
        answer_list = [dates_dict[dd]+'n', dates_dict[mm]+'n']
        return answer_list
    except Exception as e:
        logging.error(f"Error creating date answer article: {e}")
        return []


def get_dates_from_db():
    """Fetch date information from the database.
    
    Returns:
        A list of dates with their information.
    """
    try:
        conn = db.get_db()
        cursor = conn.cursor()
        
        # Execute query
        cursor.execute('SELECT id, date, sound FROM dates')
        
        # Fetch all results now before returning
        results = cursor.fetchall()
        
        return results
    except Exception as e:
        logging.error(f"Error fetching dates from DB: {e}")
        return []


def get_dates():
    """Get a list of all dates.
    
    Returns:
        A list of date tuples.
    """
    try:
        return get_dates_from_db()
    except Exception as e:
        logging.error(f"Error getting dates: {e}")
        return []


def get_date():
    """Generate a random date.
    
    Returns:
        A datetime object with a random date.
    """
    try:
        year = random.randint(2001, 2018)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        created_date = datetime(year, month, day)
        
        return created_date
    except Exception as e:
        logging.error(f"Error generating random date: {e}")
        # Return a fallback date
        return datetime(2020, 1, 1)


def get_date_dict():
    """Create a dictionary mapping date IDs to date names.
    
    Returns:
        A dictionary with date ID keys and date name values.
    """
    try:
        dates = get_dates_from_db()
        date_dict = {}
        
        for date in dates:
            date_dict[date[0]] = date[1]
        
        return date_dict
    except Exception as e:
        logging.error(f"Error creating date dictionary: {e}")
        return {}