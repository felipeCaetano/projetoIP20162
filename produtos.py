class Categoria():
	def __init__(self):
		self.codigo=Categoria.set_codigo(self)
		self.nome=Categoria.set_nome(self)
		self.descricao=Categoria.set_descricao(self)
		

	def set_codigo(self):
		codigo=input("CÓDIGO: ")
		return codigo
		
	def set_nome(self):
		nome=input("NOME: ")
		return nome

	def set_descricao(self):
		descricao=input("DESCRIÇÃO:")
		return descricao
		
	def get_codigo(self):
		return self.codigo
		
	def get_nome(self):
		return self.nome

	def get_descricao(self):
		return self.descricao

	
class Subcategoria(Categoria):
	def __init__(self,Categoria):
		self.cat=Categoria
		super().__init__()
		
class Produtos(Subcategoria):
	def __init__(self,Subcategoria):
		self.sub=Subcategoria
		#TODO: criar os atributos de Produtos
		#	   criar os metodos de Produtos 
