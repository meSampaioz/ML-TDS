"""Gerando dados sintéticos para fins de teste e demonstração."""


import numpy as np
import pandas as pd


def gerar_dados_sinteticos(n: int = 900, seed: int = 42) -> pd.DataFrame:
    if n < 2:
        raise ValueError("n must be at least 2")
    rng = np.random.default_rng(seed)
    idade = rng.integers(18, 66, size=n)
    cidade = rng.choice(
        ["Campos dos Goytacazes", "Macaé", "Niterói"], n
    )
    profissao = rng.choice(
        ["Enfermeiro", "Analista", "Professor"], n
    )
    faixa_renda = rng.choice(
        ["Baixa", "Média", "Alta"], n
    )
    return pd.DataFrame({
        "idade": idade,
        "cidade": cidade,
        "profissao": profissao,
        "faixa_renda": faixa_renda      
    })
