import serial
import csv
import time

# important variables
port = "COM4"
baud_rate = 115200
file_name = "sensor_data.csv"

sensor_data = serial.Serial(port, baud_rate)
time.sleep(2)  # wait for the serial connection to initialize

while True:

    if sensor_data.in_waiting > 0: 
        print("Reading sensor data...")
        sensor_data_string = sensor_data.readline().decode('utf-8').strip()
        if "Temperatura" in sensor_data_string:
            single_elements = sensor_data_string.split(",")

            temperatura_1 = single_elements[0].split(":")
            humidade_1 = single_elements[1].split(":")

            temperatura_2 = temperatura_1[1].split(" ")
            humidade_2 = humidade_1[1].split(" ")

            temperatura_final_string = temperatura_2[1]
            humidade_final_string = humidade_2[1]

            temperatura_final = float(temperatura_final_string)
            humidade_final = float(humidade_final_string)

            with open(file_name, "a") as variavel:
                # código que usa "variavel" aqui dentro
                escritor = csv.writer(variavel)
                escritor.writerow([temperatura_final, humidade_final, time.time()])





            



    
    
