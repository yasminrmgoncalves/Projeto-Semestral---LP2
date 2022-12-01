import db
import evento

MENU_INICIAL = 0

def main():
  evento.exibir_menuPRINCIPAL()

if __name__ == "__main__":
  db.criar_bdd()
  main()