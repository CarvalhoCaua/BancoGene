from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base

dbGB = create_engine("sqlite:///BancoGene.db")

Sessao = sessionmaker(bind=dbGB)
sessao = Sessao()

Base = declarative_base()


class Gene(Base):
    __tablename__ = "genes"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String)
    simbolo = Column("simbolo", String)

    def __init__(self, nome, simbolo):
        self.nome = nome
        self.simbolo = simbolo


class Ontologia(Base):
    __tablename__ = "ontologias"

    id = Column("id", Integer, primary_key=True, autoincrement=True)
    funcao = Column("funcao", ForeignKey("genes.id"))
    local = Column("local", String)

    def __init__(self, funcao, local):
        self.funcao = funcao
        self.local = local


Base.metadata.create_all(bind=dbGB)


# Gene
gene = Gene(nome="Granulin", simbolo="GRN")
sessao.add(gene)
sessao.commit()

# Ontologia
ontologia = Ontologia(funcao="Sexual", local="Cromossomo Y")
sessao.add(ontologia)
sessao.commit()

