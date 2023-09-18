name = str(input('Qual seu nome? '))
age = int(input('Qual sua idade? '))
weight = float(input('Qual seu peso? '))
height = float(input('Qual sua altura (EM METROS)? '))

imc = weight / (height * height)

print('Seu nome é {}, você tem {} anos, pesa {:.2f}KG e sua altura é de {:.2f} metros.'.format(
    name, age, weight, height))
print('Seu IMC é de {:.2f}'.format(imc))
