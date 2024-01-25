import PySimpleGUI as sg
import pandas as pd
import os
import csv

data_path = 'Files\Data'
local_path = os.path.dirname(os.path.abspath(__file__))

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        sg.popup_error(f"Error reading CSV file: {e}")
        return None


def generate_csv():

    BlankGymCSV = "Date, Day_of_Week, Routine_Type, Specific_Day_Routine, Exercise, Sets, Reps, Weight, RPE, Theoretical_OneRM"
    
    

    # Create the 'Data' directory if it doesn't exist
    if not os.path.exists(os.path.join(local_path, data_path)):
        os.makedirs(os.path.join(local_path, data_path))

    # Function to write a list of objects to a CSV file
    def write_csv(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(BlankGymCSV.split(", "))  # Split the header string into a list

    # PySimpleGUI window layout to get the number of routines per week
    layout_get_routines = [
        [sg.Text("How many different routines do you have per week?")],
        [sg.InputText(key='-NUM_ROUTINES-')],
        [sg.Button('OK')]
    ]

    window_get_routines = sg.Window('Number of Routines', layout_get_routines)

    event, values = window_get_routines.read()
    num_routines = int(values['-NUM_ROUTINES-'])
    window_get_routines.close()

    # PySimpleGUI window layout to get the names of the routines
    layout_get_names = [[sg.Text(f"Enter name for Routine {i + 1}: "), sg.InputText(key=f'-ROUTINE_{i+1}-')] for i in range(num_routines)]
    layout_get_names.append([sg.Button('OK')])

    window_get_names = sg.Window('Enter Routine Names', layout_get_names)

    event, values = window_get_names.read()

    routine_names = [values[f'-ROUTINE_{i+1}-'].strip() for i in range(num_routines)]
    window_get_names.close()

    # Creating CSV files based on routine names
    for routine_name in routine_names:
        if routine_name:
            file_path = os.path.join(local_path, data_path, f"{routine_name}.csv")
            write_csv(file_path)
            #sg.popup(f"CSV file '{file_path}' created successfully.")
        else:
            sg.popup_error("Please enter valid routine names.")

#funcion returns the name of the csv file in str format
def select_csv_file(path):
    csv_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f)) and f.endswith('.csv')]
    
    layout = [[sg.Button(csv_file, key=csv_file)] for csv_file in csv_files]
    window = sg.Window('CSV File Selector', layout)

    selected_file = None

    while True:
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        elif event in csv_files:
            selected_file = event
            break

    window.close()

    return selected_file


def main():
    data_path = 'Files\Data'
    local_path = os.getcwd()
    file_path = os.path.join(local_path, data_path)
    selected_file = select_csv_file(file_path)

    if selected_file:
        print(f"Selected CSV file: {selected_file}")
    else:
        print("No file selected.")
        
    return


if __name__ == '__main__':
    main()
