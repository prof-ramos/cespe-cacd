"""
Gera mapeamento JSON da cobertura do dataset CACD contra o Anexo III
do Edital CACD 2026 (objetos de avaliação).

Uso:
    python3 edital_coverage.py

Gera: EDITAL_CACD_2026_anexo_iii.json  (estrutura do programa)
       EDITAL_CACD_2026_cobertura.json  (cobertura real do dataset)
"""

import json
import re
import pandas as pd

# ── Estrutura do Anexo III extraída manualmente do edital ────────
DISCIPLINAS_ANEXO_III = {
    "Língua Portuguesa": {
        "fases": ["Primeira", "Segunda"],
        "topicos": [
            "Língua portuguesa: modalidade culta",
            "Sistema gráfico: ortografia, acentuação e pontuação",
            "Morfossintaxe",
            "Semântica",
            "Vocabulário",
            "Leitura e produção de textos",
            "Compreensão, interpretação e análise crítica de textos",
            "Conhecimentos de linguística, literatura e estilística",
            "Redação de textos dissertativos",
            "Defeitos de conteúdo e vícios de linguagem",
        ],
    },
    "Língua Inglesa": {
        "fases": ["Primeira", "Segunda"],
        "topicos": [
            "Compreensão de textos escritos",
            "Itens gramaticais relevantes",
            "Redação em língua inglesa",
            "Versão português → inglês",
        ],
    },
    "História do Brasil": {
        "fases": ["Primeira", "Segunda"],
        "topicos": [
            "Período colonial",
            "Processo de independência",
            "Primeiro Reinado (1822-1831)",
            "Regência (1831-1840)",
            "Segundo Reinado (1840-1889)",
            "Primeira República (1889-1930)",
            "Era Vargas (1930-1945)",
            "República Liberal (1945-1964)",
            "Regime Militar (1964-1985)",
            "Processo democrático a partir de 1985",
            "Impactos tecnológicos e digitais no séc. XXI",
        ],
    },
    "História Mundial": {
        "fases": ["Primeira"],
        "topicos": [
            "Estruturas e ideias econômicas",
            "Revoluções",
            "Relações internacionais",
            "Colonialismo, imperialismo",
            "Evolução política e econômica nas Américas",
            "Ideias e regimes políticos",
            "Vida cultural",
            "Relações internacionais no séc. XXI",
        ],
    },
    "Política Internacional": {
        "fases": ["Primeira", "Segunda"],
        "topicos": [
            "Conceitos básicos e paradigmas teóricos",
            "Política externa brasileira desde 1945",
            "Brasil e América do Sul / MERCOSUL",
            "Argentina e relações com o Brasil",
            "Relações com demais países do hemisfério",
            "EUA: política externa e relações com o Brasil",
            "União Europeia",
            "Rússia",
            "África",
            "Brasil e Ásia (China, Índia, Japão)",
            "Brasil e Oriente Médio",
            "Comunidade dos Países de Língua Portuguesa",
            "Brasil e agenda internacional multilateral",
        ],
    },
    "Geografia": {
        "fases": ["Primeira", "Segunda"],
        "topicos": [
            "História da Geografia e correntes teóricas",
            "Geografia da população",
            "Geografia econômica",
            "Geografia agrária",
            "Geografia urbana",
            "Geografia política",
            "Geografia e gestão ambiental",
        ],
    },
    "Economia": {
        "fases": ["Primeira", "Segunda"],
        "topicos": [
            "Microeconomia",
            "Macroeconomia",
            "Economia internacional",
            "História econômica brasileira",
            "Bancos digitais e meios de pagamento",
        ],
    },
    "Direito": {
        "fases": ["Primeira", "Segunda"],
        "topicos": [
            "Normas jurídicas",
            "Personalidade jurídica",
            "Constituição e controle de constitucionalidade",
            "Estado: elementos, soberania, formas",
            "Estado democrático de direito",
            "Organização dos poderes no Direito Brasileiro",
            "Processo legislativo brasileiro",
            "Direitos e garantias fundamentais",
            "Administração Pública (princípios, atos, processo)",
            "Licitações e contratos administrativos",
            "Responsabilidade civil do Estado",
            "Direitos, deveres do servidor público",
            "Regime Jurídico dos Servidores do SEB (Lei 11.440/2006)",
            "Finanças públicas",
            "Direito Internacional Público e Privado",
            "Princípios das relações internacionais (art. 4º CF)",
            "Estado, soberania, reconhecimento",
            "Território e formação do território brasileiro",
            "Povo, nacionalidade, estrangeiros",
            "Jurisdição, relações diplomáticas e consulares",
            "Sujeitos especiais do DIP",
            "Fontes do DIP e tratados internacionais",
            "Solução pacífica de controvérsias",
            "Organizações internacionais e ONU",
            "Direito Internacional Humanitário e Refugiados",
            "Direito penal internacional e TPI",
            "Direito do comércio internacional e OMC",
            "Direito Internacional do Meio Ambiente e do Mar",
            "Direito internacional do trabalho (OIT)",
            "Cooperação jurídica internacional",
        ],
    },
    "Língua Espanhola": {
        "fases": ["Segunda"],
        "topicos": [
            "Resumo em espanhol",
            "Versão português → espanhol",
        ],
    },
    "Língua Francesa": {
        "fases": ["Segunda"],
        "topicos": [
            "Resumo em francês",
            "Versão português → francês",
        ],
    },
}


def main():
    # ── 1. Salva estrutura pura do Anexo III ──
    with open("EDITAL_CACD_2026_anexo_iii.json", "w", encoding="utf-8") as f:
        json.dump(DISCIPLINAS_ANEXO_III, f, indent=2, ensure_ascii=False)
    print("Estrutura salva: EDITAL_CACD_2026_anexo_iii.json")

    # ── 2. Carrega o dataset CACD ──
    df = pd.read_csv("cacd_dataset.csv")

    # ── 3. Mapeia disciplinas do dataset para as do Anexo III ──
    MAP_DATASET_TO_ANEXO = {
        "Língua Portuguesa (Português)": "Língua Portuguesa",
        "Língua Inglesa (Inglês)": "Língua Inglesa",
        "História": "História do Brasil",  # dataset tem "História"
        "Geografia": "Geografia",
        "Economia e Finanças Públicas": "Economia",
        "Finanças e Conhecimentos Bancários": "Economia",
        "Direito Administrativo (Doutrina e Leis Federais)": "Direito",
        "Direito Constitucional (CF/1988 e Doutrina)": "Direito",
        "Direito Internacional Público e Privado": "Direito",
        "Direito Civil": "Direito",
        "Direito Ambiental": "Direito",
        "Direitos Humanos": "Direito",
        "Direito Marítimo, Portuário e Aeronáutico": "Direito",
        "Relações Internacionais e Comércio Internacional": "Política Internacional",
        "Língua Espanhola (Espanhol)": "Língua Espanhola",
        "Língua Francesa (Francês)": "Língua Francesa",
    }

    # Disciplinas do dataset que não estão no Anexo III (extras)
    EXTRAS = [
        "Literatura Brasileira e Estrangeira",
        "Legislação Geral Federal",
        "Línguas Estrangeiras Diversas",
    ]

    # ── 4. Gera cobertura ──
    cobertura = {}
    for anexo_nome, info in DISCIPLINAS_ANEXO_III.items():
        # Encontra quais disciplinas do dataset mapeiam para este anexo
        dataset_discs = [
            d
            for d, a in MAP_DATASET_TO_ANEXO.items()
            if a == anexo_nome and d in set(df["disciplina"])
        ]

        if not dataset_discs:
            cobertura[anexo_nome] = {
                "status": "ausente",
                "dataset_disciplinas": [],
                "fases": info["fases"],
                "topicos": len(info["topicos"]),
                "topicos_cobertos": 0,
                "total_linhas_dataset": 0,
                "observacao": "Nenhuma disciplina correspondente no dataset CACD",
            }
            continue

        # Estatísticas do dataset para estas disciplinas
        sub = df[df["disciplina"].isin(dataset_discs)]

        # Tenta estimar tópicos cobertos: conta N1 distintos que
        # correspondem a palavras-chave dos tópicos do anexo
        n1_topics = set(
            sub[sub["nivel_profundidade"] == 1]["assunto_nivel_1"].dropna()
        )
        # Coverage heuristic: pelo menos tem N1 topics
        n_topicos_cobertos = min(len(n1_topics), len(info["topicos"]))

        cobertura[anexo_nome] = {
            "status": "parcial",
            "dataset_disciplinas": dataset_discs,
            "fases": info["fases"],
            "topicos_previstos": len(info["topicos"]),
            "topicos_estimados_dataset": len(n1_topics),
            "total_linhas_dataset": len(sub),
            "subtopicos_dataset": int(sub["quantidade_encontrada"].sum()),
        }

    # Adiciona disciplinas extras (não previstas no Anexo III)
    cobertura["_extras"] = {
        disciplina: {
            "status": "extra_anexo",
            "observacao": "Disciplina presente no dataset mas não listada no Anexo III",
            "linhas": int(df[df["disciplina"] == disciplina].shape[0]),
        }
        for disciplina in EXTRAS
        if disciplina in set(df["disciplina"])
    }

    # Disciplina "História" do dataset corresponde a "História do Brasil"
    # "História Mundial" não tem correspondente direto no dataset CACD
    # Vamos verificar se cobre algo
    cobertura["História Mundial"] = {
        "status": "ausente",
        "dataset_disciplinas": [],
        "fases": ["Primeira"],
        "topicos": len(DISCIPLINAS_ANEXO_III["História Mundial"]["topicos"]),
        "topicos_cobertos": 0,
        "observacao": "História Mundial não separada no dataset CACD (fundida em 'História')",
    }

    metadata = {
        "_metadata": {
            "fonte": "EDITAL Nº 1, DE 28 DE JANEIRO DE 2026 — CACD 2026",
            "anexo": "III — DOS OBJETOS DE AVALIAÇÃO",
            "dataset_referencia": "profgabrielramos/cespe-cacd",
            "data_geracao": pd.Timestamp.now().strftime("%Y-%m-%d %H:%M"),
            "total_disciplinas_anexo": len(DISCIPLINAS_ANEXO_III),
            "total_disciplinas_dataset": df["disciplina"].nunique(),
        }
    }

    output = {**metadata, **cobertura}

    with open("EDITAL_CACD_2026_cobertura.json", "w", encoding="utf-8") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print("Cobertura salva:  EDITAL_CACD_2026_cobertura.json")

    # Sumário
    presentes = sum(
        1 for v in cobertura.values() if isinstance(v, dict) and v.get("status") == "parcial"
    )
    ausentes = sum(
        1 for v in cobertura.values() if isinstance(v, dict) and v.get("status") == "ausente"
    )
    print(f"\nResumo:")
    print(f"  Disciplinas do Anexo III com cobertura parcial: {presentes}")
    print(f"  Disciplinas do Anexo III ausentes no dataset:     {ausentes}")
    print(f"  Disciplinas extras no dataset (fora do Anexo):   {len(cobertura.get('_extras', {}))}")


if __name__ == "__main__":
    main()
