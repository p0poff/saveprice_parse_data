import go_postgres

class Saver:
	def __init__(self, **args):
		self.table = args['table']
		self.init = args['init']
		self.db = go_postgres.db_query(self.init.dbInitToDict())
		self.runQuery(self.clear())

	def save(self, genData):
		if genData is None:
			return
		
		q = 'INSERT INTO %s (id, name_seller, num_buyer, name_buyer, quantity, sum, price_seller, price, save_price, save_total, year, month) VALUES %s' % (
			self.table, ','.join(
				"(NEXTVAL('{table}_id_seq'), '{nameSeller}', '{numBuyer}', '{nameBuyer}', {quantity}, {sum}, {priceSeller}, {price}, {savePrice}, {saveTotal}, {year}, {month})".format(
					table=self.table,
					nameSeller=x.nameSeller.replace("'", "''"),
					numBuyer=str(x.numBuyer),
					nameBuyer=x.nameBuyer.replace("'", "''"),
					quantity=x.quantity,
					sum=x.sum,
					priceSeller=x.priceSeller,
					price=x.price,
					savePrice=x.savePrice,
					saveTotal=x.saveTotal,
					year=x.year,
					month=x.month					
				) for x in genData
			)
		)
		self.runQuery(q)

	def clear(self):
		return 'DELETE FROM %s' % (self.table)

	def runQuery(self, q):
		print(q)
		self.db.run_query(q)