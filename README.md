---
configs:
  - config_name: default
    data_files:
      - split: train
        path: cacd_dataset.csv
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
---

# cespe-cacd

Dataset contendo a análise e distribuição dos conteúdos programáticos do Concurso de Admissão à Carreira de Diplomata (CACD) da banca CESPE/Cebraspe.

Este dataset mapeia 19 disciplinas do edital com uma estrutura de até 4 níveis de assuntos.

## Arquivos Disponíveis

* `cacd_dataset.csv`: Dataset limpo em formato CSV.
* `cacd_dataset.json`: Dataset limpo em formato JSON.
* `cacd_dataset.parquet`: Dataset limpo em formato colunar Parquet.
* `cacd_dataset.xlsx`: Dataset limpo em formato de planilha Excel.
* `original_cacd.xlsx`: Planilha original contendo a exportação bruta do edital.
* `generate_dataset.py`: Script para processamento local.
* `EDITAL_CACD_2026.md`: O edital oficial em formato Markdown de 2026.
