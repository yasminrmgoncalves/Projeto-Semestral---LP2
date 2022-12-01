import db

class Motorista:
  def __init__(self, nome_m, cpf_m, data_nasc_m, endereco, salario):
    self.nome_m = nome_m
    self.cpf_m = cpf_m
    self.data_nasc_m = data_nasc_m
    self.endereco = endereco
    self.salario = salario

# ----- CREATE -----
  def cadastrarMotorista(self):
    print("Preencha os campos a seguir com as informações do novo motorista:")
    novo_motorista = input("\nNome Completo: ")
    cpf = input("\033[0;37mCPF: \033[0;30mExemplo: 12345678955 \033[0;37m")
    data_nasc = input("\033[0;37mData de nascimento: \033[0;30mExemplo: dd/mm/yyyy \033[0;37m")
    endereco = input("Endereço: ")
    salario = input("Salário: R$")
    print ("\033[0;32m\tCadastrando novo motorista . . .")
    db.add_motorista(novo_motorista, cpf, data_nasc, endereco, salario)
    print("\033[0;37m\tOperação realizada com sucesso!\n")

# ----- READ -----
  def mostrarMotorista(self):
    QTD_COLUNAS = 60
    print("\033[0;35m-" * QTD_COLUNAS)
    print("{:^60}".format("MOTORISTA CADASTRADOS"))
    print("-" * QTD_COLUNAS)
    for result in db.get_motorista():
      print(f"\033[0;37m[{result}]")
    
# ----- UPDATE -----
  def editarMotorista(self):
    cpf = input("\nQual o CPF do motorista que deseja editar => ")
    print("\nPreencha os campos a seguir com as informações atualizadas do motorista:")
    upd_motorista = input("\nNome Completo: ")
    upd_cpf = input("\033[0;37mCPF: \033[0;30mExemplo: 12345678955 \033[0;37m")
    upd_data_nasc = input("\033[0;37mData de nascimento: \033[0;30mExemplo: dd/mm/yyyy \033[0;37m")
    upd_endereco = input("Endereço: ")
    upd_salario = input("Salário: R$")
    print("\033[0;34m\tAtualizando as informações. . .")
    db.update_motorista(upd_motorista, upd_cpf, upd_data_nasc, upd_endereco, upd_salario, cpf)
    print("\033[0;37m\tOperação realizada com sucesso!\n")
      
# ----- REMOVE -----
  def excluirMotorista(self):
    cpf = input("\nQual o CPF do motorista que deseja apagar => ")
    print("\033[0;31m\tApagando motorista . . .")
    db.remove_motorista(cpf)
    print("\033[0;37m\tOperação realizada com sucesso!\n")