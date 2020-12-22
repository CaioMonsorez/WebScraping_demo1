import requests
from bs4 import BeautifulSoup

url = 'https://servicos.sjc.sp.gov.br/VagasPat/'

resposta = requests.get(url)
print(resposta.text)

#instanciar o bs4
#instalei com o pip lxml
soup = BeautifulSoup(resposta.text, 'lxml')


# o codigo abaixo lista o conteudo do html que esta em uma table-sm <td> e <tr> e etc...
lista_empregos = soup.find_all('table', class_= 'table-sm')
print(lista_empregos)

#o codigo abaixo lista o conteudo do html que esta em uma table-sm < td > 
for lista_td in lista_empregos:
    print(lista_td.find_all ('td'))


#o codigo abaixo lista o conteudo do html que esta em uma table-sm < th>
for lista_th in lista_empregos:
    print(lista_td.find_all('th'))
