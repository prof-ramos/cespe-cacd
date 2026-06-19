import pandas as pd

excel_path = "/Users/gabrielramos/Downloads/20604800-e629-4027-84cc-cfcd86707411.xlsx"
df = pd.read_excel(excel_path, sheet_name='Índice do Caderno')

max_depth = 0
for idx, row in df.iterrows():
    h = row['Hierarquia']
    if pd.notna(h):
        depth = len(str(h).split('.'))
        if depth > max_depth:
            max_depth = depth
            print(f"New max depth {max_depth} at row {idx} with hierarchy: {h}")

print(f"\nFinal Maximum Depth: {max_depth}")
