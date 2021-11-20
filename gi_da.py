import pandas as pd


# classe de erro e erro personalizado
class Error(Exception):
	pass


class UnknownCMD(Error):
	def __init__(self, message):
		self.message = message


# mostrar tudo
def fullopen(file):
	print(file)


# quantos de cada tipo
def type_count(file, extra = None):
	# mostra quantos de cada tipo (weapon, char)
	if extra is None:
		print(file.groupby(['type']).type.count())
	elif extra == '-w':
		cond = file.type == 'weapon'
		print(file.loc[cond].groupby(['rarity']).rarity.count())
	elif extra == '-c':
		cond = file.type == 'char'
		print(file.loc[cond].groupby(['rarity']).rarity.count())


# lista quantas personagens total
def all_chars(file):
	print(file.loc[file.type == 'char'])


# lista quantas personagens 5 estrelas
def all_5_stars(file, extra = None):
	if extra is None or extra == '-list':
		cond1 = file.type == 'char'
		cond2 = file.rarity == 5
		print(file.loc[cond1 & cond2, ['date', 'running_banner', 'wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-count':
		cond1 = file.type == 'char'
		cond2 = file.rarity == 5
		print(file.loc[cond1 & cond2].rarity.count())


# lista quantas armas 4 estrelas
def all_4_stars(file, extra1 = None):
	if extra1 is None or extra1 == '-list':
		print(file.loc[file.rarity == 4])
	elif extra1 == '-chars':
		cond1 = file.type == 'char'
		cond2 = file.rarity == 4
		print(file.loc[cond1 & cond2, ['date', 'running_banner', 'wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra1 == '-wp':
		cond1 = file.type == 'weapon'
		cond2 = file.rarity == 4
		print(file.loc[cond1 & cond2, ['date', 'running_banner', 'wish', 'rarity', 'weapon']])
	elif extra1 == '-count':
		cond = file.rarity == 4
		print(file.loc[cond].groupby(['type']).rarity.count())		


# quantas personagens por sex
def sex_sort(file, extra = None):
	if extra == '-f':
		print(file.loc[file.sex == 'F', ['date', 'running_banner', 'wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-m':
		print(file.loc[file.sex == 'M', ['date', 'running_banner', 'wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra is None:
		print(file.groupby(['sex']).sex.count())


# quantas personagens por arma
def weapon_sort(file, extra = None):
	if extra == '-s':
		cond1 = file.type == 'char'
		cond2 = file.weapon == 'Sword'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-p':
		cond1 = file.type == 'char'
		cond2 = file.weapon == 'Polearm'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-b':
		cond1 = file.type == 'char'
		cond2 = file.weapon == 'Bow'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-ca':
		cond1 = file.type == 'char'
		cond2 = file.weapon == 'Catalyst'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-cl':
		cond1 = file.type == 'char'
		cond2 = file.weapon == 'Claymore'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra is None:
		print(file.loc[file.type == 'char'].groupby(['weapon']).weapon.count())


# quantas personagens por elemento
def elem_sort(file, extra = None):
	if extra is None:
		print(file.loc[file.type == 'char'].groupby(['element']).element.count())
	elif extra == '-a':
		cond1 = file.type == 'char'
		cond2 = file.element == 'Anemo'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-c':
		cond1 = file.type == 'char'
		cond2 = file.element == 'Cryo'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-e':
		cond1 = file.type == 'char'
		cond2 = file.element == 'Electro'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-g':
		cond1 = file.type == 'char'
		cond2 = file.element == 'Geo'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-h':
		cond1 = file.type == 'char'
		cond2 = file.element == 'Hydro'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])
	elif extra == '-p':
		cond1 = file.type == 'char'
		cond2 = file.element == 'Pyro'
		print(file.loc[cond1 & cond2, ['wish', 'rarity', 'weapon', 'element', 'sex']])


def help_fun():  # listar comandos
	print('''
		+-------+
		| AJUDA |
		+-------+

		-help 					Ajuda, lista comandos e suas aplicações.
		
		-all	 				Lista todos os registros de wishes gerados.

		-amount [OPTION] 		Lista a quantidade de registros por tipo.

			-w 					Lista a quantidade de armas por raridade.

			-c 					Lista a quantidade de personagens por raridade.

		-allchars 				Lista todas as personagens obtidos.

		-allfive [OPTION] 		Lista todos os registros de personagens 5 estrelas.

			-list 				(Default) Lista todos os registros de personagens 5 estrelas.

			-count 				Mostra a quantidade de personagens 5 estrelas obtida.

		-allfour [OPTION] 		Lista todos os registros de raridade 4 estrelas.

			-list 				(Default) Lista todos os registros 4 estrelas.

			-chars 				Lista apenas as personagens de raridade 4 estrelas.

			-wp 				Lista apenas as armas 4 estrelas.

			-count 				Mostra a quantidade de personagens e de armas 4 estrelas.

		-sex [OPTION] 			Mostra a quantidade de personagens por sexo.

			-f 					Lista as personagens femininas.

			-m 					Lista as personagens masculinas.

		-charwp [OPTION] 		Mostra a quantidade de personagens por arma utilizada.

			-b 					Lista as personagens que usam arco.

			-ca 				Lista as personagens que usam catalisador.

			-cl 				Lista as personagens que usam \'Claymore\'.

			-p 					Lista as personagens que usam lança.

			-s 					Lista as personagens que usam espada.

		-charelem [OPTION] 		Mostra a quantidade de personagens por elemento/visão.

			-a 					Lista as personagens de visão Anemo.

			-c 					Lista as personagens de visão Cryo.

			-e 					Lista as personagens de visão Electro.

			-g 					Lista as personagens de visão Geo.

			-h 					Lista as personagens de visão Hydro.

			-p 					Lista as personagens de visão Pyro.

		-exit 					Encerra o GI-DA.

		----------Fim da ajuda.
	''')


print('''
	----------- GI-DA -----------
	Genshin Impact - Data Analyst
	   coded by samuelfarrus
''')

# variáveis genéricas
comandos = []  # adicionar comandos

# entrada
entry = input(
	'Digite o nome do arquivo a ser carregado.\nOu deixe vazio para arquivo de nome padrão \'genshin_dataset.csv\'.'
)

# validação de entrada (.csv)
if bool(entry) is False:
	entry = 'genshin_dataset.csv'
elif '.csv' not in entry:
	entry = entry + '.csv'

# criação de dataframe
df = pd.read_csv('{}'.format(entry), parse_dates=['date'], index_col=[0], na_values=[None])

# execução do programa
print('CSV carregado. Digite a consulta desejada, -help para ajuda ou -exit para encerrar.')

while True:
	try:
		request = input('GI-DA> ')

		if bool(request) is False:
			pass
		elif request[0] != '-':
			raise UnknownCMD('Unknown/Invalid command.')

	except UnknownCMD as uc:
		print(uc)

	else:
		if request == '-all':
			fullopen(df)
		elif request[0:7] == '-amount':
			if len(request) == 7:
				type_count(df)
			elif len(request) > 7:
				if request[8:] not in ['-c', '-w']:
					pass
				else:
					x = request[8:]
					type_count(df, x)
		elif request == '-allchars':
			all_chars(df)
		elif request[0:8] == '-allfive':
			if len(request) == 8:
				all_5_stars(df)
			elif len(request) > 8:
				if request[9:] not in ['-list', '-count']:
					pass
				else:
					x = request[9:]
					all_5_stars(df, x)
		elif request[0:8] == '-allfour':
			if len(request) == 8:
				all_4_stars(df)
			elif len(request) > 8:
				if request[9:] not in ['-list', '-chars', '-wp', '-count']:
					pass
				else:
					x = request[9:]
					all_4_stars(df, x)
		elif request[0:4] == '-sex':
			if len(request) == 4:
				sex_sort(df)
			elif len(request) > 4:
				if request[5:] not in ['-f', '-m']:
					pass
				else:
					x = request[5:]
					sex_sort(df, x)
		elif request[0:7] == '-charwp':
			if len(request) == 7:
				weapon_sort(df)
			elif len(request) > 7:
				if request[8:] not in ['-s', '-p', '-b', '-ca', '-cl']:
					pass
				else:
					x = request[8:]
					weapon_sort(df, x)
		elif request[0:9] == '-charelem':
			if len(request) == 9:
				elem_sort(df)
			elif len(request) > 9:
				if request[10:] not in ['-a', '-c', '-e', '-g', '-h', '-p']:
					pass
				else:
					x = request[-2:]
					elem_sort(df, x)
		elif request == '-help':
			help_fun()
		elif request == '-exit':
			break

print('GI-DA encerrado.')
