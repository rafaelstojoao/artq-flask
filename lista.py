#list all files in a path
#by Rafael S. João
from fnmatch import fnmatch
import os

caminho = '.'
tipo = "*.dcm"

for pasta, subpasta, arqs in os.walk(caminho):
    for nomeArq in arqs:
        if fnmatch(nomeArq, tipo): # busca todos os arquivos do tipo tipo
            print (os.path.join(pasta, nomeArq))
