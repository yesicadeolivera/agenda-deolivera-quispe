class Persona:

	def capitalizar(self, dato):
		cont=0
		palabra=""
		for letra in dato:
			if cont==0:
				palabra=palabra+letra.upper()
			elif letra==" ":
				cont=-1
				palabra=palabra+letra
			else:
				palabra=palabra+letra.lower()
				#print cont, letra
			cont+=1

		return palabra

