import sqlite3

conn = sqlite3.connect("bdd.db")

def criar_bdd():
  conn.execute("""
  create table if not exists onibus(
    placa text primary key,
    assentos integer
  )
  """)
  
  conn.execute("""
  create table if not exists passagem(
    id_passagem integer primary key AUTOINCREMENT,
    destino text,
    preco float
  )
  """)
  
  conn.execute("""
  create table if not exists motorista(
    cpf int primary key,
    nome text,
    data_nasc date,
    endereco text,
    salario float
  )
  """)

  conn.execute("""
  create table if not exists vendas(
    id integer primary key AUTOINCREMENT,
    nome text,
    cpf integer,
    data_nasc date,
    destino text,
    assento_escolhido integer,
    forma_pagamento text
  )
  """)
  
# --- ONIBUS (CRUD) ---
def add_onibus(placa, assentos):
  conn.execute("insert into onibus (placa, assentos) values (?, ?)", (placa, assentos))
  conn.commit()

def get_onibus():
  return conn.execute("select * from onibus")

def update_onibus(upd_placa, upd_assento, placa):
  conn.execute("update onibus set placa = ?, assentos = ? where placa = ?", (upd_placa, upd_assento, placa))
  conn.commit()

def remove_onibus(placa):
  conn.execute("delete from onibus where placa = ?", (placa, ))
  conn.commit()

# --- PASSAGEM (CRUD) ---
def add_passagem(destino, preco):
  conn.execute("insert into passagem (destino, preco) values (?, ?)", (destino, preco))
  conn.commit()

def get_passagem():
  return conn.execute("select * from passagem")

def update_passagem(upd_destino, upd_preco, id):
  conn.execute("update passagem set destino = ?, preco = ? where id_passagem = ?", (upd_destino, upd_preco, id))
  conn.commit()

def remove_passagem(id):
  conn.execute("delete from passagem where id_passagem = ?", (id, ))
  conn.commit()

# --- MOTORISTA (CRUD) ---
def add_motorista(novo_motorista, cpf, data_nasc, endereco, salario):
  conn.execute("insert into motorista (nome, cpf, data_nasc, endereco, salario) values (?, ?, ?, ?, ?)", (novo_motorista, cpf, data_nasc, endereco, salario))
  conn.commit()

def get_motorista():
  return conn.execute("select * from motorista")

def update_motorista(upd_motorista, upd_cpf, upd_data_nasc, upd_endereco, upd_salario, cpf):
  conn.execute("update motorista set nome = ?, cpf = ?, data_nasc = ?, endereco = ?, salario = ? where cpf = ?", (upd_motorista, upd_cpf, upd_data_nasc, upd_endereco, upd_salario, cpf))
  conn.commit()

def remove_motorista(cpf):
  conn.execute("delete from motorista where cpf = ?", (cpf, ))
  conn.commit()
  
# --- VENDAS (CRUD) ---
def add_vendas(nome, cpf, data_nasc, destino, assento_escolhido, forma_pagamento):
  conn.execute("insert into vendas (nome, cpf, data_nasc, destino, assento_escolhido, forma_pagamento) values (?, ?, ?, ?, ?, ?)", (nome, cpf, data_nasc, destino, assento_escolhido, forma_pagamento))
  conn.commit()

def get_vendas():
  return conn.execute("select * from vendas")

def update_vendas(upd_nome, upd_cpf, upd_data_nasc, upd_destino, upd_assento_escolhido, upd_forma_pagamento, id):
  conn.execute("update vendas set nome = ?, cpf = ?, data_nasc = ?, destino= ?, assento_escolhido = ?, forma_pagamento = ? where id = ?", (upd_nome, upd_cpf, upd_data_nasc, upd_destino, upd_assento_escolhido, upd_forma_pagamento, id))
  conn.commit()

def remove_vendas(id):
  conn.execute("delete from vendas where id = ?", (id, ))
  conn.commit()