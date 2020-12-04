import os

class Init(object):
	
	def __init__(self, **args):
		super(Init, self).__init__()
		self.host = args.get('host')
		self.user = args.get('user')
		self.passwd = args.get('passwd')
		self.port = args.get('port')
		self.db = args.get('db')
		self.file = args.get('file')

	def dbInitToDict(self):
		return {
		'db': self.db,
		'host': self.host,
		'port': int(self.port),
		'user': self.user,
		'passwd': self.passwd
		}

init = Init(
	host=os.environ['HOST'],
	user=os.environ['USER'],
	passwd=os.environ['PASS'],
	port=os.environ['PORT'],
	db=os.environ['DB'],
	file='/data/' + os.environ['FILE']
	)
		