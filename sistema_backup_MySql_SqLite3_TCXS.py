#!/usr/bin/env python
# -*- coding: utf-8 -*-
# ███╗   ███╗ █████╗ ███╗   ██╗██╗ ██████╗ ██████╗ ███╗   ███╗██╗ ██████╗
# ████╗ ████║██╔══██╗████╗  ██║██║██╔════╝██╔═══██╗████╗ ████║██║██╔═══██╗
# ██╔████╔██║███████║██╔██╗ ██║██║██║     ██║   ██║██╔████╔██║██║██║   ██║
# ██║╚██╔╝██║██╔══██║██║╚██╗██║██║██║     ██║   ██║██║╚██╔╝██║██║██║   ██║
# ██║ ╚═╝ ██║██║  ██║██║ ╚████║██║╚██████╗╚██████╔╝██║ ╚═╝ ██║██║╚██████╔╝
# ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝ ╚═════╝ ╚═════╝ ╚═╝     ╚═╝╚═╝ ╚═════╝
#            @GorpoOrko | Manicomio TCXS Project | 2020
import pymysql.cursors
import sqlite3
from datetime import datetime

#CONEXAO MYSQL
conexao_mysql = pymysql.connect(host ='localhost', user='root', password='', db='tcxs_store', charset='utf8mb4', cursorclass= pymysql.cursors.DictCursor)
cursor_mysql = conexao_mysql.cursor()
#CONEXAO SQLITE
conexao_sqlite = sqlite3.connect('dump_MYSQL.db')
cursor_sqlite = conexao_sqlite.cursor()


print('iniciou')
cursor_mysql.execute(f"SELECT * FROM playstation_users")
cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_users` ( id integer not null primary key autoincrement, `usuario` varchar(200) NOT NULL, `senha` varchar(329) NOT NULL, `nome` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `nivel` varchar(999)) """)
conexao_sqlite.commit()
tabela_users = cursor_mysql.fetchall()
conexao_mysql.commit()
for dados_user in tabela_users:
    try:
        usuario = dados_user['usuario']
        senha = dados_user['senha']
        nome = dados_user['nome']
        cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
        nivel = dados_user['nivel']
        cursor_sqlite.execute(f"""INSERT INTO playstation_users ( `usuario`, `senha`, `nome`, `cadastro`,`nivel`) VALUES ('{usuario}','{senha}','{nome}','{cadastro}','{nivel}')""")
        conexao_sqlite.commit()
        #print(dados_user)
    except Exception as e:
        print(f'erro ps users: {e}')
        pass

cursor_mysql.execute(f"SELECT * FROM playstation_infos")
cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_infos` ( id integer not null primary key autoincrement, `informacao` varchar(999) NOT NULL) """)
conexao_sqlite.commit()
tabela_infos = cursor_mysql.fetchall()
conexao_mysql.commit()
for dados_info in tabela_infos:
    try:
        info = dados_info['informacao']
        cursor_sqlite.execute(f"""INSERT INTO playstation_infos (`informacao`) VALUES ('{info}')""")
        conexao_sqlite.commit()
        #print(dados_info)
    except Exception as e:
        print(f'erro ps infos: {e}')
        pass


cursor_mysql.execute(f"SELECT * FROM playstation_psp")
cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_psp` ( id integer not null primary key autoincrement,
 `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
conexao_sqlite.commit()
tabela_psp = cursor_mysql.fetchall()
conexao_mysql.commit()
for dados_user in tabela_psp:
    try:
        titulo = dados_user['titulo']
        descricao = dados_user['descricao']
        content_id = dados_user['content_id']
        imagem = dados_user['imagem']
        cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
        link = dados_user['link']
        cursor_sqlite.execute(f"""INSERT INTO playstation_psp (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
        conexao_sqlite.commit()
        #print(dados_user)
    except Exception as e:
        print(f'erro ps psp: {e}')
        pass


cursor_mysql.execute(f"SELECT * FROM playstation_ps1")
cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_ps1` ( id integer not null primary key autoincrement,
 `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
conexao_sqlite.commit()
tabela_ps1 = cursor_mysql.fetchall()
conexao_mysql.commit()
for dados_user in tabela_ps1:
    try:
        titulo = dados_user['titulo']
        descricao = dados_user['descricao']
        content_id = dados_user['content_id']
        imagem = dados_user['imagem']
        cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
        link = dados_user['link']
        cursor_sqlite.execute(f"""INSERT INTO playstation_ps1 (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
        conexao_sqlite.commit()
        #print(dados_user)
    except Exception as e:
        print(f'erro ps ps1: {e}')
        pass

cursor_mysql.execute(f"SELECT * FROM playstation_ps2")
cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_ps2` ( id integer not null primary key autoincrement,
 `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
conexao_sqlite.commit()
tabela_ps2 = cursor_mysql.fetchall()
conexao_mysql.commit()
for dados_user in tabela_ps2:
    try:
        titulo = dados_user['titulo']
        descricao = dados_user['descricao']
        content_id = dados_user['content_id']
        imagem = dados_user['imagem']
        cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
        link = dados_user['link']
        cursor_sqlite.execute(f"""INSERT INTO playstation_ps2 (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
        conexao_sqlite.commit()
        #print(dados_user)
    except Exception as e:
        print(f'erro ps ps2: {e}')
        pass

cursor_mysql.execute(f"SELECT * FROM playstation_emuladores")
cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_emuladores` ( id integer not null primary key autoincrement,
 `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
conexao_sqlite.commit()
tabela_emuladores = cursor_mysql.fetchall()
conexao_mysql.commit()
for dados_user in tabela_emuladores:
    try:
        titulo = dados_user['titulo']
        descricao = dados_user['descricao']
        content_id = dados_user['content_id']
        imagem = dados_user['imagem']
        cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
        link = dados_user['link']
        cursor_sqlite.execute(f"""INSERT INTO playstation_emuladores (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
        conexao_sqlite.commit()
        #print(dados_user)
    except Exception as e:
        print(f'erro ps users: {e}')
        pass

cursor_mysql.execute(f"SELECT * FROM playstation_extras")
cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_extras` ( id integer not null primary key autoincrement,
 `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,`imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL, `link` varchar(999) NOT NULL) """)
conexao_sqlite.commit()
tabela_extras = cursor_mysql.fetchall()
conexao_mysql.commit()
for dados_user in tabela_extras:
    try:
        titulo = dados_user['titulo']
        descricao = dados_user['descricao']
        content_id = dados_user['content_id']
        imagem = dados_user['imagem']
        cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
        link = dados_user['link']
        cursor_sqlite.execute(f"""INSERT INTO playstation_extras (titulo, descricao, content_id, imagem, cadastro, link) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}','{link}')""")
        conexao_sqlite.commit()
        #print(dados_user)
    except Exception as e:
        print(f'erro ps users: {e}')



cursor_mysql.execute(f"SELECT * FROM playstation_ps3")
cursor_sqlite.execute("""CREATE TABLE IF NOT EXISTS `playstation_ps3` ( id integer not null primary key autoincrement,
 `titulo` varchar(999) NOT NULL, `descricao` varchar(999) NOT NULL, `content_id` varchar(999) NOT NULL,
 `imagem` varchar(999) NOT NULL, `cadastro` datetime NOT NULL,
  `link1` varchar(999) NOT NULL,`link2` varchar(999) NOT NULL,`link3` varchar(999) NOT NULL,`link4` varchar(999) NOT NULL,
  `link5` varchar(999) NOT NULL,`link6` varchar(999) NOT NULL,`link7` varchar(999) NOT NULL,`link8` varchar(999) NOT NULL,
  `link9` varchar(999) NOT NULL,`link10` varchar(999) NOT NULL,`link11` varchar(999) NOT NULL,`link12` varchar(999) NOT NULL,
  `link13` varchar(999) NOT NULL,`link14` varchar(999) NOT NULL,`link15` varchar(999) NOT NULL,`link16` varchar(999) NOT NULL,
  `link17` varchar(999) NOT NULL,`link18` varchar(999) NOT NULL,`link19` varchar(999) NOT NULL,`link20` varchar(999) NOT NULL,
  `link21` varchar(999) NOT NULL,`link22` varchar(999) NOT NULL,`link23` varchar(999) NOT NULL,`link24` varchar(999) NOT NULL,
  `link25` varchar(999) NOT NULL,`link26` varchar(999) NOT NULL,`link27` varchar(999) NOT NULL,`link28` varchar(999) NOT NULL,
  `link29` varchar(999) NOT NULL,`link30` varchar(999) NOT NULL) """)

conexao_sqlite.commit()
tabela_ps3 = cursor_mysql.fetchall()
conexao_mysql.commit()
for dados_user in tabela_ps3:
    try:
        titulo = dados_user['titulo']
        descricao = dados_user['descricao']
        content_id = dados_user['content_id']
        imagem = dados_user['imagem']
        cadastro = datetime.fromisoformat(str(dados_user['cadastro']))
        link1 = dados_user['link1']
        link2 = dados_user['link2']
        link3 = dados_user['link3']
        link4 = dados_user['link4']
        link5 = dados_user['link5']
        link6 = dados_user['link6']
        link7 = dados_user['link7']
        link8 = dados_user['link8']
        link9 = dados_user['link9']
        link10 = dados_user['link10']
        link11 = dados_user['link11']
        link12 = dados_user['link12']
        link13 = dados_user['link13']
        link14 = dados_user['link14']
        link15 = dados_user['link15']
        link16 = dados_user['link16']
        link17 = dados_user['link17']
        link18 = dados_user['link18']
        link19 = dados_user['link19']
        link20 = dados_user['link20']
        link21 = dados_user['link21']
        link22 = dados_user['link22']
        link23 = dados_user['link23']
        link24 = dados_user['link24']
        link25 = dados_user['link25']
        link26 = dados_user['link26']
        link27 = dados_user['link27']
        link28 = dados_user['link28']
        link29 = dados_user['link29']
        link30 = dados_user['link30']

        cursor_sqlite.execute(f"""INSERT INTO playstation_ps3 (titulo, descricao, content_id, imagem, cadastro,
link1,link2,link3,link4,link5,link6,link7,link8,link9,link10,link11,link12,link13,link14,link15,
link16,link17,link18,link19,link20,link21,link22,link23,link24,link25,link26,link27,link28,link29,link30) VALUES ('{titulo}','{descricao}','{content_id}','{imagem}','{cadastro}',
'{link1}','{link2}','{link3}','{link4}','{link5}','{link6}','{link7}','{link8}','{link9}','{link10}','{link11}','{link12}','{link13}',
'{link14}','{link15}','{link16}','{link17}','{link18}','{link19}','{link20}','{link21}','{link22}','{link23}','{link24}','{link25}',
'{link26}','{link27}','{link28}','{link29}','{link30}')""")
        conexao_sqlite.commit()
        #print(dados_user)
    except Exception as e:
        print(f'erro ps ps3: {e}')
        pass

print('acabou a operaçao')