from datetime import datetime, timedelta

pessoa ={
    'ano':'',
    'mes':'',
    'dia':'',
}

for chave in pessoa:
    pessoa[chave] = int(input('Digite o ' +chave))
    print(f"{chave}: {pessoa[chave]}")

print