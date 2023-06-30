import os
from config.definitions import ROOT_DIR

def abrirArchivo(path, flags):
    return open(path,flags)
    

def main():
    openedFile = abrirArchivo(os.path.join(ROOT_DIR,'Files', 'test.txt'),'r')
    print (openedFile.read())
    

if __name__ == "__main__":
    main()