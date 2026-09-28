print('Digite seu nome')
nome = input()
print('Seja bem-vindo', nome, '!')
print('Digiteseu peso (Kg):')
Peso = float(input())
print('Digite sua altura (m):')
Altura = float(input())
IMC = Peso / (Altura ** 2)
print('Seu IMC é:', IMC)
if IMC < 18.5:
    print('Abaixo do peso')
elif IMC < 24.9:
    print('Peso Ideal')
elif IMC < 29.9:
    print('Sobrepeso')
elif IMC < 34.9:
    print('Obesidade I')
elif IMC < 39.9:
    print('Obesidade II (Severa)')
else:
    print('Obseidade III (Morbida)')