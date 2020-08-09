import os
import re
from tkinter import filedialog

folders = ['Contacts', 'Desktop', 'Documents', 'Downloads', 'Favorites', 'Pictures', 'Music', 'Videos', 'AppData/Local/Google/Chrome']

def calcula(path):
	#Definido o caminho a ser calculado
	dirBkp = path #'C:/Uteis/bkp/Dedo.old'
	tamTotal = 0

	for i in range(len(folders)):
		if os.path.exists(os.path.join(dirBkp, folders[i])):
			#Criando e esvaziando a lista a cada laço
			lista = []
			#Entrando no diretório a ser calculado
			os.chdir(os.path.join(dirBkp, folders[i]))
			#Criando arquivo txt com informações do conteúdo do diretório
			os.system(f'dir /s /w > C:/temp/lista{i}.txt')
			#Abrindo o arquivo txt criado
			arquivo = open(f'C:/temp/lista{i}.txt', 'r', encoding='iso-8859-1')
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

			tamTotal+=infFinal

			os.chdir('C:/temp')
			os.system(f'del lista{i}.txt')
		else:
			#Criando e esvaziando a lista a cada laço
			lista = []
			#Entrando no diretório a ser calculado
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

			tamTotal+=infFinal

			os.chdir('C:/temp')
			os.system('del lista.txt')
			break

	
	
	
	
	

	#Printando os resultados
	if tamTotal >= 1073741824:	
		print('Localizado um backup de {:.2f} GB ({} bytes).'.format(tamTotal/1073741824, tamTotal))
	elif tamTotal >= 1048576:
		print('Localizado um backup de {:.2f} MB ({} bytes).'.format(tamTotal/1048576, tamTotal))
	elif tamTotal >= 1024:
		print('Localizado um backup de {:.2f} KB ({} bytes).'.format(tamTotal/1024, tamTotal))
	else:
		print(f'Localizado um backup de {tamTotal} bytes.')
	
	return tamTotal

#origem = filedialog.askdirectory(title = 'Selecionar local de origem')

#calcula(origem)
