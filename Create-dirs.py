import os
import sys
#Solicitar el nombre de la carpeta a crear
new_dir = str(input("Write the name for the new dir: "))

dir_path = os.path.dirname(os.path.realpath(__file__))
for root, dirs, files in os.walk(dir_path):
    os.mkdir(new_dir)