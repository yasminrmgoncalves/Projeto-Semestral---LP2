import db

class Onibus:
  def __init__(self, placa, assentos):
    self.placa = placa
    self.assentos = assentos

# ----- CREATE -----
  def criarOnibus(self):
    placa = input("\nInsira a placa do novo onibus => ")
    while len(placa) != 7:
      placa = input("\033[0;33m\tDado Inválido!\033[0;37m\nInsira a placa do novo ônibus => ")
    assentos = input("Insira os assentos do novo onibus => ")
    print ("\033[0;32m\tAdicionando novo ônibus . . .")
    db.add_onibus(placa, assentos)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# ----- READ -----
  def mostrarOnibus(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("ONIBUS CADASTRADOS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_onibus():
      print(f"\033[0;37m[{result}]")
    
# ----- UPDATE -----
  def editarOnibus(self):
    placa = input("\033[0;37m\nQual a placa do ônibus que deseja editar? => ")
    upd_placa = input("\033[0;37mDigite a nova placa => ")
    while len(upd_placa) != 7:
      upd_placa = input("\033[0;33m\tDado Inválido!\033[0;37m\nInsira a placa do novo ônibus => ")
    upd_assento = input("\033[0;37mDigite a quantidade dos assentos => ")
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_onibus(upd_placa,upd_assento, placa)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# ----- REMOVE -----
  def excluirOnibus(self):
    placa = input("\033[0;37m\nQual a placa do ônibus que deseja excluir => ")
    print("\033[0;31m\tExcluindo ônibus . . .")
    db.remove_onibus(placa)
    print("\033[0;37m\tOperação realizada com sucesso!\n")