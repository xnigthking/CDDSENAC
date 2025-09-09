import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ================== PREPARAÇÃO ==================
caminho = r'C:\Users\luis34288836\Desktop\Ciência de Dados\Visual Studio Code\Aulas Exercicios\09092025\salarios_caged.csv'
df = pd.read_csv(caminho)

def limpar_salario(coluna: pd.Series) -> pd.Series:
    return (
        coluna.astype(str)
        .str.replace("R$", "", regex=False)
        .str.replace(".", "", regex=False)
        .str.replace(",", ".", regex=False)
        .astype(float)
    )

colunas_salario = ["Salário Médio Real de Admissão", "Salário Médio Real de Desligamento"]
for col in colunas_salario:
    df[col] = limpar_salario(df[col])

# ================== ESTATÍSTICAS ==================
col = "Salário Médio Real de Admissão"
resumo = df[col].describe()

print("="*50)
print("📊 MEDIDAS DE TENDÊNCIA CENTRAL")
print(f"Média   : {resumo['mean']:.2f}")
print(f"Mediana : {df[col].median():.2f}")
print(f"Moda    : {df[col].mode()[0]:.2f}")

print("\n📉 MEDIDAS DE DISPERSÃO")
print(f"Desvio padrão : {resumo['std']:.2f}")
print(f"Mínimo        : {resumo['min']:.2f}")
print(f"Máximo        : {resumo['max']:.2f}")

print("\n📑 RESUMO COMPLETO")
print(resumo)
print("="*50)

# ================== VISUALIZAÇÕES ==================

# Histogramas
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
sns.histplot(df["Salário Médio Real de Admissão"], bins=30, kde=True, color="blue")
plt.title("Distribuição - Salário de Admissão")

plt.subplot(1, 2, 2)
sns.histplot(df["Salário Médio Real de Desligamento"], bins=30, kde=True, color="green")
plt.title("Distribuição - Salário de Desligamento")

plt.tight_layout()
plt.show()

# Boxplot comparativo (complementado com média e mediana)
plt.figure(figsize=(7, 5))
ax = sns.boxplot(data=df[colunas_salario], palette="pastel")
sns.pointplot(data=df[colunas_salario], join=False, color="red", markers="D", ci=None)

for i, coluna in enumerate(colunas_salario):
    mediana = df[coluna].median()
    plt.hlines(mediana, i-0.3, i+0.3, colors="blue", linestyles="--", label=f"Mediana {coluna}" if i == 0 else "")

plt.title("Boxplot Comparativo com Média (♦) e Mediana (--)")
plt.legend()
plt.show()

# Gráfico de Pizza - Comparação das Médias
medias = df[colunas_salario].mean()
plt.figure(figsize=(6, 6))
plt.pie(
    medias,
    labels=medias.index,
    autopct="%.2f%%",
    colors=["skyblue", "lightgreen"],
    startangle=90,
    wedgeprops={"edgecolor": "black"}
)
plt.title("Proporção das Médias Salariais")
plt.show()
