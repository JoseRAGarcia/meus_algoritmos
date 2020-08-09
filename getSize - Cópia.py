import os
import re
from tkinter import filedialog

def calcula(path):
	#Definido o caminho do backup
	dirBkp = path #'C:/Uteis/bkp/Dedo.old'

	#Entrando no diretório do backup
	os.chdir(dirBkp)
	#Criando arquivo txt com informações do conteúdo do diretório
	os.system('dir /s /w > C:/temp/lista.txt')
	#Abrindo o arquivo txt criado
	arquivo = open('C:/temp/lista.txt', 'r', encoding='iso-8859-1')
	#Incluindo cada linha do arquivo em uma lista
	lista = arquivo.readlines()
	#Fechando o arquivo (as informações já estão na lista, não precisamos mais do arquivo aberto)
	arquivo.close()
	#Verificando o tamanho da lista
	tamLista = len(lista)
	#Sabe-se que a informação que precisamos se encontra no segundo índice de trás pra frente, logo se diminui o tamanho da lista por 2
	localInformacao = tamLista-2
	#Capturamos a informação bruta e alfanumérica em uma variável
	infBruta = lista[localInformacao]
	#Retiramos os 27 primeiros caracters que não são desejáveis
	infLiq = infBruta[27:]
	#Retiramos todo caracter não numérico da informação e transformamos o resto da informação em um número inteiro
	if re.sub('[^0-9]', '',infLiq) != '':
		infFinal = int(re.sub('[^0-9]', '',infLiq))
	else:
		infFinal = 0

	#os.system('pause')
	os.chdir('C:/temp')
	os.system('del lista.txt')

	#Printando os resultados
	if infFinal >= 1073741824:	
		print('Localizado um backup de {:.2f} GB ({} bytes).'.format(infFinal/1073741824, infFinal))
	elif infFinal >= 1048576:
		print('Localizado um backup de {:.2f} MB ({} bytes).'.format(infFinal/1048576, infFinal))
	elif infFinal >= 1024:
		print('Localizado um backup de {:.2f} KB ({} bytes).'.format(infFinal/1024, infFinal))
	else:
		print(f'Localizado um backup de {infFinal} bytes.')

	return infFinal

origem = filedialog.askdirectory(title = 'Selecionar local de origem')

calcula(origem)