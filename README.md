# Organizador
Organizador - programa para fins de avaliação - projeto 1 - do Curso de extensão da UFRGS (controle externo)

Programa executado com o python 3.10.6. Bibliotecas OS e shutils já instaladas por padrão nessa versão. Instalação do programa através do ambiente virtual (python -m venv projeto 1)


"""
PROGRAMA: organizador de arquivos xls e doc/docx em pasta para subpastas (para fins de avaliação - projeto 1 - do curso de extensão da UFRGS - controle externo).
REQUISITOS: Sua tarefa é organizar tais arquivos nas pastas planilhas e documentos de acordo com a extens˜ao do arquivo. Para executar sua tarefa, escreva um programa em Python que crie as pastas e mova os arquivos para as devidas pastas.
AUTOR:   Ítalo de Castro Rodrigues
DATA:   29/08/2022
VERSÃO: 1.0.0
"""


ATIVIDADE - Projeto Python 1:
PROFESSOR Nelson Seixas
2022

Voce tem dentro de uma pasta os seguintes arquivos:
• orcamento.xls
• orcamento.docx
• clientes.xls
• clientes.doc
• relatorio.doc

Sua tarefa ´e organizar tais arquivos nas pastas planilhas e documentos
de acordo com a extens˜ao do arquivo.
Para executar sua tarefa, escreva um programa em Python que crie as pastas
e mova os arquivos para as devidas pastas.
No GitHub, crie um reposit´orio denominado organizador e suba seu programa
para l´a.
Observa¸c˜oes:
1. N˜ao se esque¸ca de deixar seu reposit´orio p´ublico e de responder `a pergunta
”Qual o link de seu reposit´orio” no Moodle .
2. Use os pacotes OS e SHUTILS da biblioteca padr˜ao do Python para lhe
ajudar nesta tarefa.


CÓDIGO ABAIXO:





PROGRAMA: organizador de arquivos xls e doc/docx em pasta para subpastas.
REQUISITOS: Sua tarefa é organizar tais arquivos nas pastas planilhas e documentos
de acordo com a extens˜ao do arquivo. Para executar sua tarefa, escreva um programa em Python que crie as pastas e mova os arquivos para as devidas pastas.
AUTOR:   Ítalo de Castro Rodrigues
DATA:   29/08/2022
VERSÃO: 1.0.0
"""



"""

def main():
    import os
    import shutil

    pasta = os.listdir ('arquivos')

    if len(pasta) > 0:
        if os.path.isdir("arquivos/documentos") == False:
            os.mkdir("documentos")
            shutil.move("documentos", "arquivos")

        if os.path.isdir("arquivos/planilhas") == False:
            os.mkdir("planilhas")
            shutil.move("planilhas", "arquivos")
            
    for n in pasta:
        if n[-4:] == '.doc': 
            shutil.move (f"arquivos/{n}", "arquivos/documentos")

        elif n[-5:] == '.docx':
            shutil.move (f"arquivos/{n}", "arquivos/documentos")
                
        elif n[-4:] == '.xls':
            shutil.move(f"arquivos/{n}", "arquivos/planilhas")
            
    print ("terminei de organizar!")


if __name__ == "__main__":
    main()

#anotações diversas na busca da solução e teste de operações:
#n = pasta[0]
#print (n)
#print(type(n))
#print(n)
#print (n[-3:])
#print os.path.isdir("arquivos")
    















