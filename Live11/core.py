from datetime import datetime
from sqlalchemy import (create_engine, MetaData, Column,
                        Table, Integer, String, DateTime)

engine = create_engine('sqlite:///teste.db',
                       echo=False)

metadata = MetaData(bind=engine)
"""
ID.
Observe a maneira como marcamos esta coluna como a chave primária da tabela.
Mais sobre isso em um segundo.

NOME.
Vamos acelerar o indice nessa coluna.
"""

users_table = Table('usuarios', metadata,
                    Column('id', Integer, primary_key=True),
                    Column('nome', String(40), index=True),
                    Column('idade', Integer, nullable=False),
                    Column('senha', String),
                    Column('criado_em', DateTime(), default=datetime.now),
                    Column('atualizado_em',
                           DateTime(),
                           default=datetime.now,
                           onupdate=datetime.now))

metadata.create_all()
