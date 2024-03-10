import pandas as pd

a_csv_file = pd.read_csv("./samples/sample.csv")

a_csv_file.rename(columns={'Index': 'Ind.'}, inplace=True)
print(a_csv_file)
