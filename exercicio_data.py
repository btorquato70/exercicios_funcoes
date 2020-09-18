#Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string \n
#no formato D de mesPorExtenso de AAAA.Opcionalmente, valide a data e retorne NULL caso a data seja inválida.

def receber_data():
    data = str(input('Digite uma data no formato DD/MM/AAAA: '))
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    mes_ext = ['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']

    conversao = mes_ext[mes-1]
    return f'{dia} de {conversao} de {ano}'

print(receber_data())




