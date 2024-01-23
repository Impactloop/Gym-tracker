import pandas as pd 
import csv
import os
import seaborn as sns
import matplotlib.pyplot as plt
import PySimpleGUI as sg
local_path = os.path.dirname(os.path.abspath(__file__))
print(local_path)
#comprobación de la existencia del archivo
def habits_csv(path):
    if os.path.exists(path):
        print(f"File '{path}' already exists.")
    else:
        with open(path, 'w') as file:
            file.write("Aquí van tus hábitos")
            print("The habitdata file has been created.")

def gym_csv(path):
    if os.path.exists(path):
        print(f"File '{path}' already exists.")
    else:
        with open(path, 'w') as file:
            file.write("Aquí va tu rutina.")
            print("The gymdata file has been created.")

def get_csv_file_names(path):
    """Get a list of CSV file names in the specified folder."""
    csv_files = [file for file in os.listdir(path) if file.lower().endswith('.csv')]
    return csv_files

def choose_csv_file(csv_files):
    layout = [
        [sg.Text("Select a CSV file:")],
        *[[sg.Button(file_name)] for file_name in csv_files],
        [sg.Button("Exit")]
    ]

    # Create the window
    window = sg.Window("CSV File Selector", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Exit"):
            break
        else:
            selected_file = event
            sg.popup(f"You selected: {selected_file}", title="File Selected")

    window.close()

def create_columns_csv(dataframe):
    df_path = os.path.join(local_path, dataframe)
    print(df_path)
    df = pd.read_csv(df_path)
    

def main():
    # Check for existing data files
    habits_path = os.path.join(local_path, 'habitdata.csv')
    habits_csv(habits_path)

    gym_path = os.path.join(local_path, 'gymdata.csv')
    gym_csv(gym_path)

    # Create columns in CSV file
    options = get_csv_file_names(local_path)
    choose_csv_file(options)

    # Uncomment the line below if you want to create columns in a specific CSV file
    # create_columns_csv(options[0])

if __name__ == "__main__":
    main()