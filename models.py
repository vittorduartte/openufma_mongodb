from mongoengine import *

class Curso(Document):
    codigo = StringField(required=True, primary_key=True)
    nome = StringField(required=True)
    modalidade = StringField(required=True)
    municipio = StringField()
    coordenador = StringField(required=True)

    meta = {"db_alias":"openufma", "collection":"cursos"}

class Subunidade(Document):
    codigo = StringField(required=True, primary_key=True)
    nome = StringField(required=True)

    meta = {"db_alias":"openufma", "collection":"subunidades"}

class Docente(Document):
    siape = StringField(required=True, primary_key=True)
    nome = StringField(required=True)
    departamento = StringField()
    descricao = StringField()
    formacao = StringField()
    interesse = StringField()
    lattes = StringField()
    email = StringField()
    telefone = StringField()
    img = StringField()
    subunidade =  ReferenceField(Subunidade, required=True)

    meta = {"db_alias":"openufma", "collection":"docentes"}

class Discente(Document):
    matricula = StringField(required=True, primary_key=True)
    nome = StringField(required=True)
    curso = StringField(required=True)
    id_curso = ReferenceField(Curso, required=True)

    meta = {"db_alias":"openufma", "collection":"discentes"}

class Monografia(Document):
    codigo = StringField(required=True, primary_key=True)
    titulo = StringField(required=True)
    ano = StringField(required=True)
    discente = StringField(required=True)
    orientador = StringField(required=True)
    id_curso = ReferenceField(Curso, required=True)

    meta = {"db_alias":"openufma", "collection":"monografias"}