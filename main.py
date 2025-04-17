from data_loader import load_data
from data_cleaner import clean_dataset
from db_connector import connect_to_db
from db_inserter import insert_data_to_mysql
from analysis import perform_analysis

file_path = 'C:/Users/gudur/Desktop/Projects/Global_Cybersecurity_Threats_2015-2024.csv'

df = load_data(file_path)

if df is not None:
    df = clean_dataset(df)

    connection = connect_to_db()
    cursor = connection.cursor()
    print("🔗 MySQL connection established!")

    insert_data_to_mysql(df, cursor, connection)
    cursor.close()
    connection.close()

    perform_analysis(df)
