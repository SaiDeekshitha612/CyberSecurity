def clean_dataset(df):
    df.drop_duplicates(inplace=True)
    df.dropna(inplace=True)
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_').str.replace(r'[^\w\s]', '', regex=True)

    columns_to_clean = [
        'country',
        'attack_type',
        'target_industry',
        'attack_source',
        'security_vulnerability_type',
        'defense_mechanism_used'
    ]

    for col in columns_to_clean:
        df[col] = df[col].str.strip().str.title()

    print(" Data cleaning completed.")
    print(df.info())
    return df
