from conexionBD import ConexionBD
from persona import Persona
import os
import datetime
def Menu():
	columnas=['nombre','apellido','telefono','email','fecha_nacimiento']

	c=ConexionBD()
	c.crear_tabla()
	p=Persona()
	continuar = "s"
	while continuar == "s":
		print (".:: MENU ::.")
		print ("1_Ingresar datos \n2_Actualizar mis datos\n3_Borrar datos \n4_Imprimir registro \n5_Imprimir cantidad de registros")
		op=int(raw_input ("Opcion: "))
		 
		if op ==  1 : 
			print (".:: INGRESAR DATOS ::.")
			nombre1 = raw_input("Ingrese nombre: ")
			nombre1=p.capitalizar(nombre1)
			
			apellido1 = raw_input("Ingrese apellido: ")
			apellido1=p.capitalizar(apellido1)

			telefono = raw_input("Ingrese telefono: ")
			email = raw_input("Ingrese email: ")
			print("Ingrese fecha de nacimiento de forma numerica")
			d = raw_input("Ingrese dia: ")
			m = raw_input("Ingrese mes: ")
			y = raw_input("Ingrese anio: ")

			
			c.insertar(nombre1, apellido1,telefono, email,y,m,d)
			c.select_all()

		elif op == 2:
			print (".:: ACTUALIZAR DATOS ::.")
			print(".:: IMPRIMIR UN REGISTRO	::.")
			dato=raw_input("Ingrese apellido (buscador): ")
			dato2=raw_input("Ingrese email como identificador:")
			c.buscar(dato,dato2)
			
			for x in columnas:
				col=x
				res = raw_input("Editar " + x + "? s/n: ")
				if res == 's':
					
					nuevo_dato=raw_input("Nuevo " + x + ": ")
					if x == 'apellido':
						dato=nuevo_dato
					#print col, nuevo_dato, e_mail
					c.actualizar_datos(col,nuevo_dato,dato2)
			c.buscar(dato,dato2)
		elif op==3:
			print (".:: BORRAR DATOS :: .")
			print(".:: IMPRIMIR UN REGISTRO	::.")
			dato=raw_input("Ingrese apellido (buscador): ")
			dato2=raw_input("Ingrese email como identificador:")
			c.buscar(dato,dato2)
			c.eliminar_datos(dato2)
			print("Se eliminaron los datos")

		elif op==4:
			print(".:: IMPRIMIR UN REGISTRO	::.")
			dato=raw_input("Ingrese apellido (buscador): ")
			dato2=raw_input("Ingrese email como identificador:")
			c.buscar(dato,dato2)
		elif op == 5:
			print(".:: IMPRIMIR CANTIDAD DE REGISTROS ::.")
			cant=c.cantidad_registros()
			print cant
		else:
			print ("Opcion inexistente")
		continuar=raw_input("Desea continuar? s/n ")
		os.system('cls')
	if continuar=="n":
		print "-----------Exit-----------"



