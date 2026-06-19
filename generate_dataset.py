import pandas as pd

excel_path = "/Users/gabrielramos/Downloads/20604800-e629-4027-84cc-cfcd86707411.xlsx"
df = pd.read_excel(excel_path, sheet_name='Índice do Caderno')

active_path = {0: None, 1: None, 2: None, 3: None, 4: None}
dataset_records = []

def parse_percentage(val):
    if pd.isna(val):
        return 0.0
    val_str = str(val).replace('%', '').strip()
    try:
        return float(val_str)
    except ValueError:
        return 0.0

for idx, row in df.iterrows():
    h = row['Hierarquia']
    indice = row['Índice']
    
    # Identify depth level and update hierarchy path tracker
    if pd.isna(h):
        active_path[0] = indice
        active_path[1] = None
        active_path[2] = None
        active_path[3] = None
        active_path[4] = None
        level = 0
    else:
        parts = str(h).split('.')
        level = len(parts)
        active_path[level] = indice
        # Clear sub-level paths
        for depth in range(level + 1, 5):
            active_path[depth] = None

    pct_enc = parse_percentage(row['Porcentagem'])
    pct_cad = parse_percentage(row['Porcentagem.1'])
    qty_enc = int(row['Quantidade encontrada'])
    qty_cad = int(row['Quantidade no caderno'])
    
    dataset_records.append({
        'linha_original': idx,
        'disciplina': active_path[0],
        'hierarquia_codigo': h if pd.notna(h) else '',
        'nivel_profundidade': level,
        'assunto_nivel_1': active_path[1] if active_path[1] else '',
        'assunto_nivel_2': active_path[2] if active_path[2] else '',
        'assunto_nivel_3': active_path[3] if active_path[3] else '',
        'assunto_nivel_4': active_path[4] if active_path[4] else '',
        'assunto_especifico': indice,
        'quantidade_encontrada': qty_enc,
        'porcentagem_encontrada': pct_enc,
        'quantidade_caderno': qty_cad,
        'porcentagem_caderno': pct_cad
    })

df_clean = pd.DataFrame(dataset_records)

# Define file outputs
csv_output = "cacd_dataset.csv"
json_output = "cacd_dataset.json"
parquet_output = "cacd_dataset.parquet"
xlsx_output = "cacd_dataset.xlsx"

# Save to various formats
df_clean.to_csv(csv_output, index=False, encoding='utf-8-sig')
df_clean.to_json(json_output, orient='records', indent=2, force_ascii=False)
df_clean.to_parquet(parquet_output, index=False)
df_clean.to_excel(xlsx_output, index=False)

print("Dataset conversion completed successfully!")
print("Cleaned dataset saved as:")
print(f" - CSV:     {csv_output}")
print(f" - JSON:    {json_output}")
print(f" - Parquet: {parquet_output}")
print(f" - Excel:   {xlsx_output}")
print(f"\nTotal rows processed: {len(df_clean)}")
print(f"Columns in dataset: {list(df_clean.columns)}")
