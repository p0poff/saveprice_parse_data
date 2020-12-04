from pg import DB

class db_query:
	def __init__(self, auth):
		self.auth = auth
		self.connect()

	def __del__(self):
		try:
			self.db.close()
		except:
			pass

	def connect(self):
		self.db = DB(dbname=self.auth['db'], host=self.auth['host'], port=self.auth['port'], user=self.auth['user'], passwd=self.auth['passwd'])

	def run_query(self, query, *args):
		def send_query(q):
			return self.db.query(q)
		try:
			res = send_query(query)
		except:
			self.connect()
			res = send_query(query)
		return res

	def array_query(self, query, *args):
		res = self.run_query(query)
		return res.dictresult()