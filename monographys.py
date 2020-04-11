from ufma_scrapper import curso as course
from models import Monografia

def saveMonographys():
    
    cursos = course.get_cursos()

    for ano in range(2014, 2018):
        id_mono = 1
        
        for curso in cursos:
            
            monografias = course.get_monografias(curso["codigo"], str(ano))["data"]
            
            for monografia in monografias:
                
                mono = Monografia(codigo=curso["codigo"]+"_"+str(ano)+"_"+str(id_mono),
                                titulo=monografia["titulo"],
                                ano=str(ano),
                                discente=monografia["discente"],
                                orientador=monografia["orientador"],
                                id_curso=curso["codigo"]
                                )
                try:
                    mono.save()
                except Exception as error:
                    print("Erro ao persistir os dados de discentes: ", error)
                
                id_mono+=1
