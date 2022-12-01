from onibus import Onibus
from passagem import Passagem
from motorista import Motorista
from vendas import Vendas

import matplotlib.pyplot as mp

meses = ('Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho')
valores = (155245, 103240, 50515, 64895, 78210, 110560)

# --- MENU PRINCIPAL ---

tracejado = lambda x: print("\033[0;34m-" * x)
QTD_COLUNAS = 60

def exibir_menuPRINCIPAL():
  while True:
    tracejado(QTD_COLUNAS)
    print("{:^60}".format("BUS PASS"))
    tracejado(QTD_COLUNAS)

    try:
      
      opcao = int(input("\033[0;37mO que deseja fazer?\n(1) Gerenciar Ônibus\n(2) Gerenciar Passagens \n(3) Gerenciar Motoristas\n(4) Gerenciar Vendas\n(5) Gráfico de Faturamento \n(99) Sair \n=>  "))

      if opcao == 1:
        menuONIBUS()
      elif opcao == 2:
        menuPASSAGEM()
      elif opcao == 3:
        menuMOTORISTA()
      elif opcao == 4:
        menuVENDAS()
      elif opcao == 5:
        mp.title('Faturamento no primeiro semestre de 2022')
        mp.plot(meses, valores)
        mp.xlabel('Meses')
        mp.ylabel('Faturamento em R$')
        mp.show()
      elif opcao == 99:
        break
      else:
        print("\nOpção não reconhecida, por favor informar um número das opções acima")
    except ValueError as e:
      print("\nOpção não reconhecida, por favor informar um número das opções acima", e)
    finally:
      if opcao == 99:
        print("\033[0;32m\n\taté mais :D\n")
      else:
        print("\033[0;31m\tTente novamente...")
      
# ----- ONIBUS -----
def menuONIBUS():
  try:
    bus = Onibus(0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR ONIBUS"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Voltar ao Menu Principal \n=>  "))

      if opcao == 1:
        bus.criarOnibus()
        menuONIBUS()
      elif opcao == 2:
        bus.mostrarOnibus()
        op = int(input("\033[0;37m\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuONIBUS()
      elif opcao == 3:
        bus.mostrarOnibus()
        bus.editarOnibus()
        menuONIBUS()
      elif opcao == 4:
        bus.mostrarOnibus()
        bus.excluirOnibus()
        menuONIBUS()
      elif opcao == 5:
        exibir_menuPRINCIPAL()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")
    
# ----- PASSAGEM -----
def menuPASSAGEM():
  try:
    ticket = Passagem(0, 0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR PASSAGEM"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Voltar ao Menu Principal \n=>  "))

      if opcao == 1:
        ticket.cadastrarPassagem()
        menuPASSAGEM()
      elif opcao == 2:
        ticket.mostrarPassagem()
        op = int(input("\033[0;37m\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuPASSAGEM()
      elif opcao == 3:
        ticket.mostrarPassagem()
        ticket.editarPassagem()
        menuPASSAGEM()
      elif opcao == 4:
        ticket.mostrarPassagem()
        ticket.excluirPassagem()
        menuPASSAGEM()
      elif opcao == 5:
        exibir_menuPRINCIPAL()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")

# ----- MOTORISTA -----
def menuMOTORISTA():
  try:
    driver = Motorista(0, 0, 0, 0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR MOTORISTA"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Voltar ao Menu Principal \n=>  "))

      if opcao == 1:
        driver.cadastrarMotorista()
        menuMOTORISTA()
      elif opcao == 2:
        driver.mostrarMotorista()
        op = int(input("\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuMOTORISTA()
      elif opcao == 3:
        driver.mostrarMotorista()
        driver.editarMotorista()
        menuMOTORISTA()
      elif opcao == 4:
        driver.mostrarMotorista()
        driver.excluirMotorista()
        menuMOTORISTA()
      elif opcao == 5:
        exibir_menuPRINCIPAL()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")

# ----- VENDAS -----
def menuVENDAS():
  try:
    sell = Vendas(0, 0, 0, 0, 0, 0, 0)
    while True:
      tracejado(QTD_COLUNAS)
      print("{:^60}".format("GERENCIAR VENDAS"))
      tracejado(QTD_COLUNAS)

      opcao = int(input("\033[0;37m(1) Criar\n(2) Visualizar \n(3) Atualizar \n(4) Excluir \n(5) Voltar ao Menu Principal \n=>  "))

      if opcao == 1:
        sell.cadastrarVendas()
        menuVENDAS()
      elif opcao == 2:
        sell.mostrarVendas()
        op = int(input("\033[0;37m\n(1) Voltar para o Menu \n => "))
        if op == 1:
          menuVENDAS()
      elif opcao == 3:
        sell.mostrarVendas()
        sell.editarVendas()
        menuVENDAS()
      elif opcao == 4:
        sell.mostrarVendas()
        sell.excluirVendas()
        menuVENDAS()
      elif opcao == 5:
        exibir_menuPRINCIPAL()
      else:
        print("Opção não reconhecida, por favor informar um número das opções acima")
  except ValueError as e:
    print("Opção não reconhecida, por favor informar um número das opções acima", e)
  finally:
    if opcao == 99:
      print("\033[0;32m\n\taté mais :D\n")
    else:
      print("\033[0;31m\tTente novamente...")