from init import init
from pyxlsb import open_workbook as open_xlsb
from object import obj
import saver

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
	raise Exception('no this sheet')

def workData(**args):
	def f(iter):
		__args = args
		row = next(iter)
		# print('\r\n'.join([str(x) for x in row]))
		i = 0
		__break = False
		while True:
			i += 1
			data = []
			for x in range(args.get('offset', 1)):
				try:
					row = next(iter)
				except:
					__break = True
					break
				data.append(row)
			args.get('handler').save((getDataObject(x, __args.get('sheet')) for x in data))
			if (__args.get('limit', True) and i == 10) or __break: break

	return f

def getIterData(**args):
	with open_xlsb(init.file) as wb:
		with wb.get_sheet(args.get('sheet', 0)) as sheet:
			rows = sheet.rows()
			args.get('callback', lambda x: print(x))(rows)

def run():
	print('run sheet #1....')
	sheet = 1
	getIterData(
		sheet=sheet, 
		callback=workData(
			handler=saver.Saver(table='price_save_gas_data', init=init), 
			sheet=sheet, 
			limit=False, 
			offset=100
		)
	)
	print('run sheet #2....')
	sheet = 2
	getIterData(
		sheet=sheet, 
		callback=workData(
			handler=saver.Saver(table='price_save_elec_data', init=init), 
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
