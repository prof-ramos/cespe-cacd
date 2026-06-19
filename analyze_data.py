import pandas as pd

df = pd.read_csv("cacd_dataset.csv")

print("=== CACD Dataset Analysis ===")
print(f"Total Rows: {len(df)}")
print(f"Total Questions (Found): {df[df['nivel_profundidade'] == 0]['quantidade_encontrada'].sum()}")

print("\n=== Questions by Discipline (Top-level, nivel_profundidade == 0) ===")
disciplines = df[df['nivel_profundidade'] == 0].sort_values(by='quantidade_encontrada', ascending=False)
for _, row in disciplines.iterrows():
    print(f" - {row['disciplina']}: {row['quantidade_encontrada']} questions ({row['porcentagem_encontrada']}%)")

print("\n=== Top 15 Most Specific Topics (Leaf topics, max depth for their branches) ===")
# To find leaf topics, we look at rows where the hierarquia_codigo is not an ancestor of any other row.
all_codes = set(df['hierarquia_codigo'].dropna().unique())
leaf_records = []

for idx, row in df.iterrows():
    code = row['hierarquia_codigo']
    if pd.isna(code) or code == '':
        continue
    # If no other code starts with this code followed by '.', it's a leaf
    is_leaf = True
    for other_code in all_codes:
        if other_code.startswith(str(code) + '.'):
            is_leaf = False
            break
    if is_leaf:
        leaf_records.append(row)

df_leaves = pd.DataFrame(leaf_records)
top_leaves = df_leaves.sort_values(by='quantidade_encontrada', ascending=False).head(15)
for _, row in top_leaves.iterrows():
    print(f" - [{row['disciplina']}] {row['assunto_especifico']} ({row['hierarquia_codigo']}): {row['quantidade_encontrada']} questions")

print("\n=== Hierarchy Depth Distribution ===")
depth_counts = df['nivel_profundidade'].value_counts().sort_index()
for depth, count in depth_counts.items():
    print(f" - Level {depth}: {count} items")

print("\n=== Specific Insights for Top 3 Disciplines ===")
top_3_discs = disciplines['disciplina'].head(3).tolist()
for disc in top_3_discs:
    print(f"\n--- Top Topics in: {disc} ---")
    disc_df = df[(df['disciplina'] == disc) & (df['nivel_profundidade'] > 0)]
    # Look at level 1 topics
    lvl1_topics = disc_df[disc_df['nivel_profundidade'] == 1].sort_values(by='quantidade_encontrada', ascending=False).head(5)
    for _, row in lvl1_topics.iterrows():
        print(f"   * {row['assunto_especifico']}: {row['quantidade_encontrada']} questions ({row['porcentagem_encontrada']}%)")
