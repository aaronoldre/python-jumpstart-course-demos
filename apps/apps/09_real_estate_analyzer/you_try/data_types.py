
class Purchase:
	def __init__(self, street, city, zipcode, state, beds,
		bath, sq__ft, home_type, sale_date, price,
		latitude, longitude):
		self.street = street
		self.city = city
		self.zipcode = zipcode
		self.state = state
		self.beds = beds
		self.bath = bath
		self.sq__ft = sq__ft
		self.home_type = home_type
		self.sale_date = sale_date
		self.price = price
		self.latitude = latitude
		self.longitude = longitude

	@staticmethod
	def create_from_dict(lookup):
		return Purchase(
			lookup['street'],
			lookup['city'],
			lookup['zip'],
			lookup['state'],
			int(lookup['beds']),
			int(lookup['baths']),
			int(lookup['sq__ft']),
			lookup['type'],
			lookup['sale_date'],
			float(lookup['price']),
			float(lookup['latitude']),
			float(lookup['longitude']))