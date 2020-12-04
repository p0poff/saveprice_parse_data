import datetime

class obj:
	def __init__(self, **args):
		self.numSeller = self.inInt(args.get('numSeller'))
		self.nameSeller = args.get('nameSeller')
		self.numBuyer = self.inInt(args.get('numBuyer'))
		self.nameBuyer = args.get('nameBuyer')
		self.dateOrder = self.getDate(args.get('dateOrder'))  
		self.quantity = args.get('quantity')
		self.amount = args.get('amount')
		self.year = self.inInt(args.get('year'))
		self.month = self.inInt(args.get('month'))

	def inInt(self, arg):
		try:
			return int(arg)
		except:
			return 0

		

	def getDate(self, excelDate):
		return datetime.datetime.fromtimestamp((int(excelDate) - 25569) * 86400).strftime('%Y-%m-%d %H:%M:%S')