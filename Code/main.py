import os
from config.definitions import ROOT_DIR

def abrirArchivo(path, flags):
    return open(path,flags)

#abrir en modo leer: 'r'
def leerArchivo(archivo):
    f = abrirArchivo(archivo, 'r')
    print(f.read())
    f.close()

#abrir en modo append: 'a'   
def modificarArchivo(archivo, modificacion):
    f = abrirArchivo(archivo,'a')
    f.write(modificacion)
    f.close() 

def main():
    rutaArchivo = os.path.join(ROOT_DIR,'Files', 'test.txt')
    leerArchivo(rutaArchivo)
    modificarArchivo(rutaArchivo,"\nmodificacion de prueba xd")
    leerArchivo(rutaArchivo)
    
    

if __name__ == "__main__":
    main()