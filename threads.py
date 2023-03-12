from threading import Thread
import time


def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 10:
        trajeto+=velocidade
        time.sleep(0.5)
        print(f"\tPiloto: {piloto}.\n\tKm: {trajeto}\n")

t_carro1 = Thread(target = carro, args=[1, "Bruno"])
t_carro2 = Thread(target = carro, args=[1.5, "Python"])

t_carro1.start()
t_carro2.start()
