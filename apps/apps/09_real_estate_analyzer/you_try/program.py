import os
from io import open		# changed for python 2.7
import csv
from data_types import Purchase
try:
	import statistics
except:
	import statistics_standin_for_py2 as statistics



def main():
	print_header()
	filename = get_data_file()
	data = load_file(filename)
	query_data(data)

def print_header():
	print('----------------------------')
	print('    REAL ESTATE APP')
	print('-----------------------------')
	print(' ')


def get_data_file():
	base_folder = os.path.dirname(__file__)
	return os.path.join(base_folder, 'data', 'SacramentoRealEstateTransactions2008.csv')

def load_file(filename):
	with open(filename, 'r', encoding = "ISO-8859-1") as fin:		# changed for python 2.7

		reader = csv.DictReader(fin)
		purchases = []
		for row in reader:
			#print("Bed count: {}".format(row['beds']))
			p = Purchase.create_from_dict(row)
			purchases.append(p)

	return purchases

		# print(purchases[0].__dict__)

		# header = fin.readline().strip()
		# reader = csv.reader(fin, delimiter = ',')
		# for row in reader:
		# 	print(type(row),row)


# def load_file_basic(filename):
# 	with open(filename, 'r', encoding = "ISO-8859-1") as fin:
# 		header = fin.readline()
# 		print("found header: " + header)

# 		lines = []
# 		for line in fin:
# 			line_data = line.strip().split(',')
# 			bed_count = line_data[4]
# 			lines.append(line_data)

# 		print(lines[:10])

# def get_price(p):
# 	return p.price


def query_data(data):

	# if data was sorted by price:
	data.sort(key = lambda p:  p.price)

	# most expensive house
	high_purchase = data[-1]
	print("The most expensive house is ${:,} with {} beds and {} baths". format(high_purchase.price,
		high_purchase.beds, high_purchase.bath))
	# least expensive house
	low_purchase = data[0]
	print("The most least house is ${:,} with {} beds and {} baths". format(low_purchase.price,
		low_purchase.beds, low_purchase.bath))

	# average price house
	prices = [p.price for p in data]
	# for pur in data:
	# 	prices.append(pur.price)
	avg_price = statistics.mean(prices)
	print("The average home price is ${:,}".format(int(avg_price)))

	# average price of 2 bedroom house
	two_bed_homes = [p for p in data if p.beds == 2]

	# prices = []
	# for pur in data:
	# 	if pur.beds == 2:
	# 		prices.append(pur.price)
	avg_price = statistics.mean([p.price for p in two_bed_homes])
	avg_baths = statistics.mean([p.bath for p in two_bed_homes])
	#avg_
	print("The average 2 bedroom home price is ${:,}".format(int(avg_price)))

if __name__ == '__main__':
    main()