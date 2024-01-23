import subprocess
import sys

# Listado de librerías necesarias
required_libraries = ['pandas', 'seaborn', 'matplotlib', 'PySimpleGUI']

# Comprobación de la existencia de librerías
for library in required_libraries:
    try:
        __import__(library)
    except ImportError:
        print(f"{library} not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", library])


import pandas as pd 
import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
import PySimpleGUI as sg
import df_manipulator

local_path = os.path.dirname(os.path.abspath(__file__))


# Comprobación  de la existencia del archivo

def gym_csv(path):
    if os.path.exists(path):
        print(f"File '{path}' already exists.")
    else:
        with open(path, 'w') as file:
            file.write("Aquí va tu rutina.")
            print("The gymdata file has been created.")



# def create_columns_csv(dataframe):
#     path = os.path.join(local_path, dataframe)

#     df = pd.read_csv(path)
    
    

def main():
    # Comprobación de la existencia de archivos
    gym_path = os.path.join(local_path, 'gymdata.csv')
    gym_csv(gym_path)


if __name__ == "__main__":
    main()