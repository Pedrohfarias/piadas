from random import randint, random

from piadas import PIADAS_PERGUNTA_RESPOSTA


def piadas_perguntas_respostas():
    numero_aleatorio = randint(0,len(PIADAS_PERGUNTA_RESPOSTA)-1)
    piada = PIADAS_PERGUNTA_RESPOSTA[numero_aleatorio]
    return {"piada":piada}

