from ufma_scrapper import curso as course
from models import Curso, Discente

def saveCoursesAndStudents():  

    cursos = course.get_cursos()

    for curso in cursos:
       
        curso = Curso(codigo=curso["codigo"], 
                      nome=curso["nome"], 
                      modalidade=curso["modalidade"], 
                      municipio=curso["municipio"], 
                      coordenador=curso["coordenador"]
                     )
        try:
            curso.save()
        except Exception as error:
            print("Erro ao persistir os dados de curso: ", error)

        discentes = course.get_discentes_ativos(curso.id)["data"]

        for disc in discentes:

            discente = Discente(matricula=disc["matricula"],
                                nome=disc["nome"],
                                curso=disc["nome_curso"],
                                id_curso=disc["codigo_curso"]
                               )

            try:
                discente.save()
            except Exception as error:
                print("Erro ao persistir os dados de discentes: ", error)
                
