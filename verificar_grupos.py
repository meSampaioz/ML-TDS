from privacy_ml.dados_sinteticos import gerar_dados_sinteticos

dados = gerar_dados_sinteticos()

grupos = dados.groupby(
    ["categoria", "canal", "plano"]
).size()

print(grupos)
print("\nMenor grupo:", grupos.min())

print(dados.head())