import os 
os.system

primeiro_numero = int(input("Digite o primeiro numero: "))
segundo_numero = int(input("Digite o segundo numero: "))
                     
soma =primeiro_numero + segundo_numero
produto = primeiro_numero * segundo_numero

maior = max (primeiro_numero, segundo_numero)
menor = min (primeiro_numero, segundo_numero)

print(f"soma: {soma}")
print(f"produto: {produto}")
print(f"Maior numero: {maior}")
print(f"Menor numero: {menor}")