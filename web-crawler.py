"""Este script vai elencar as palavras mais repetidas (e o número de vezes em que se repetem) de um determinado site (geeksforgeeks) e printar o top 10 ao final."""

import requests
from bs4 import BeautifulSoup
import operator
from collections import Counter


# Funcao remover todos os caracteres especiais
def clean_wordlist(wordlist):
    clean_list = []
    for word in wordlist:
        symbols = '!@#$#%^&*()_-+={[}]|\;:"<>?/.,  '

        for i in range(0, len(symbols)):
            word = word.replace(symbols[i], '')

        if len(word) > 0:
            clean_list.append(word)
    create_dictionary(clean_list)


def create_dictionary(clean_list):
    word_count = {}

    for word in clean_list:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for key, value in sorted(word_count.items(),
                            key = operator.itemgetter(1)):
        print("% s : % s " % (key, value))

    c = Counter(word_count)
    top = c.most_common(10)
    print(top)


def start(url):
    wordlist = []
    source_code = requests.get(url).text
    soup = BeautifulSoup(source_code, 'html.parser')

# Procurando todos os texts das Divs cujas classes são "entry-content":
    for each_text in soup.findAll('div', {'class': 'entry-content'}):
        content = each_text.text
        # Separa cada caso usando split além do lower para deixar em letra minúscula:
        words = content.lower().split()
        # Salva essas words no wordlist
        for each_word in words:
            wordlist.append(each_word)
        clean_wordlist(wordlist)  # Limpa todos os caracteres especiais da wordlist


if __name__ == '__main__':
    start("https://geeksforgeeks.org/python-programming-language/?ref=leftbar")
