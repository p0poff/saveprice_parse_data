from init import init
from pyxlsb import open_workbook as open_xlsd
from object import obj
from object_xls import objXls
import saver
import saver_xls
import time
from xlrd import open_workbook as open_xlsx

def getDataObject(row, sheet):
	if sheet == 1:
		return obj(
			numSeller = 	row[2].v,
			nameSeller = 	row[3].v,
			numBuyer = 		row[8].v,
			nameBuyer = 	row[9].v,
			dateOrder = 	row[13].v,
			quantity = 		row[18].v,
			amount = 		row[20].v,
			year = 			row[21].v,
			month = 		row[22].v
			)
	if sheet == 2:
		return obj(
			numSeller = 	row[4].v,
			nameSeller = 	row[5].v,
			numBuyer = 		row[11].v,
			nameBuyer = 	row[12].v,
			dateOrder = 	row[17].v,
			quantity = 		row[29].v,
			amount = 		row[31].v,
			year = 			row[34].v,
			month = 		row[33].v
			)
	if sheet == 0:
		return objXls(
			nameSeller = 	row[10].value,
			numBuyer = 		row[1].value,
			nameBuyer = 	row[0].value,
			quantity = 		row[4].value,
			sum = 			row[5].value,
			price = 		row[7].value,
			priceSeller = 	row[6].value,
			savePrice = 	row[8].value,
			saveTotal = 	row[9].value,
			year = 			row[2].value,
			month = 		row[3].value
			)
	raise Exception('no this sheet')

def getIterChank(iter, offset):
	__break = False
	data = []
	for x in range(offset):
		try:
			row = next(iter)
		except:
			__break = True
			break
		data.append(row)
	return __break, data

def workData(**args):
	def f(iter):
		#title
		row = next(iter)
		# print('\r\n'.join([str(x) for x in row]))
		i = 0
		while True:
			i += 1
			__break, data = getIterChank(iter, args.get('offset', 1))
			args.get('handler').save((getDataObject(x, args.get('sheet')) for x in data))
			if (args.get('limit', True) and i == 10) or __break: break

	return f

def getIterData(**args):
	with open_xlsd(init.file) as wb:
		with wb.get_sheet(args.get('sheet', 0)) as sheet:
			rows = sheet.rows()
			args.get('callback', lambda x: print(x))(rows)

def getIterDataXlsx(**args):
	with open_xlsx(init.file) as wb:
		sh = wb.sheet_by_index(args.get('sheet', 0))
		rows = (sh.row(rx) for rx in range(sh.nrows))
		args.get('callback', lambda x: print(x))(rows)

def run():
	time.sleep(3)
	# print('run sheet #1....')
	# sheet = 1
	# getIterData(
	# 	sheet=sheet, 
	# 	callback=workData(
	# 		handler=saver.Saver(table='price_save_gas_data', init=init), 
	# 		sheet=sheet, 
	# 		limit=True, 
	# 		offset=100
	# 	)
	# )
	# print('run sheet #2....')
	# sheet = 2
	# getIterData(
	# 	sheet=sheet, 
	# 	callback=workData(
	# 		handler=saver.Saver(table='price_save_elec_data', init=init), 
	# 		sheet=sheet, 
	# 		limit=False, 
	# 		offset=100
	# 	)
	# )

	print('run sheet #1....')
	sheet = 0
	getIterDataXlsx(
		sheet=sheet, 
		callback=workData(
			handler=saver_xls.Saver(table='price_save_gas_data', init=init), 
			sheet=sheet, 
			limit=False, 
			offset=100
		)
	)
	
def main():
	print('Start price save application...')
	run()
	print('End price save application')

if __name__ == '__main__':
	main()
