"""
PROGRAMA: organizador de arquivos xls e doc/docx em pasta para subpastas.
REQUISITOS: Sua tarefa é organizar tais arquivos nas pastas planilhas e documentos
de acordo com a extens˜ao do arquivo. Para executar sua tarefa, escreva um programa em Python que crie as pastas e mova os arquivos para as devidas pastas.
AUTOR:   Ítalo de Castro Rodrigues
DATA:   29/08/2022
VERSÃO: 1.0.0
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
    
