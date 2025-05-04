def get_number(minute):
	hour_dictionary = {
		1: "ein",
		2: "zwei",
		3: "drei",
		4: "vier",
		5: "fünf",
		6: "sechs",
		7: "sieben",
		8: "acht",
		9: "neun",
		10: "zehn",
		11: "elf",
		12: "zwölf",
		13: "dreizehn",
		14: "vierzehn",
		15: "fünfzehn",
		16: "sechzehn",
		17: "siebzehn",
		18: "achtzehn",
		19: "neunzehn",
		20: "zwanzig",
		21: "einundzwanzig",
		22: "zwaiundzwanzig",
		23: "draiundzwanzig",
		24: "vierundzwanzig", 
		25: "fünfundzwanzig",
		26: "sechsundzwanzig",
		27: "seibundzwanzig",
		28: "achundzwanzig",
		29: "neunundzwanzig",
		30: "dreiβig",
		31: "einunddreiβig",
		32: "zweiunddreißig",
		33: "dreiunddreiβig",
		34: "vierunddreißig",
		35: "fünfunddreißig",
		36: "sechsunddreißig",
		37: "siebenunddreißig",
		38: "achtunddreiβig",
		39: "neununddreiβig",
		40: "vierzig",
		41: "einundvierzig",
		42: "zweiundvierzig",
		43: "dreiundvierzig",
		44: "vierundvierzig",
		45: "fünfundvierzig",
		46: "sechsundvierzig",
		47: "siebenundvierzig",
		48: "achtundvierzig",
		49: "neunundvierzig",
		50: "fünfzig",
		51: "einundfünfzig",
		52: "zweiundfünfzig",
		53: "dreiundfünfzig",
		54: "vierundfünfzig",
		55: "fünfundfünfzig",
		56: "sechsundfünfzig",
		57: "siebenundfünfzig",
		58: "achtundfünfzig",
		59: "neunundfünfzig",
		0: "zwölf"
	}
	return hour_dictionary.get(minute)


def getUnofficialPhrase(minute):
	phrase_dictionary =	{	
		5: "fünf",
		10: "zehn",
		15: "Viertel",
		20: "zwanzig",
		30: "halb",
		1: "eins",
		0: "um"
	}
	return phrase_dictionary.get(minute)


def getPreposition(prep):
	phrase_dictionary =	{
		"after": "nach",
		"before": "vor"
	}
	return phrase_dictionary.get(prep)


def get12Hour(hour):
	hour_dictionary =	{
		1: "eins",
		2: "zwei",
		3: "drei",
		4: "vier",
		5: "fünf",
		6: "sechs",
		7: "sieben",
		8: "acht",
		9: "neun",
		10: "zehn",
		11: "elf",
		12: "zwolf",
		0: "zwolf"
	}
	return hour_dictionary.get(hour)
