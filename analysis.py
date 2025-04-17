from tabulate import tabulate
import pandas as pd

def print_table(title, data):
    print(f"\n📌 {title}")
    if isinstance(data, pd.DataFrame):
        print(tabulate(data, headers='keys', tablefmt='pretty'))
    elif isinstance(data, pd.Series):
        print(tabulate(data.reset_index().values, headers=['Index', 'Value'], tablefmt='pretty'))
    else:
        print(tabulate(data, headers='keys', tablefmt='pretty'))

def perform_analysis(df):
    top_countries = df['country'].value_counts().head(10)
    threat_frequency = df['attack_type'].value_counts()
    yearly_trends = df.groupby('year').size()
    impact_by_region = df.groupby('country')['financial_loss_in_million_'].sum().sort_values(ascending=False).head(10)
    attack_sector_correlation = df.groupby(['attack_type', 'target_industry']).size().unstack(fill_value=0)

    print_table("Top 10 Countries Affected by Cyber Attacks", top_countries)
    print_table("Frequency of Threat Types", threat_frequency)
    print_table("Year-over-Year Incident Counts", yearly_trends)
    print_table("Top 10 Countries by Financial Impact", impact_by_region)
    print_table("Attack Type vs. Target Industry Matrix", attack_sector_correlation)
