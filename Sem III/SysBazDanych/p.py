import mysql.connector
# Ustawienia połączenia
config = {
'user': 'new_user',
'password': 'new_password',
'host': 'localhost',
'database': 'MojaBazaDanych',
'port': 3306, # Domyślnie 3306, MySQL miniserver port 3311
'charset': 'utf8', # Jeżeli potrzebne, zmień na obsługiwany zestaw znaków
'raise_on_warnings': True,
# 'auth_plugin':'r'
'auth_plugin':'mysql_native_password'
}
# Utworzenie połączenia
conn = mysql.connector.connect(**config)
# Utworzenie obiektu kursora
cursor = conn.cursor()
# Przykładowe zapytanie
cursor.execute("SELECT * FROM MojaTabela")
# Pobranie wyników
result = cursor.fetchall()
# Wyświetlenie wyników
for row in result:
    print(row)
# Zamknięcie połączenia
cursor.close()
conn.close()