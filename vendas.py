import db

destinos = ['Atibaia', 'Itatiba', 'Extrema', 'São Paulo', 'Campinas']

class Vendas:
  def __init__(self, id, nome, cpf, data_nasc, destino, assento_escolhido, forma_pagamento):
    self.id = id
    self.nome = nome
    self.cpf = cpf
    self.data_nasc = data_nasc
    self.destino = destino
    self.assento_escolhido = assento_escolhido
    self.forma_pagamento = forma_pagamento

# ----- CREATE -----
  def cadastrarVendas(self):
    formas_pag = {'0':'PIX', '1':'Cartão de Debito', '2':'Cartão de Crédito'}
    nome = input("\nNome Completo: ")
    cpf = input("\033[0;37mCPF: \033[0;30mexemplo: 12345678955 \033[0;37m")
    data_nasc = input("Data de nascimento: \033[0;30mexemplo: dd/mm/yyyy \033[0;37m")
  
    print(f"\033[0;37mEscolha o destino: \n(0) {destinos[0]} \n(1) {destinos[1]} \n(2) {destinos[2]} \n(3) {destinos[3]} \n(4) {destinos[4]}")
    op = int(input("=> "))
    if op == 0:
      destino = destinos[0] 
    if op == 1:
      destino = destinos[1] 
    if op == 2:
      destino = destinos[2] 
    if op == 3:
      destino = destinos[3] 
    if op == 4:
      destino = destinos[4]  

    assento_escolhido = input("Assento: ")
    print("\nEscolha a forma de pagamento: \n(0)",formas_pag['0'],"\n(1)",formas_pag['1'],"\n(2)",formas_pag['2'])
    pag = int(input("=> "))
    if pag == 0:
     forma_pagamento = formas_pag['0'] 
    elif pag == 1:
     forma_pagamento = formas_pag['1']
    elif pag == 2:
     forma_pagamento = formas_pag['2']
    print ("\033[0;32m\tAdicionando nova compra . . .")
    db.add_vendas(nome, cpf, data_nasc, destino, assento_escolhido, forma_pagamento)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# ----- READ -----
  def mostrarVendas(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("VENDAS CADASTRADAS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_vendas():
      print(f"\033[0;37m[{result}]")
    
# ----- UPDATE -----
  def editarVendas(self):
    formas_pag = {'0':'PIX', '1':'Cartão de Debito', '2':'Cartão de Crédito'}
    id = input("\nQual o ID da compra que deseja alterar as informações? => ")
    upd_nome = input("\nNome Completo: ")
    upd_cpf = input("\033[0;37mCPF: \033[0;30mExemplo: 12345678955 \033[0;37m")
    upd_data_nasc = input("\033[0;37mData de nascimento: \033[0;30mExemplo: dd/mm/yyyy \033[0;37m")

    print(f"Escolha o destino: \n(0) {destinos[0]} \n(1) {destinos[1]} \n(2) {destinos[2]} \n(3) {destinos[3]} \n(4) {destinos[4]}")
    op = int(input("\n=> "))
    if op == 0:
      upd_destino = destinos[0]
    if op == 1:
      upd_destino = destinos[1]
    if op == 2:
      upd_destino = destinos[2]
    if op == 3:
      upd_destino = destinos[3]
    if op == 4:
      upd_destino = destinos[4] 

    upd_assento_escolhido = input("Assento: ")
    print("Escolha a forma de pagamento: \n(0)",formas_pag['0'],"\n(1)",formas_pag['1'],"\n(2)",formas_pag['2'])
    pag = int(input("=> "))
    if pag == 0:
     upd_forma_pagamento = formas_pag['0'] 
    elif pag == 1:
     upd_forma_pagamento = formas_pag['1']
    elif pag == 2:
     upd_forma_pagamento = formas_pag['2']
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_vendas(upd_nome, upd_cpf, upd_data_nasc, upd_destino, upd_assento_escolhido, upd_forma_pagamento, id)
    print("\033[0;37m\tOperação realizada com sucesso!\n")
      
# ----- REMOVE -----
  def excluirVendas(self):
    id = input("\nQual o ID da venda que deseja excluir a compra? => ")
    print("\033[0;31m\tExcluindo venda . . .")
    db.remove_vendas(id)
    print("\033[0;37m\tOperação realizada com sucesso!\n")