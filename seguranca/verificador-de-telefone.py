"""Este script irá verificar telefones"""

import phonenumbers


from phonenumbers import geocoder  # geocoder tira a localização do telefone com base no número (Ex: 11 = São Paulo, 98 = Maranhão, 48 = Santa Catarina, etc)


phone = input("Digite o telefone no formato +551140028922: ")
phone_number = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))

