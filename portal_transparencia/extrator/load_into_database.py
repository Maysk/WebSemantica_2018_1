import os
import zipfile 
import psycopg2
from config import config

def load_csv_into_table(csv_path, table_name):
	conn = None
	sql = "COPY {} FROM '{}' CSV HEADER delimiter ';';".format(table_name, csv_path)
	print(sql)
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		
		cur.execute(sql)

		conn.commit()
		cur.close()
	
	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ", error)
	
	finally:
		if conn is not None:
			conn.close()





files_names = os.listdir('dados/')

for name in zipfile.ZipFile("dados/"+files_names[0]).namelist():
    print('Listing zip files: %s' % name)

#f = zipfile.ZipFile('dados/' + files_names[0])
#f.extractall('working_area')
#f.close()

#base_path = os.getcwd()

#arquivos_extraidos = os.listdir('working_area/')

#load_csv_into_table(base_path + '\\working_area\\' + arquivos_extraidos[0], 'item_licitacao')



#for fname in files_names:

