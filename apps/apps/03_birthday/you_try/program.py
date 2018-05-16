import datetime

def print_header():
	print('----------------------------')
	print('        BIRTHDAY APP')
	print('-----------------------------')
	print()


def get_birthday_from_user():
	print("When were you born? ")
	year = int(raw_input("Year [YYYY]: "))
	month = int(raw_input("Month [MM]: "))
	day = int(raw_input("Day [DD]: "))

	bday = datetime.date(year, month, day)

	return bday

def compute_days_between_date(original_date, target_date):
	this_year = datetime.date(target_date.year, original_date.month, original_date.day)
	dt = this_year - target_date
	return dt.days

def print_birthday_information(days):
	if days < 0:
		print("You had your BIRTHDAY {} days ago this year.".format(-days))
	elif days > 0:
		print("Your birthday is in {} days!".format(days))
	elif days == 0:
		print("ToDAY IS YOUR BIRTHDAY!!!")
	pass

def main():
	print_header()
	bday = get_birthday_from_user()
	now = datetime.date.today()
	number_of_days = compute_days_between_date(bday, now)
	print_birthday_information(number_of_days)

main()