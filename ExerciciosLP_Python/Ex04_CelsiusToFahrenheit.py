# Receba a temperatura em graus Celsius. Calcule e mostre a sua
# temperatura convertida em fahrenheit F = (9*C+160) /5.

print('Bem vindo a conversão de temperatura')

celsius = int(input("Digite o valor em celsius: "))
fahrenheit = int((celsius * 9) / 5 + 32)

print(str(celsius) + 'ºC => ' + str(fahrenheit) + 'ºF')
