
sair = "sair"

numero1 = input("Digite o primeiro número")
numero2 = input("Digite o segundo número")
operador = input("Digite o operador (+-/*)")

numero1_float = 0
numero2_float = 0 

numero1_float = float(numero1)
numero2_float = float(numero2)

if operador == "+":
 print(f"(numero1_float) + (numero2_float) =", numero2_float + numero1_float)

if operador == "-":
 print(f"(numero1_float) - (numero2_float) =", numero2_float - numero1_float)

if operador == "*":
 print(f"(numero1_float) * (numero2_float) =", numero2_float * numero1_float)

if operador == "/":
 print(f"(numero1_float) / (numero2_float) =", numero2_float / numero1_float)