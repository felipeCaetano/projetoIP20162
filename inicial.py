#!/usr/bin/python
#_*_ coding: utf-8 _*_
import os,sys
# Sistemas de Venda ao Cliente - SVC
#Versão 0.0.0
# Vende os produtos previamente cadastrados.
#Se não houver cadastro de produtos é necessário cadastrar primeiro
#Só é possível vender se houver estoque suficiete.
#Se não houver estoque suficiente um aviso deve ser emitido
#Funções Disponiveis:
#1- Iniciar Venda
#1.1 - Novo Produto
#1.2 - Finalizar Venda
#2- Cadastrar Produto
#2.1 - Cadastra
#2.2 - Altera Cadastro
#2.3 - Apaga
#0- Sair do Sistema
from funcoes import *

produtos={}

while 1:
    print("\n******* Sistema de Vendas ao Consumidor ****************")
    print("Digite a opção Desejada:\n1- Iniciar Venda\n2- Cadastrar Produto\n0-Fechar Programa")
    entrada=input(">>")
    if entrada.isdigit():
        if entrada=="0":
            print("terminado.")
            break
        elif entrada=="1":
            iniciar_vendas(produtos)
        elif entrada=="2":
            cadastrar_produto(produtos)
        else:
            print("\nOpção Inválida\n")
    else:
        print("\nOpção Inválida\n")

