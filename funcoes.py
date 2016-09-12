#!/usr/bin/python
#_*_ coding: utf-8 _*_
import os,sys
# Modulo de funções do Sistema de Vendas
# To change this template file, choose Tools | Templates
# and open the template in the editor.


def iniciar_vendas(produtos):
    '''
    Cria ambiante para inciar vendas ao consumidor
    se houver produtos cadastrados o operadorador
    devera digitar o código do produto, a quantidade de produto
    e depois escolher se um novo produto entrará na lista
    caso contrário encerra a venda
    '''
    operacoes=[]
    continuar_vendendo=True
    total=0
    
    
    print("Iniciar Vendas\n")
    if len(produtos)==0:
        print("\nNão Existe produtos cadastrados!\nCadastrar Produtos para inicar vendas. ")
        cadastrar_produto(produtos)     #produtos ainda esta vazio
        iniciar_vendas(produtos)        #produtos não está mais vazio
    else:
        print("Vendas Iniciadas")   #colocar aqui açoes para vender
        while continuar_vendendo:
            
            codigo_info=input("Digite o código do produto: ").strip()

            #validação
            if codigo_info.isdigit():
                codigo_info=int(codigo_info)
            else:
                print("Código Inválido!")
                iniciar_vendas(produtos)

            #trecho de debug
            if codigo_info not in produtos:
                print("Produto não Cadastrado!")
                opcao=input("Deseja Cadastrar? (S/N)").strip()
                opcao=opcao.lower()
                if opcao=='s':
                    cadastrar_produto(produtos)
                else:
                    iniciar_vendas(produtos)
            #fim de trecho de debug

            quantidade_info=input("Digite a Quantidade: ").strip()
            #validação
            if quantidade_info.isdigit():
                quantidade_info=int(quantidade_info)
                if quantidade_info<=0:
                    print("Impossível Vender: 0 OU MENOS ITENS")
                    iniciar_vendas(produtos)
            else:
                print("Digite quantidade válida")
                iniciar_vendas(produtos)

            #trecho de debug
            if codigo_info in produtos:
                total_prod=(produtos[codigo_info][1]*quantidade_info)
                operacoes.append([quantidade_info, produtos[codigo_info][0], total_prod])
                #print("%d: %s = %.2f" % (quantidade_info, produtos[codigo_info][0], total_prod))

                opcao=input("Deseja Continuar Compra? (S/N)").strip()
                opcao=opcao.lower()
                if opcao=='s':
                    total+=total_prod
                    for op in operacoes:
                        print("%d: %s = %.2f" % (op[0],op[1],op[2]))
                else:
                    total+=total_prod
                    finalizar_vendas(total,operacoes)
                    continuar_vendendo=False
        #fim de trecho de debug

        
def finalizar_vendas(total,operacoes):
    
    '''mostra na tela a lista de produtos comprados
        informa o valor total e habilita a função pagamento
    '''
    for op in operacoes:
        print("%d: %s = %.2f" % (op[0],op[1],op[2]))
    print("Valor Total: %.2f" % total)
    realizar_pagamento(total)
    

def realizar_pagamento(total):
    '''
    função pagamentos recebe dinheiro do cliente
    verifica se o pagamento foi suficiente
    informa troco
    salva o fluxo de caixa
    '''
    dinheiro_valido=False
    while not dinheiro_valido:
        dinheiro=input("Dinheiro: R$ ").strip()
        #validação
        if not dinheiro.isalpha():
            dinheiro=float(dinheiro)
            dinheiro_valido=True
        else:
            print("digite um Valor Válido!")
    else:
        if dinheiro<total:
            print("Valor insuficiente para pagamento")
            realizar_pagamento(total)
        else:
            troco=float(dinheiro)-float(total)
            print("Troco: R$ %.2f" % troco)
            #TODO - salvar fluxo de caixa
            
            
def cadastrar_produto(produtos):
    '''
    Cadastra produtos para vendas no formato:
    (Código Nome Preço_Unitário Quantidade_em_Estoque)
    Solicitando se novos produtos devem ser cadastrados em seguida
    caso contrário salva o cadastro realizado e o(s) produtos já estarão 
    disponíveis para venda.
    '''
    cadastro_confirmado=False
    print("\nCadastrar Produto\n")
    while not (cadastro_confirmado):
        #recebe e valida os dados
        codigo=input("Digite o código: ").strip()
        if codigo.isdigit():
            codigo=int(codigo)
        else:
            print("Codigo Invalido")
            cadastrar_produto(produtos)
        nome=input("Digite o nome do Produto: ").strip()
        if len(nome)==0:
            print("Nome não pode ser em Branco")
            cadastrar_produto(produtos)
        else:
            nome=nome.upper()
        preco=input("Digite o preço unitário: ").strip()
        if not preco.isalpha():
            preco=float(preco)
        else:
            print("digite um preço válido")
            cadastrar_produto(produtos)
        quantidade=input("Digite a quantidade em estoque: ").strip()
        if quantidade.isdigit():
            quantidade=int(quantidade)
            if quantidade<=0:
                print("Impossível Cadastrar: 0 OU MENOS ITENS")
                cadastrar_produto(produtos)
        else:
            print("Digite quantidade válida")
        cadastro_confirmado=True
    else:
        print("Código\tNome\t\tPreço\tQuantidade")
        print("%d\t%s\t%.2f\t%d \n- Cadastrado com Sucesso\n"% (codigo,nome,preco,quantidade))
    produtos[codigo]=[nome,preco,quantidade]
    for key in produtos:
        print(produtos[key])

    
    

def alterar_produtos():
    pass

def retirar_produto():
    pass
