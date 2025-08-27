import os
os.system("cls")

numero1 = float(input("Digite o primeiro numero: "))
numero2 = float(input("DIGITE SEGUNDO NUMERO"))

media = (numero1 + numero2) /2

if media >= 7:
    resultado = "APROVADO"

else:
    resultado = "REPROVADO"

print("\n")
print(f"media: {media}")

print(f"resultado: {resultado}")

