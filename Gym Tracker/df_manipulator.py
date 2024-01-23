import PySimpleGUI as sg
import pandas as pd
import os

local_path = os.path.dirname(os.path.abspath(__file__))

def read_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        return df
    except Exception as e:
        sg.popup_error(f"Error reading CSV file: {e}")
        return None

def create_column(df, column_name, default_value):
    df[column_name] = default_value

def modify_column(df, column_name, new_values):
    if column_name in df.columns:
        df[column_name] = new_values
    else:
        sg.popup_error(f"Column '{column_name}' not found in the CSV file.")

def delete_column(df, column_name):
    if column_name in df.columns:
        df.drop(columns=[column_name], inplace=True)
    else:
        sg.popup_error(f"Column '{column_name}' not found in the CSV file.")

def get_csv_file_names(path):
    """Get a list of CSV file names in the specified folder."""
    csv_files = [file for file in os.listdir(path) if file.lower().endswith('.csv')]
    return csv_files

def choose_csv_file(csv_files):
    layout = [
        [sg.Text("Selecciona un archivo:")],
        *[[sg.Button(file_name)] for file_name in csv_files],
        [sg.Button("Salir")]
    ]

    # Open file selector window
    window = sg.Window("Selector de archivo", layout)

    while True:
        event, values = window.read()

        if event in (sg.WIN_CLOSED, "Salir"):
            break
        else:
            selected_file = event
            file_name_without_extension, _ = os.path.splitext(selected_file)
            sg.popup(f"Has seleccionado: {file_name_without_extension}", title="Archivo seleccionado")

    window.close()
    return selected_file

def create_column_window():
    layout = [
        [sg.Text('Create Column')],
        [sg.Text('Column Name:'), sg.InputText(key='COLUMN_NAME')],
        [sg.Text('Default Value:'), sg.InputText(key='DEFAULT_VALUE')],
        [sg.Button('Execute'), sg.Button('Back')]
    ]

    return sg.Window('Create Column', layout)

def modify_column_window():
    layout = [
        [sg.Text('Modify Column')],
        [sg.Text('Column Name:'), sg.InputText(key='COLUMN_NAME')],
        [sg.Text('New Values:'), sg.InputText(key='NEW_VALUES')],
        [sg.Button('Execute'), sg.Button('Back')]
    ]

    return sg.Window('Modify Column', layout)

def delete_column_window():
    layout = [
        [sg.Text('Delete Column')],
        [sg.Text('Column Name:'), sg.InputText(key='COLUMN_NAME')],
        [sg.Button('Execute'), sg.Button('Back')]
    ]

    return sg.Window('Delete Column', layout)

def main_window():
    layout = [
        [sg.Text('CSV Manipulator')],
        [sg.Button('Read')],
        [sg.Button('Create Column')],
        [sg.Button('Modify Column')],
        [sg.Button('Delete Column')],
        [sg.Button('Exit')]
    ]

    return sg.Window('Main Menu', layout)

def main():
    sg.theme('LightBlue2')  # Set the GUI theme
    main_win = main_window()

    while True:
        event, values = main_win.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        elif event == 'Read':
            selected_file = choose_csv_file(get_csv_file_names(local_path))
            file_path = os.path.join(local_path, selected_file)
            df = read_csv(file_path)
            if df is not None:
                sg.popup(f"CSV File Contents:\n{df}")
        elif event == 'Create Column':
            create_win = create_column_window()
            while True:
                event, values = create_win.read()

                if event == sg.WIN_CLOSED or event == 'Back':
                    create_win.close()
                    break
                elif event == 'Execute':
                    # Perform create column operation
                    column_name = values['COLUMN_NAME']
                    default_value = values['DEFAULT_VALUE']
                    file_path = os.path.join(local_path, selected_file)
                    df = read_csv(file_path)
                    create_column(df, column_name, default_value)
                    sg.popup('Column created successfully.')
                    create_win.close()
        elif event == 'Modify Column':
            modify_win = modify_column_window()
            while True:
                event, values = modify_win.read()

                if event == sg.WIN_CLOSED or event == 'Back':
                    modify_win.close()
                    break
                elif event == 'Execute':
                    # Perform modify column operation
                    column_name = values['COLUMN_NAME']
                    new_values = values['NEW_VALUES']
                    file_path = os.path.join(local_path, selected_file)
                    df = read_csv(file_path)
                    modify_column(df, column_name, new_values.split(','))
                    sg.popup('Column modified successfully.')
                    modify_win.close()
        elif event == 'Delete Column':
            delete_win = delete_column_window()
            while True:
                event, values = delete_win.read()

                if event == sg.WIN_CLOSED or event == 'Back':
                    delete_win.close()
                    break
                elif event == 'Execute':
                    # Perform delete column operation
                    column_name = values['COLUMN_NAME']
                    file_path = os.path.join(local_path, selected_file)
                    df = read_csv(file_path)
                    delete_column(df, column_name)
                    sg.popup('Column deleted successfully.')
                    delete_win.close()

    main_win.close()

# Call the main function if this script is executed directly
if __name__ == '__main__':
    main()
