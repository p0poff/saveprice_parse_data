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
			
		q = 'INSERT INTO %s (id, num_seller, name_seller, num_buyer, name_buyer, date_order, quantity, amount, year, month) VALUES %s' % (
			self.table, ','.join(
				"(NEXTVAL('{table}_id_seq'), '{numSeller}', '{nameSeller}', '{numBuyer}', '{nameBuyer}', '{dateOrder}', {quantity}, {amount}, {year}, {month})".format(
					table=self.table,
					numSeller=str(x.numSeller), 
					nameSeller=x.nameSeller.replace("'", "''"),
					numBuyer=str(x.numBuyer),
					nameBuyer=x.nameBuyer.replace("'", "''"),
					dateOrder=x.dateOrder,
					quantity=x.quantity,
					amount=x.amount,
					year=x.year,
					month=x.month					
				) for x in genData
			)
		)
		self.runQuery(q)

	def clear(self):
		return 'DELETE FROM %s' % (self.table)

	def runQuery(self, q):
		self.db.run_query(q)


