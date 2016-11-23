#!/usr/bin/python
#_*_ coding: utf-8 _*_
import os, sys
# Cadastro de clientes, fornecedores e funcionÃ¡rios

class Pessoa():
    def __init__(self):
        self.nome=Pessoa.setNome(self)
        while self.nome=="Nome Inválido":
            print("Nome Inválido")
            self.nome=Pessoa.setNome(self)     
            
        self.endereco=Pessoa.setEndereco(self)
        while self.endereco=="Endereço Inválido":
            print("Endereço Inválido")
            self.endereco=Pessoa.setEndereco(self) 
            
        self.numero=Pessoa.setNumero(self)
        while self.numero=="Número Inválido":
            print("Número Inválido")
            self.numero=Pessoa.setNumero(self)
            
        self.bairro=Pessoa.setBairro(self)
        while self.bairro=="Bairro Inválido":
            print("Bairro Inválido")
            self.bairro=Pessoa.setBairro(self)   
            
        self.cidade=Pessoa.setCidade(self)
        while self.cidade=="Cidade Inválida":
            print("Cidade Inválida")
            self.cidade=Pessoa.setCidade(self) 
            
        self.CEP=Pessoa.setCEP(self)
        while self.CEP=="CEP Inválido":
            print("CEP Inválido")
            self.CEP=Pessoa.setCEP(self)
            
        self.estado=Pessoa.setEstado(self)
        while self.estado=="Estado Inválido":
            print("Estado Inválido")
            self.estadoe=Pessoa.setEstado(self) 
            
        self.telefone=Pessoa.setTelefone(self)
        while self.telefone=="Telefone Inválido":
            print("Telefone Inválido")
            self.telefone=Pessoa.setTelefone(self) 
            
        self.celular=Pessoa.setCelular(self)
        while self.celular=="Celular Inválido":
            print("Celular Inválido")
            self.celular=Pessoa.setCelular(self)  
            
        self.email=Pessoa.setEmail(self)
        while self.email=="Email Inválido":
            print("Email Inválido")
            self.email=Pessoa.setEmail(self)   
            
        self.rg=Pessoa.set_rg(self)
        while self.rg==False:
            print("RG Inválido")
            self.rg=Pessoa.set_rg(self)  
            
        self.cadastro=Pessoa.set_cadastro(self)
        while self.cadastro==False:
            print("CPF\CNPJ Inválido")
            self.cadastro=Pessoa.set_cadastro(self)  
        
    #metodos seters
    def setNome(self):
        nome=input("Nome: ")
        self.nome=Pessoa.validaNome(nome)
        return self.nome
    def setEndereco(self):
        endereco=input("Endereco: ")
        self.endereco=Pessoa.validaEndereco(endereco)
        return self.endereco
    def setNumero(self):
        numero=input("Número: ")
        self.numero=Pessoa.validaNumero(numero)
        return self.numero
    def setBairro(self):
        bairro=input("Bairro: ")
        self.bairro=Pessoa.validaBairro(bairro)
        return self.bairro    
    def setCidade(self):
        cidade=input("Cidade: ")
        self.cidade=Pessoa.validaCidade(cidade)
        return self.cidade    
    def setEstado(self):
        estado=input("Estado: ")
        self.estado=Pessoa.validaEstado(estado)
        return self.estado
    def setTelefone(self):
        telefone=input("Telefone: ")
        self.telefone=Pessoa.validaTelefone(telefone)
        return self.telefone
    def setCelular(self):
        celular=input("Celular: ")
        self.celular=Pessoa.validaCelular(celular)
        return self.celular
    def setEmail(self):
        email=input("Email: ")
        self.email=Pessoa.validaEmail(email)
        return self.email
    def set_rg(self):
        rg=input("RG: ")
        self.rg=Pessoa.valida_rg(rg)
        return self.rg
    def set_cadastro(self):
        cadastro=input("Cadastro(CPF ou CNPJ): ")
        self.cadastro=Pessoa.valida_cadastro(cadastro)
        return self.cadastro
    def setCEP(self):
        CEP=input("CEP: ")
        self.CEP=Pessoa.validaCEP(CEP)
        return self.CEP
    
    #metodos geters
    def getNome(self):
        return self.nome
    def getEndereco(self):
        return self.endereco
    def getNumero(self):
        return self.numero
    def getBairro(self):
        return self.bairro
    def getCidade(self):
        return self.cidade
    def getEstado(self):
        return self.estado
    def getTelefone(self):
        return self.telefone
    def getCelular(self):
        return self.celular
    def getEmail(self):
        return self.email
    def get_rg(self):
        return self.rg
    def get_cadastro(self):
        return self.cadastro
    def getCEP(self):
        return self.CEP
   
    #validadores
    def validaNome(nome):
        n=nome.split()
        for c in n:
            if not c.isalpha():
                return "Nome Inválido"
        else:
            return nome
        
    def validaEndereco(endereco):
        end=endereco.split()
        for e in end:
            if not e.isalnum():
                return "Endereço Inválido"
        else:
            return endereco
        
    def validaNumero(numero):
        nb=numero.split()
        for number in nb:
            if not number.isdigit():
                return "Número Inválido"
        else:
            return numero 
      
    def validaBairro(bairro):
        b=bairro.split()
        for nbh in b:
            if not nbh.isalpha():
                return "Bairro Inválido"
        else:
            return bairro
        
    def validaCidade(cidade):
        c=cidade.split()
        for city in c:
            if not city.isalpha():
                return "Cidade Inválida"
        else:
            return cidade   
        
    def validaEstado(estado):
        estados=['AC','AL','AP','AM','BA','CE','DF','ES','GO','MA','MT','MS','MG',
        'PA','PB','PR','PE','PI','RJ','RN','RS','RO','RR','SC','SP','SE','TO']
      
        e=estado.split()
        for state in e:
          if state.upper() not in estados:
            return "Estado Inválido"
        else:
          return estado
          
    def validaCEP(CEP):
        CEP=CEP.replace("-","")
        if len(CEP)!=8:
            return "CEP Inválido"
        elif CEP.isdigit():
            return CEP
        
    def validaTelefone(telefone):
        telefone=telefone.replace("(","")
        telefone=telefone.replace(")","")
        telefone=telefone.replace("-","")
        
        if telefone=="":
            return telefone
        elif len(telefone)<8:
            return "Telefone Inválido"
        elif 8<len(telefone)<=10 and telefone.isdigit():
            return telefone
        
    def validaCelular(celular):
        celular=celular.replace("(","") 
        celular=celular.replace(")","")
        celular=celular.replace("-","")
        
        if celular=="":
            return celular
        if len(celular)<9:
            return "Celular Inválido"
        if len(celular)==9 and celular[0]!='9':
            return "Celular Inválido"
        if len(celular)==11 and celular[2]!='9':
            return "Celular Inválido"
        else:
            return celular
        
    def validaEmail(email):
        '''Verificador de email fraco
        @TODO - Usar expressões regulares
        verifica apenas se tem @ e .com
        '''
        if email!="":
            pos=email.find('@')
            if pos>0:
                if email.find(".com")>0:
                    return email
                else:
                    return "Email Inválido"
            else:
                    return "Email Inválido"
        else:
            return "Email Inválido"
                
    def valida_rg(RG):
        if RG=="":
            return RG
        if RG!="" and 5<=len(RG)<=7:
            if RG.isdigit():
                return RG
            else:
                return False
        else:
            return False
                 
    def valida_cadastro(cadastro):
        result=0
        # XX.XXX.XXX/YYYY-ZZ
        cadastro=cadastro.replace("-","") #remove o traço se houver
        cadastro=cadastro.replace(".","")
        cadastro=cadastro.replace("/","")
        if len(cadastro)<11:
            return False   #maior ou menor q 11 n vale
        if len(cadastro)==11:
            a=[int(x) for x in range(2,11)]
            a.reverse() #primeira parte da vericação
            for i in range(9):
                result+=int(cadastro[i])*a[i]

            result=(result*10)%11
            if result==10: #se resto da divisão for 10
                result=0

            if result==int(cadastro[9]):#verificação 1 ok.
                result=0
                b=[int(x) for x in range(2,12)]
                b.reverse()
                for i in range(10):
                    result+=int(cadastro[i])*b[i]

                result=(result*10)%11
                if result==int(cadastro[10]): #verificação 2 ok.
                    return cadastro
                else:
                    return False
            else:
                return False
        elif len(cadastro) == 14:
            #valida cnpj    11.222.333/0001-XX.
            lista=[5,4,3,2,9,8,7,6,5,4,3,2]
            resultado=0
            for i in range(12):
                resultado+=lista[i]*int(cadastro[i])
            resultado%=11
            
            if resultado<2:
                resultado=0
            else:
                resultado=11-resultado
                
            if resultado==int(cadastro[12]):
                lista=[6,5,4,3,2,9,8,7,6,5,4,3,2]
                resultado=0
                for i in range(13):
                    resultado+=lista[i]*int(cadastro[i])
                
                resultado%=11
                
                if resultado<2:
                    resultado=0
                else:
                    resultado=11-resultado
                    
                if resultado==int(cadastro[13]):
                    return cadastro
                else:
                    return False
            else:
                return False
                    
    def __str__(self):
        #listaparametros=[self.nome,self.endereco]
        #return listaparametros
        return self.nome
    
class Cliente(Pessoa):
    
    #cliente tem data de nascimento
    def __init__(self):
        Pessoa.__init__(self)
        self.datanasc=Cliente.set_data_nasc(self)
        while self.datanasc==False:
            print("Data Inválida")
            self.datanasc=Cliente.set_data_nasc(self)

    def set_data_nasc(self):
        data=input("DN(dd/mm/aaaa): ")
        self.datanasc=Cliente.valida_data(data)
        return self.datanasc
    
    def get_data_nasc(self):
        return self.datanasc
    
    def valida_data(data):
        data=data.replace("/","")
        if data=="":
            return data
        else:
            if int(data[0:2])>31:
                return False
            if int(data[2:4])>12:
                return False
            #TODO:se ano maior q ano atual tb deve retornar False
            if len(data)==8 and data.isdigit():
                return data
            else:
                return False
            
        
class Fornecedores(Pessoa):
    
    #fornecedor tem cnpj
    def __init__(self):
        pass
    
    
class Funcionario(Pessoa):
    
    #TODO: cliente tem foto
    
    def __init__(self):
        self.datanasc=Funcionario.set_data_nasc(self)
        while self.datanasc==False:
            print("Data Inválida")
            self.datanasc=Funcionario.set_data_nasc(self)

    def set_data_nasc(self):
        data=input("DN(dd/mm/aaaa): ")
        self.datanasc=Funcionario.valida_data(data)
        return self.datanasc
    
    def get_data_nasc(self):
        return self.datanasc
    
    def valida_data(data):
        data=data.replace("/","")
        if data=="":
            return data
        else:
            if int(data[0:2])>31:
                return False
            if int(data[2:4])>12:
                return False
            #TODO:se ano maior q ano atual tb deve retornar False
            if len(data)==8 and data.isdigit():
                return data
            else:
                return False

pessoa1=Cliente()
print(pessoa1)
