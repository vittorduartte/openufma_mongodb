from ufma_scrapper import subunidade as subunity
from models import Subunidade, Docente

def saveSubunitysAndTeachers():

    subunidades = subunity.get_subunidades()

    for subunidade in subunidades:

        subunidade = Subunidade(codigo=subunidade["codigo"],
                                nome=subunidade["nome"]
                                )
        try:
            subunidade.save()
        except Exception as error:
            print("Erro ao persistir os dados de subunidade: ", error)

        docentes = subunity.get_docentes(subunidade.id)

        for docente in docentes:

            docente = Docente(siape=docente["siape"], 
                              nome=docente["nome"], 
                              subunidade=docente["codigo_subunidade"]
                             )
            try:
                docente.save()
            except Exception as error:
                print("Erro ao persistir os dados de docente: ", error)