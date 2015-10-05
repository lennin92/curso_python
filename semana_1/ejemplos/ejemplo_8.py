def contar_as(cadena):
	cnt = 0
	for char in cadena:
		if char=='a':
			cnt+=1
	return cnt

TEXTO = """
ALGORITMO "BACKPROPAGATION".
 
Cuando necesitamos representar problemas complejos, no nos basta únicamente con un simple perceptrón, sino que necesitamos una red de perceptrones interconectados entre ellos.
 
Para el entrenamiento de una red hemos de tener en cuenta que la salida de cada neurona no va a depender únicamente de las entradas del problema, sino que también depende de las salidas que ofrezcan el resto de las neuronas. Por este mismo motivo también podemos afirmar que el error cometido por una neurona no solo va a depender de que sus pesos sean los correctos o no, sino que dependerá del error que traiga acumulado del resto de neuronas que le precedan en la red.
"""
print(TEXTO)
print("\n\nEn el texto hay %d cantidad de 'a's\n\n"%(contar_as(TEXTO)))

print("\n\t==============================================================\n")
TEXTO="La luna esta rojA"
print(TEXTO)
print("\n\nEn el texto hay %d cantidad de 'a's\n\n"%(contar_as(TEXTO)))
