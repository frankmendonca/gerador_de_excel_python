import json


class Leitor:

	def __init__(self, columns):
		self.columns = columns

	def transform(self, column, value):
		if (column['tipo'] == 'numero'):
			value = int(value)
		else:
			value = value.strip()
		return value


class Posicional(Leitor):

	def __init__(self, columns):
		super().__init__(columns)

	def execute(self, content):
		for line in content:
			print('Line: {}'.format(line))
			position = 0
			for column in self.columns:
				length = column['tamanho']
				value = line[position:length]
				value = self.transform(column, value)
				print('{} = {}'.format(column['nome'], value))
				position = position + length


class Comma(Leitor):

	def __init__(self, columns, separator):
		super().__init__(columns)
		self.separator = separator

	def execute(self, content):
		for line in content:
			print('Line: {}'.format(line))
			position = 0
			line_splited = line.split(self.separator)
			for column in self.columns:
				value = line_splited[position]
				value = self.transform(column, value)
				print('{} = {}'.format(column['nome'], value))
				position = position + 1



files = [
	{ 'config': 'config_txt.json', 'content': 'content.txt' },
	{ 'config': 'config_csv.json', 'content': 'content.csv' }
]

for file in files:
	print()
	file_config = file['config']
	file_content = file['content']
	print('{} => {}'.format(file_config, file_content))

	with open(file_config, 'r') as data_file_config:
		config = json.load(data_file_config)

	with open(file_content, 'r') as data_file_content:
		content = data_file_content.read().split()

	if config['tipo'] == 'posicional':
		Posicional(config['colunas']).execute(content)

	if config['tipo'] == 'comma':
		Comma(config['colunas'], config['separador']).execute(content)
