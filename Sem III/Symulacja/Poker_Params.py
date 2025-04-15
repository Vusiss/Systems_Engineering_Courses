import itertools
import pandas as pd

# Definicja poziomów dla każdego parametru
player_types = ['CautiousPlayer', 'PatientPlayer', 'PassivePlayer', 'AgressivePlayer']
starting_money_levels = [500, 2500, 5000, 7500, 10000]  # Okrągłe poziomy pieniędzy
recklessness_levels = [0.1, 0.5, 0.9]  # Lekkomyślność: niski, średni, wysoki
extravagance_levels = [0.1, 0.5, 0.9]  # Rozrzutność: niski, średni, wysoki


expected_hands = [
    'High card', 'One pair', 'Two pair', 'Three-of-a-Kind',
    'Straight', 'Flush', 'Full house', 'Four-of-a-Kind', 'Straight flush'
]

# Generowanie wszystkich kombinacji parametrów
parameter_combinations = list(itertools.product(
    player_types,
    starting_money_levels,
    recklessness_levels,
    extravagance_levels,
    expected_hands
))

# Konwersja do DataFrame dla przejrzystości
columns = ["Typ gracza", "Pieniądze na wstępie", "Lekkomyślność", "Rozrzutność", "Minimalna oczekiwana ręka"]
df_params = pd.DataFrame(parameter_combinations, columns=columns)