import db

class Passagem():
  def __init__(self, id_passagem, destino, preco):
    self.id_passagem = id_passagem
    self.destino = destino
    self.preco = preco

# ----- CREATE -----
  def cadastrarPassagem(self):
    destinos = ['Atibaia', 'Itatiba', 'Extrema', 'São Paulo', 'Campinas']
    print(f"Escolha o destino: \n(0) {destinos[0]} \n(1) {destinos[1]} \n(2) {destinos[2]} \n(3) {destinos[3]} \n(4) {destinos[4]}")
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
    preco = input("Valor da passagem: R$")
    print ("\033[0;32m\tCadastrando nova passagem . . .")
    db.add_passagem(destino, preco)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# ----- READ -----
  def mostrarPassagem(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("PASSAGENS CADASTRADAS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_passagem():
      print(f"\033[0;37m[{result}]")
    
# ----- UPDATE -----
  def editarPassagem(self):
    id = input("\nQual o ID da passagem que deseja editar => ")
    print("\nPreencha os campos a seguir com as informações atualizadas da passagem:")
    destinos = ['Atibaia', 'Itatiba', 'Extrema', 'São Paulo', 'Campinas']
    print(f"\nEscolha o destino: \n(0) {destinos[0]} \n(1) {destinos[1]} \n(2) {destinos[2]} \n(3) {destinos[3]} \n(4) {destinos[4]}")
    op = int(input("=> "))
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
    upd_preco = input("Valor da passagem: R$")
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_passagem(upd_destino, upd_preco, id)
    print("\033[0;37m\tOperação realizada com sucesso!\n")
      
# ----- REMOVE -----
  def excluirPassagem(self):
    id = input("\nQual o ID da passagem que deseja apagar => ")
    print("\033[0;31m\tApagando passagem . . .")
    db.remove_passagem(id)
    print("\033[0;37m\tOperação realizada com sucesso!\n")