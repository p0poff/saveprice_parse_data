import datetime

class objXls:
	def __init__(self, **args):
		self.nameSeller = args.get('nameSeller')
		self.numBuyer = self.inInt(args.get('numBuyer'))
		self.nameBuyer = args.get('nameBuyer')
		self.quantity = args.get('quantity')
		self.sum = args.get('sum')
		self.price = args.get('price')
		self.priceSeller = args.get('priceSeller')
		self.savePrice = args.get('savePrice')
		self.saveTotal = args.get('saveTotal')
		self.year = self.inInt(args.get('year'))
		self.month = self.inInt(args.get('month'))

	def inInt(self, arg):
		try:
			return int(arg)
		except:
			return 0

		

	def getDate(self, excelDate):
		return datetime.datetime.fromtimestamp((int(excelDate) - 25569) * 86400).strftime('%Y-%m-%d %H:%M:%S')