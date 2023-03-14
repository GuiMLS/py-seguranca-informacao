import random
import string

tamanho = int(input("Digite quantos caracteres terá a senha a ser gerada: "))

chars = string.ascii_letters + string.digits + '!çÇ@#%$&*()-=+,.;:/?'

rnd = random.SystemRandom() # os.urandom
print("Sua senha gerada é:")
print(''.join(rnd.choice(chars) for i in range(tamanho)))