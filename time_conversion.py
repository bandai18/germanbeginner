import time_german as tg
import math


def get_half_time(hour, minute):
	time_phrase = []

	time_phrase.append(tg.get_unofficial_phrase(30))
	time_phrase.append(tg.get_12_hour(hour+1))

	return get_string_name(time_phrase)


def get_quater_time(hour, minute):
	time_phrase = []
	hour_index = 0

	time_phrase.append(tg.get_unofficial_phrase(15))
	if minute == 15:
		time_phrase.append(tg.get_preposition('after'))
	else:
		time_phrase.append(tg.get_preposition('before'))
		hour_index = 1

	time_phrase.append(tg.get_12_hour(hour + hour_index))

	return get_string_name(time_phrase)


def get_twenty_minutes(hour, minute):
	full_time_phrase = []
	
	full_time_phrase.append(get_to_half_time(hour, minute))
	full_time_phrase.append(get_twenty(hour, minute))
	
	return full_time_phrase

	
def get_twenty(hour, minute):
	time_phrase = []
	hour_index = 0
	
	time_phrase.append(tg.get_unofficial_phrase(20))
	if minute == 20:
		time_phrase.append(tg.get_preposition('after'))
	else:
		time_phrase.append(tg.get_preposition('before'))
		hour_index = 1
	
	time_phrase.append(tg.get_12_hour(hour+hour_index))
	
	return get_string_name(time_phrase)
	
	
def get_to_half_time(hour, minute):
	half_time_phrase = []	
	difference = minute - 30

	half_time_phrase.append(tg.get_unofficial_phrase(math.fabs(difference)))
	if difference < 0:
		half_time_phrase.append(tg.get_preposition('before'))
	else:
		half_time_phrase.append(tg.get_preposition('after'))
		
	half_time_phrase.append(tg.get_unofficial_phrase(30))
	half_time_phrase.append(tg.get_12_hour(hour+1))
	
	return get_string_name(half_time_phrase)


def get_five_minutes(hour, minute):
	time_phrase = []	
	hour_index = 1
	
	time_phrase.append(tg.get_unofficial_phrase(5))
	if minute < 6:
		time_phrase.append(tg.get_preposition('after'))
		hour_index = 0
	elif minute < 26:
		time_phrase.append(tg.get_preposition('before'))
		time_phrase.append(tg.get_unofficial_phrase(30))
	elif minute < 36:
		time_phrase.append(tg.get_preposition('after'))
		time_phrase.append(tg.get_unofficial_phrase(30))
	else:
		time_phrase.append(tg.get_preposition('before'))

	time_phrase.append(tg.get_12_hour(hour+hour_index))
	
	return get_string_name(time_phrase)

	
def get_ten_minutes(hour, minute):
	time_phrase = []	
	hour_index = 0
	
	time_phrase.append(tg.get_unofficial_phrase(10))
	if minute < 11:
		time_phrase.append(tg.get_preposition('after'))
	else:
		time_phrase.append(tg.get_preposition('before'))
		hour_index = 1
		
	time_phrase.append(tg.get_12_hour(hour+hour_index))

	return get_string_name(time_phrase)


def get_exact_time_phrase(hour, minute):
	full_time_phrase = []

	full_time_phrase.append(tg.get_unofficial_phrase(minute))
	full_time_phrase.append(tg.get_12_hour(hour))

	return get_string_name(full_time_phrase)


def get_phrase(hour, min):
	full_time_phrase = []

	if min % 30 == 0:
		full_time_phrase.append(get_half_time(hour, min))
	elif min % 15 == 0:
		full_time_phrase.append(get_quater_time(hour, min))
	elif min % 20 == 0:
		full_time_phrase = get_twenty_minutes(hour, min)
	elif min % 10 == 0:
		full_time_phrase.append(get_ten_minutes(hour, min))
	else:
		full_time_phrase.append(get_five_minutes(hour, min))

	return full_time_phrase


def get_german_time_phrase(hour, minute):
	time_phrase = []

	if (minute != 0 and minute % 5 == 0):
		time_phrase = get_phrase(hour, minute)
	elif minute == 0:
		time_phrase.append(get_exact_time_phrase(hour, minute))

	return time_phrase


def get_string_name(items_list):
	my_str = ' '.join(map(str, items_list))

	return my_str
