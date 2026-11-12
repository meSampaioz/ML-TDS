import pandas as pd
from privacy_ml.dados_sinteticos import gerar_dados_sinteticos

dados = gerar_dados_sinteticos()
dados_generalizados = dados.copy()

k = 20
etapa = 0

def calcular_menor_grupo(tabela):
    grupos = tabela.groupby(
        ["idade", "cidade", "profissao"],
        observed=True
    ).size()

    menor_grupo = grupos.min()
    grupos_menores = grupos[grupos == menor_grupo]

    return menor_grupo, grupos_menores

print("\n========== INICIANDO ANONIMIZAÇÃO ==========")

print(f"\nTotal de registros gerados: {len(dados)}")
print("Atributos analisados: idade, cidade e profissão")
print(f"Meta de anonimização: k = {k}")

while True:

    print(f"\n{'=' * 50}")
    print(f"ETAPA {etapa} — ANÁLISE DOS DADOS")
    print(f"{'=' * 50}")

    print("\n[1] AMOSTRA DOS DADOS")
    print(f"Exibindo apenas 5 dos {len(dados_generalizados)} registros:")
    print(dados_generalizados.head(5))

    print("\n[2] VERIFICAÇÃO DO K-ANONIMATO")
    print(f"Total de registros analisados: {len(dados_generalizados)}")

    menor_grupo, grupos_menores = calcular_menor_grupo(
        dados_generalizados
    )

    print("\nGrupo(s) com a menor quantidade de registros:")
    print(grupos_menores.to_string())

    print(f"\nMenor grupo encontrado: {menor_grupo} pessoas")
    print(f"Quantidade mínima exigida por grupo: {k} pessoas")

    print("\n[3] RESULTADO DA VERIFICAÇÃO")

    if menor_grupo >= k:
        print("✅ K-ANONIMATO ATINGIDO!")
        print("✅ ANONIMIZAÇÃO CONCLUÍDA COM SUCESSO!")
        break

    print("❌ K-anonimato não atingido.")

    if etapa == 0:
        print("\n[4] PRÓXIMA AÇÃO: Generalizando idades...")

        dados_generalizados["idade"] = pd.cut(
            dados_generalizados["idade"],
            bins=[18, 30, 40, 50, 66],
            labels=["18-29", "30-39", "40-49", "50-65"],
            right=False
        )

    elif etapa == 1:
        print("\n[4] PRÓXIMA AÇÃO: Generalizando cidades...")

        dados_generalizados["cidade"] = "Rio de Janeiro (estado)"

    else:
        print("\n⚠️ Não há mais generalizações disponíveis.")
        print("Não foi possível atingir o k desejado.")
        break

    etapa += 1