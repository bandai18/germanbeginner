import time_german as tg
import math


def get_half_time(hour, minute):
	timePhrase = []

	timePhrase.append(tg.getUnofficialPhrase(30))
	timePhrase.append(tg.get12Hour(hour+1))

	return getStringName(timePhrase)


def get_quater_time(hour, minute):
	timePhrase = []
	hourIndex = 0

	timePhrase.append(tg.getUnofficialPhrase(15))
	if minute == 15:
		timePhrase.append(tg.getPreposition('after'))
	else:
		timePhrase.append(tg.getPreposition('before'))
		hourIndex = 1

	timePhrase.append(tg.get12Hour(hour + hourIndex))

	return getStringName(timePhrase)


def get_twenty_minutes(hour, minute):
	fullTimePhrase = []
	
	fullTimePhrase.append(get_to_half_time(hour, minute))
	fullTimePhrase.append(get_twenty(hour, minute))
	
	return fullTimePhrase

	
def get_twenty(hour, minute):
	timePhrase = []
	hourIndex = 0
	
	timePhrase.append(tg.getUnofficialPhrase(20))
	if minute == 20:
		timePhrase.append(tg.getPreposition('after'))
	else:
		timePhrase.append(tg.getPreposition('before'))
		hourIndex = 1
	
	timePhrase.append(tg.get12Hour(hour+hourIndex))
	
	return getStringName(timePhrase)
	
	
def get_to_half_time(hour, minute):
	halfTimePhrase = []	
	difference = minute - 30

	halfTimePhrase.append(tg.getUnofficialPhrase(math.fabs(difference)))
	if difference < 0:
		halfTimePhrase.append(tg.getPreposition('before'))
	else:
		halfTimePhrase.append(tg.getPreposition('after'))
		
	halfTimePhrase.append(tg.getUnofficialPhrase(30))
	halfTimePhrase.append(tg.get12Hour(hour+1))
	
	return getStringName(halfTimePhrase)


def get_five_minutes(hour, minute):
	timePhrase = []	
	hourIndex = 1
	
	timePhrase.append(tg.getUnofficialPhrase(5))
	if minute < 6:
		timePhrase.append(tg.getPreposition('after'))
		hourIndex = 0
	elif minute < 26:
		timePhrase.append(tg.getPreposition('before'))
		timePhrase.append(tg.getUnofficialPhrase(30))
	elif minute < 36:
		timePhrase.append(tg.getPreposition('after'))
		timePhrase.append(tg.getUnofficialPhrase(30))
	else:
		timePhrase.append(tg.getPreposition('before'))

	timePhrase.append(tg.get12Hour(hour+hourIndex))
	
	return getStringName(timePhrase)

	
def get_ten_minutes(hour, minute):
	timePhrase = []	
	hourIndex = 0
	
	timePhrase.append(tg.getUnofficialPhrase(10))
	if minute < 11:
		timePhrase.append(tg.getPreposition('after'))
	else:
		timePhrase.append(tg.getPreposition('before'))
		hourIndex = 1
		
	timePhrase.append(tg.get12Hour(hour+hourIndex))

	return getStringName(timePhrase)


def get_exact_time_phrase(hour, minute):
	fullTimePhrase = []

	fullTimePhrase.append(tg.getUnofficialPhrase(minute))
	fullTimePhrase.append(tg.get12Hour(hour))

	return getStringName(fullTimePhrase)


def get_phrase(hour, min):
	fullTimePhrase = []

	if min % 30 == 0:
		fullTimePhrase.append(get_half_time(hour, min))
	elif min % 15 == 0:
		fullTimePhrase.append(get_quater_time(hour, min))
	elif min % 20 == 0:
		fullTimePhrase = get_twenty_minutes(hour, min)
	elif min % 10 == 0:
		fullTimePhrase.append(get_ten_minutes(hour, min))
	else:
		fullTimePhrase.append(get_five_minutes(hour, min))

	return fullTimePhrase


def get_german_time_phrase(hour, minute):
	timePhrase = []

	if (minute != 0 and minute % 5 == 0):
		timePhrase = get_phrase(hour, minute)
	elif minute == 0:
		timePhrase.append(get_exact_time_phrase(hour, minute))

	return timePhrase


def getStringName(list):
	my_str = ' '.join(map(str, list))

	return my_str
