import os
from huggingface_hub import HfApi

# 1. Create README.md dataset card
readme_content = """---
configs:
  - config_name: default
    data_files:
      - split: train
        path: cacd_dataset.csv
license: cc-by-4.0
dataset_info:
  features:
    - name: linha_original
      dtype: int64
    - name: disciplina
      dtype: string
    - name: hierarquia_codigo
      dtype: string
    - name: nivel_profundidade
      dtype: int64
    - name: assunto_nivel_1
      dtype: string
    - name: assunto_nivel_2
      dtype: string
    - name: assunto_nivel_3
      dtype: string
    - name: assunto_nivel_4
      dtype: string
    - name: assunto_especifico
      dtype: string
    - name: quantidade_encontrada
      dtype: int64
    - name: porcentagem_encontrada
      dtype: float64
    - name: quantidade_caderno
      dtype: int64
    - name: porcentagem_caderno
      dtype: float64
  citation: |-
    @misc{gabriel-ramos-cespe-cacd,
      author       = {Gabriel Ramos},
      title        = {cespe-cacd: Distribuição de Conteúdos CACD/CESPE},
      year         = {2026},
      publisher    = {Hugging Face},
      journal      = {Hugging Face Datasets}
    }
---

# cespe-cacd

Dataset contendo a análise e distribuição dos conteúdos programáticos do Concurso de Admissão à Carreira de Diplomata (CACD) da banca CESPE/Cebraspe.

Este dataset mapeia 19 disciplinas do edital com uma estrutura de até 4 níveis de assuntos.

## Arquivos Disponíveis

* `cacd_dataset.csv`: Dataset limpo em formato CSV (658 linhas, 19 disciplinas).
* `cacd_dataset.json`: Dataset limpo em formato JSON.
* `cacd_dataset.parquet`: Dataset limpo em formato colunar Parquet.
* `cacd_dataset.xlsx`: Dataset limpo em formato de planilha Excel.
* `original_cacd.xlsx`: Planilha original contendo a exportação bruta do edital.
* `generate_dataset.py`: Script para processamento local.
* `EDITAL_CACD_2026.md`: O edital oficial em formato Markdown de 2026.

## Licença

Este dataset é disponibilizado sob a licença **Creative Commons Attribution 4.0 International (CC BY 4.0)**.
"""

with open("README.md", "w", encoding="utf-8") as f:
    f.write(readme_content)

# 2. Setup repo and upload
api = HfApi()
repo_id = "profgabrielramos/cespe-cacd"

print(f"Creating dataset repository: {repo_id}...")
api.create_repo(
    repo_id=repo_id,
    repo_type="dataset",
    private=False,
    exist_ok=True
)

# Upload map: local path -> destination path on repo
uploads = {
    "README.md": "README.md",
    "cacd_dataset.csv": "cacd_dataset.csv",
    "cacd_dataset.json": "cacd_dataset.json",
    "cacd_dataset.parquet": "cacd_dataset.parquet",
    "cacd_dataset.xlsx": "cacd_dataset.xlsx",
    "generate_dataset.py": "generate_dataset.py",
    "EDITAL_CACD_2026.md": "EDITAL_CACD_2026.md",
    "original_cacd.xlsx": "original_cacd.xlsx"
}

print("Uploading files to Hugging Face Hub...")
for local_file, repo_file in uploads.items():
    if os.path.exists(local_file):
        print(f" - Uploading {local_file} as {repo_file}...")
        api.upload_file(
            path_or_fileobj=local_file,
            path_in_repo=repo_file,
            repo_id=repo_id,
            repo_type="dataset"
        )

print("\nUpload completed successfully!")
print(f"Check your dataset on Hugging Face: https://huggingface.co/datasets/{repo_id}")
