# Receba o preço atual e a média mensal de um produto.
# Calcule e mostre o novo preço sabendo que:
#     Venda Mensal        Preço Atual         Preço Novo
#     < 500               < 30                +10%
#     >= 500 e < 1000     >= 30 e < 80        +15%
#     >= 1000             >= 80               -5%
#     Obs.: para outras condições, preço novo será igual ao preço atual

print("Bem vindo ao Calculo de Produto")

precoAtual: float = float(input("Digite o preço atual do produto: R$ "))
vendaMensal: int = int(input("Digite a média mensal de quantidade vendida: "))

precoNovo: float


if vendaMensal < 500 and precoAtual < 30:
    precoNovo = precoAtual * 1.10

elif 500 <= vendaMensal < 1000 and 30 <= precoAtual < 80:
    precoNovo = precoAtual * 1.15

elif vendaMensal >= 1000 and precoAtual >= 80:
    precoNovo = precoAtual * (1 - 0.05)
else:
    precoNovo = precoAtual

print(f"Preço Atual: R$ {precoAtual:.2f}")
print(f"Venda Mensal: {vendaMensal}")
print(f"Novo Preço: R$ {precoNovo:.2f}")