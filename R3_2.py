#!/usr/bin/env python
import os
def crear_archivo():
	ruta='/home/usuario/practica'
	os.chdir(ruta)
	try:
		with open("prueba.txt", "x") as prueba:
			prueba.write("Este archivo es de prueba.\n")
	except FileExistsError:
		print("El archivo ya existe.")
	return 0

def cambiar_nombre():
	ruta='/home/usuario/practica'
	os.chdir(ruta)
	os.renames('prueba.txt','log_de_sistema.log')
	return 0
	
def eliminar_archivo():
	ruta='/home/usuario/practica/log_de_sistema.log'
	try:
		os.remove(ruta)
	except OSError as e:
		print(f'Error: {ruta} : {e.strerror}')
	return 0

def main(args):
	nuevoarchivo=crear_archivo()
	nuevonombre=cambiar_nombre()
	eliminar=eliminar_archivo()
	return 0

if __name__ == '__main__':
	import sys
	sys.exit(main(sys.argv))

