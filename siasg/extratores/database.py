import psycopg2
from config import config


def bulk_insert_uasg(lista_de_uasgs, keys):
	conn = None
	sql = "INSERT INTO public.uasgs(" + ",".join(keys) + ") VALUES(" + ",".join(["%("+k+")s" for k in keys]) + ");"
	print (sql)
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		for uasg in lista_de_uasgs:
			cur.execute(sql, uasg)

		conn.commit()
		cur.close()
	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ", error)
	finally:
		if conn is not None:
			conn.close()

def bulk_insert_uasg(lista_de_uasgs, keys):
	conn = None
	sql = "INSERT INTO public.uasgs(" + ",".join(keys) + ") VALUES(" + ",".join(["%("+k+")s" for k in keys]) + ");"
	print (sql)
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		for uasg in lista_de_uasgs:
			cur.execute(sql, uasg)

		conn.commit()
		cur.close()
	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ", error)
	finally:
		if conn is not None:
			conn.close()


def bulk_insert_contratos(lista_de_contratos, keys):
	conn = None
	sql = "INSERT INTO public.contratos(" + ",".join(keys) + ") VALUES(" + ",".join(["%("+k+")s" for k in keys]) + ");"
	print (sql)
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		for uasg in lista_de_contratos:
			cur.execute(sql, uasg)

		conn.commit()
		cur.close()
	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ", error)
	finally:
		if conn is not None:
			conn.close()


def get_uasgs_relevantes():
	conn = None
	rows = []
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		sql = """SELECT DISTINCT id FROM uasgs"""
		cur.execute(sql)
		rows = cur.fetchall()
		cur.close()

	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ",error)

	finally:
		if conn is not None:
			conn.close()
		return rows
