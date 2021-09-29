import pandas as pd
from twilio.rest import Client

# logando no twilio
account_sid = "YOUR_SID"
auth_token  = "YOUR_TOKEN"
client = Client(account_sid, auth_token)

# abrir os arquivos em excel e analizar o que teve mais vendas e quantas vendas
list_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in list_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    # se tiver alguem com vendas acima de 55000 o programa manda um sms para o gerente
    if (tabela_vendas['Vendas'] > 55000).any(): # any() fala que é para verificar algum valor dentro da coluna
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        menssagem = str(f'No mes de {mes} o vendedor {vendedor} bateu a meta com R${vendas} em vendas!')
        # enviar a mensagem pelo zap
        message = client.messages.create(
            to="+55018991065626",
            from_="+12408234870",
            body=menssagem)

