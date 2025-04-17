def insert_data_to_mysql(df, cursor, connection):
    insert_query = """
        INSERT INTO attacks (country, year, attack_type, target_industry, financial_loss_in_million,
                             number_of_affected_users, attack_source, security_vulnerability_type,
                             defense_mechanism_used, incident_resolution_time_in_hours)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for row in df.itertuples(index=False):
        cursor.execute(insert_query, row)

    connection.commit()
    print(f" {cursor.rowcount} rows inserted successfully.")
