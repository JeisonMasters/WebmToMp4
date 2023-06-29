import os
from config.definitions import ROOT_DIR

def abrirArchivo(file):
    f = open(file)
    return f

def main():
    openedFile = abrirArchivo(os.path.join(ROOT_DIR,'Files','test.txt'))
    print ("Nombre de archivo: ",openedFile.name)

if __name__ == "__main__":
    main()