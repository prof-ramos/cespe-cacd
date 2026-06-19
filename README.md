---
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

[![CC BY 4.0](https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![Hugging Face Dataset](https://img.shields.io/badge/%F0%9F%A4%97-Dataset%20Hub-yellow)](https://huggingface.co/datasets/profgabrielramos/cespe-cacd)
[![Python 3.12+](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)

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
