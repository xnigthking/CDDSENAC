import pandas as pd

# Criando o DataFrame com os dados fornecidos
df = pd.DataFrame({
    'Nome': ['Luis', 'Eduardo', None, 'Luis'],
    'Idade': ['18', '32', '25', '32'],
    'Cidade': ['Taguatinga', 'Brasilia', 'Brasília', 'Areal'],
    'Curso Favorito': ['Front-End', 'Adobe-Photoshop', 'Full-Stack', 'Photoshop']
})

# ---------------------------
# 1. Valores ausentes
# ---------------------------
print("📊 Contagem de valores ausentes em cada coluna:")
print(df.isna().sum())

# ---------------------------
# 2. Preenchimento e normalização
# ---------------------------
df['Nome'] = df['Nome'].fillna('Desconhecido')
df['Cidade'] = df['Cidade'].replace({'Brasilia': 'Brasília'})

print("\n✅ DataFrame após ajustes em 'Nome' e 'Cidade':")
print(df)

# ---------------------------
# 3. Removendo linhas com dados ausentes
# ---------------------------
df_sem_na = df.dropna()
print("\n🧹 DataFrame após remoção de linhas com valores ausentes:")
print(df_sem_na)

# ---------------------------
# 4. Removendo apenas onde 'Nome' é nulo
# ---------------------------
df_sem_na_nome = df.dropna(subset=['Nome'])
print("\n🔎 DataFrame após remoção de linhas onde 'Nome' é nulo:")
print(df_sem_na_nome)

# ---------------------------
# 5. Estatísticas rápidas (extra)
# ---------------------------
print("\n📈 Estatísticas descritivas por idade:")
print(df.assign(Idade=df['Idade'].astype(int)).groupby('Nome')['Idade'].describe())
