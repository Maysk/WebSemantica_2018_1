import psycopg2
from config import config
import logging

logger = logging.getLogger("MainExtractor.Database")

def bulk_insert(lista_de_instancias, keys, nome_da_tabela):
	conn = None
	sql = "INSERT INTO public."+ nome_da_tabela + "(" + ",".join(keys) + ") VALUES(" + ",".join(["%("+k+")s" for k in keys]) + ");"

	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		for instancia in lista_de_instancias:
			cur.execute(sql, instancia)

		conn.commit()
		cur.close()
	
	except(Exception, psycopg2.DatabaseError) as error:
		print("ERROR: ", error)
	
	finally:
		if conn is not None:
			conn.close()

def setup():
	if(not tabela_ja_criada("tabelas_ja_povoadas")):
		sql_command = """create table tabelas_ja_povoadas(nome_da_tabela text);"""
		try:
			params = config()
			conn = psycopg2.connect(**params)
			cur = conn.cursor()
			cur.execute(sql_command)
			cur.close()
			conn.commit()
			logger.info("Tabela 'tabelas_ja_povoadas' foi criada;")

		except psycopg2.DatabaseError as error:
			print("Error", error)

		finally:
			if conn is not None:
				conn.close()
	else:
		logger.info("Tabela 'tabelas_ja_povoadas' já foi criada anteriormente;")

def tabela_ja_povoada(nome_da_tabela):
	conn = None
	tabela_ja_povoada = True

	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		cur.execute('SELECT * from tabelas_ja_povoadas where nome_da_tabela like %s', (nome_da_tabela,))
		v = cur.fetchone()
		if v is None:
			tabela_ja_povoada = False

		cur.close()

	except psycopg2.DatabaseError as error:
		
		tabela_ja_povoada = False

	finally:
		if conn is not None:
			conn.close()
			
		return tabela_ja_povoada

def tabela_ja_criada(nome_da_tabela):
	conn = None
	existe_tabela = True

	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		cur.execute('SELECT 1 from {}'.format(nome_da_tabela))
		cur.fetchone()
		cur.close()

	except psycopg2.DatabaseError as error:
		existe_tabela = False

	finally:
		if conn is not None:
			conn.close()

		return existe_tabela

def insere_tabela_povoada(nome_da_tabela):
	sql_command = """insert into tabelas_ja_povoadas values (%s);"""
	try:
		params = config()
		conn = psycopg2.connect(**params)
		cur = conn.cursor()
		cur.execute(sql_command, (nome_da_tabela,))
		cur.close()
		conn.commit()

	except psycopg2.DatabaseError as error:
		print("Error", error)

	finally:
		if conn is not None:
			conn.close()
