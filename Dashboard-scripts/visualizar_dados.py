import matplotlib.pyplot as plt
import csv
import time

temperaturas = []
humidades = []
timestamps = []

with open("sensor_data.csv", "r") as variavel:

    leitor = csv.reader(variavel)

    for linha in leitor:
        if len(linha) == 3:
            temperaturas.append(float(linha[0]))
            humidades.append(float(linha[1]))
            timestamps.append(linha[2])

fig, eixos = plt.subplots(3, 1, figsize=(12, 5))

eixos[0].plot(range(len(temperaturas)), temperaturas, label= "Temperatura (ºC)")
eixos[0].set(xlabel="Leitura", ylabel="Temperatura (°C)", title="Temperatura ao longo do tempo")

eixos[1].plot(range(len(humidades)), humidades, label= "Humidade (%)")
eixos[1].set(xlabel="Leitura", ylabel="Humidade (%)", title="Humidade ao longo do tempo")

eixo_secundario = eixos[2].twinx()
eixos[2].set_ylabel("Temperatura (°C)")
eixo_secundario.set_ylabel("Humidade (%)")
eixos[2].plot(range(len(temperaturas)), temperaturas, label="Temperatura (°C)", color="red")
eixo_secundario.plot(range(len(humidades)), humidades, label="Humidade (%)", color="blue")

plt.tight_layout()
plt.show()