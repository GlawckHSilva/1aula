nome = input ("Qual o seu nome?")
sobrenome = input ("Qual o seu sobrenome?")
idade =int(input("Qual a sua idade?"))
altura = float(input ("Qual a sua altura?"))
peso = float(input (" Qual o seu peso"))


maior_idade = idade >= 18 


print( "\nRersultado:")
print("nome:", nome)
print("sobrenome:", sobrenome)
print ("idade:", idade)
print("altura", altura, "cm")
print("peso", peso, "kg")
print("Maior de idade:", "Sim" if maior_idade else "Não")