from bs4 import BeautifulSoup
import requests

site = requests.get("https://www.climatempo.com.br/").content
# Objeto site recebendo o conteudo da requisicao http do site

soup = BeautifulSoup(site, 'html.parser')
# Objeto soup baixando o html do site

print(soup.prettify)
# Prettify transforma a estrutura HTML em string.


# DESAFIO: OBTER APENAS A TEMPERATURA DE HOJE:

# ######### Quero apenas um trecho do HTML - Para isso usaremos os finds

print("\n#################### Área dos Finds ####################")

# Achando todos os elementos HTML que possuem a seguinte característica: <img alt="Temperatura máxima Hoje" class="_margin-l-10 _margin-r-5" height="12" src="/dist/images/v2/svg/ic-arrow-max.svg" width="12"/>
print("Achando todos os elementos HTML que possuam algo em comum:")
temperaturas_maximas_all = soup.find_all("img", class_="_margin-l-10 _margin-r-5", attrs={"height":"12", "src":"/dist/images/v2/svg/ic-arrow-max.svg", "width":"12"})
print(temperaturas_maximas_all)

# Achando O PRIMEIRO ELEMENTO HTML que possui a seguinte característica: <img alt="Temperatura máxima Hoje" class="_margin-l-10 _margin-r-5" height="12" src="/dist/images/v2/svg/ic-arrow-max.svg" width="12"/>
print("Achando APENAS O PRIMEIRO ELEMENTO HTML que possua algo em comum:")
temperaturas_maximas_one = soup.find("img", class_="_margin-l-10 _margin-r-5", attrs={"height":"12", "src":"/dist/images/v2/svg/ic-arrow-max.svg", "width":"12"})
print(temperaturas_maximas_one)

# Achando esse trecho do HTML -> <span class="city _margin-r-5 -font-13">-</span> :
print("Encontrando um elemento html simples:")
temperatura_span = soup.find("span", class_="city _margin-r-5 -font-13")
print(temperatura_span.string)

# Encontrar apenas a temperatura máxima de HOJE:
print("Encontrando o trecho de apenas a temperatura máxima de Hoje:")
temperatura_maxima_hoje = soup.find("img", class_="_margin-l-10 _margin-r-5", attrs={"alt":"Temperatura máxima Hoje"})
print(temperatura_maxima_hoje)
"""Contudo observe que isso nao nos dá a temperatura de hoje. Isso acontece porque o valor da temperatura NÃO ESTÁ DENTRO DA TAG IMG. Observe abaixo:
        <p class="-gray _flex _align-center">
        <img alt="Temperatura mínima Hoje" class="_margin-r-5" height="12" src="/dist/images/v2/svg/ic-arrow-min.svg" width="12"/>
        20°
        <img alt="Temperatura máxima Hoje" class="_margin-l-10 _margin-r-5" height="12" src="/dist/images/v2/svg/ic-arrow-max.svg" width="12"/>
        27°
        </p>
Logo, como o valor de 27° NÃO ESTÁ DENTRO DE IMG, vamos usar o elemento .next_sibling, que é O PRIMEIRO ELEMENTO IMEDIATAMENTE APÓS A OCORRÊNCIA DO FIND (após a linha do <img> temos exatamente 27°C). Logo:
"""
print("Encontrando APENAS O VALOR DA TEMPERATURA MÁXIMA DE HOJE:")
temperatura_maxima_hoje_valor_string = soup.find("img", class_="_margin-l-10 _margin-r-5", attrs={"alt":"Temperatura máxima Hoje"}).next_sibling
# print(temperatura_maxima_hoje_valor_string)

# #####Arrumando para termos apenas o valor da temperatura (no exemplo acima, seria apenas 27°)
temperatura_maxima_hoje_valor_ok = temperatura_maxima_hoje_valor_string.replace('\n', '')
print(temperatura_maxima_hoje_valor_ok)
