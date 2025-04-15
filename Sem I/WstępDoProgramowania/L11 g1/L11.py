import json
import pandas as pd
import matplotlib.pyplot as plt

def read_config(file_path):
    try:
        with open(file_path, 'r') as config_file:
            config = json.load(config_file)
            validate_config(config)
            return config
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except json.JSONDecodeError:
        print(f"Error decoding JSON in {file_path}")
        exit(1)
    except ValueError as e:
        print(f"Invalid config: {e}")
        exit(1)

def validate_config(config):
    required_keys = ['kody obszaru', 'lata', 'wskaźniki']
    for key in required_keys:
        if key not in config:
            raise ValueError(f"Missing key in config: {key}")

def read_data(file_path):
    try:
        data = pd.read_excel(file_path, sheet_name='TABLICA')
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit(1)
    except pd.errors.EmptyDataError:
        print(f"No data found in sheet 'TABLICA' of {file_path}")
        exit(1)

def plot_graph(data, config):
    areas = config['kody obszaru']
    years = config['lata']
    indicators = config['wskaźniki']

    for indicator in indicators:
        plt.figure(figsize=(10, 6))
        plt.title(f'Wykres dla wskaźnika {indicator}')
        plt.xlabel('Lata')
        plt.ylabel('Wartość wskaźnika')

        for area in areas:
            area_data = data[data['Kod'] == area]
            indicator_data = area_data[area_data['Indeks wskaźnika'] == indicator]
            plt.plot(indicator_data['Rok'], indicator_data['Wartość'], label=f'Obszar {area}')

        plt.legend()
        plt.show()

if __name__ == "__main__":
    config_file_path = '/Users/vusis/Documents/Program/WstępDoProgramowania/L11 g1/konf.json'
    data_file_path = '/Users/vusis/Documents/Program/WstępDoProgramowania/L11 g1/dane_g1.xlsx'

    config = read_config(config_file_path)
    data = read_data(data_file_path)

    plot_graph(data, config)
