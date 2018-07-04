import requests, re, urllib.request

#CRIAR PASTA DADOS

anoInicial = 2013
mesInicial = 1
anoFinal = 2018
mesFinal = 3

anoAtual = anoInicial
mesAtual = mesInicial


while (anoAtual < anoFinal or (anoAtual == anoFinal and mesAtual <= mesFinal ) ):
	download_url = "http://www.portaldatransparencia.gov.br/download-de-dados/compras/{}{:02}".format(anoAtual, mesAtual)
	print("Downloading {}{:02}".format(anoAtual, mesAtual))
	nome_do_arquivo = "dados_contratos/{}{:02}.zip".format(anoAtual, mesAtual)
	urllib.request.urlretrieve(download_url, nome_do_arquivo)
	if(mesAtual == 12):
		anoAtual = anoAtual + 1
		mesAtual = 1
	else:
		mesAtual = mesAtual + 1




