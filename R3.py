import os
def mostrar_directorio():
	directorio=(os.getcwd())	
	return directorio
def cambiar_directorio():
	ruta='/tmp'
	os.chdir(ruta)	
	
def crear_directorio():
	ruta='/home/usuario/'
	os.chdir(ruta)
	os.mkdir('practica')
	
def listar_directorio():
	ruta='/home/usuario/practica'
	lista=(os.listdir(ruta))
	print (lista)

def main(args):
	nuevacarpeta=crear_directorio()
	lista=listar_directorio()
	nuevodirectorio=cambiar_directorio()
	directorio=mostrar_directorio()
	print (directorio)

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
