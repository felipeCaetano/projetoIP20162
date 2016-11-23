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
            
        self.RG=Pessoa.setRG(self)
        while self.RG=="RG Inválido":
            print("RG Inválido")
            self.RG=Pessoa.setRG(self)  
            
        self.CPF=Pessoa.setCPF(self)
        while self.CPF=="CPF Inválido":
            print("CPF Inválido")
            self.CPF=Pessoa.setCPF(self)  
        
    
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
    def setRG(self):
        RG=input("RG: ")
        self.RG=Pessoa.validaRG(RG)
        return self.RG
    def setCPF(self):
        CPF=input("CPF: ")
        self.CPF=Pessoa.validaCPF(CPF)
        return self.CPF
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
    def getNumeroRG(self):
        return self.RG
    def getCPF(self):
        return self.CPF
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
                    print(pos)
                    return email
                else:
                    return "Email Inválido"
            else:
                    return "Email Inválido"
        #elif email=="":     #o campo pode ser deixado em branco.
         #   return email
        else:
            return "Email Inválido"
                
    def validaRG(RG):
        if RG!="" and 5<=len(RG)<=7:
            if RG.isdigit():
                return RG
            else:
                return "RG Inválido"
        else:
            return "RG Inválido"
                
        
    def validaCPF(CPF):
        result=0
        CPF=CPF.replace("-","") #remove o traço se houver
        CPF=CPF.replace(".","")
        if len(CPF)!=11:
            return "CPF Inválido"   #maior ou menor q 11 n vale
        a=[int(x) for x in range(2,11)]
        a.reverse() #primeira parte da vericação
        for i in range(9):
            result+=int(CPF[i])*a[i]
      
        result=(result*10)%11
        if result==10:
            result=0
        
        if result==int(CPF[9]):#verificação 1 ok.
            result=0
            b=[int(x) for x in range(2,12)]
            b.reverse()
            for i in range(10):
                result+=int(CPF[i])*b[i]
          
            result=(result*10)%11
            if result==int(CPF[10]): #verificação 2 ok.
                return CPF
            else:
                return "CPF Inválido"
        else:
            return "CPF Inválido"
    
    def __str__(self):
        #listaparametros=[self.nome,self.endereco]
        #return listaparametros
        return self.nome
    
class Cliente(Pessoa):
    #cliente tem foto
    #cliente tem data de nascimento
    #cliente tem fax
    def __init__(self):
        Pessoa.__init__(self)
        self.datanasc=None
     

class Fornecedores(Pessoa):
    #fornecedor tem cnpj
    #fornecedor tem fax
    def __init__(self):
        pass
class Funcionarios(Pessoa):
    #funcionÃ¡rio tem data de nascimento
    def __init__(self):
        pass


pessoa1=Cliente()
print(pessoa1.email)
