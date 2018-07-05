import os
import zipfile 
import psycopg2
from config import config

def load_csv_into_table(csv_path, table_name):
	conn = None
	sql = "COPY {} FROM '{}' CSV HEADER delimiter ';' ENCODING 'WINDOWS1252';".format(table_name, csv_path)
	#print(sql)
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		cur.execute(sql)

		conn.commit()
		cur.close()
	
	except(Exception, psycopg2.DatabaseError) as error:
		print("csv_path", csv_path,"   -  -   ERROR: ", error)
	
	finally:
		if conn is not None:
			conn.close()





files_names = os.listdir('working_area/')
#print(files_names)
for file_name in files_names:
	os.rename('working_area/' + file_name, 'working_area/' + file_name.replace('ç','c').replace('ã','a'))

base_path = os.getcwd()
files_names = os.listdir('working_area/')
print(len(files_names))
i = 0
while i < len(files_names):
	print(i)
	load_csv_into_table(base_path + '\\working_area\\' + files_names[i], 'item_licitacao')
	#load_csv_into_table(base_path + '\\working_area\\' + files_names[i+1], 'licitacao')
	#load_csv_into_table(base_path + '\\working_area\\' + files_names[i+2], 'participante_licitacao')	
	#load_csv_into_table(base_path + '\\working_area\\' + files_names[i], 'contratos')
	#load_csv_into_table(base_path + '\\working_area\\' + files_names[i+1], 'item_compra')
	#load_csv_into_table(base_path + '\\working_area\\' + files_names[i+2], 'termo_aditivo')	
	i=i+3

