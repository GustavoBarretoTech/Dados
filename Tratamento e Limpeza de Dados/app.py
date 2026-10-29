import pandas as pd

df = pd.read_csv("tab.csv")

def padronizar(col):
    if col.dtype in ["object", "string"]:
        col = col.str.strip()
        col = col.where(col != "", pd.NA)

        if col.name != "Data":
            col = col.str.title()
        else:
            col = pd.to_datetime(col, errors='coerce', format="mixed", dayfirst=True)

    return  col

df = df.apply(padronizar) # Limpar colunas de texto e padronizar

# ComNulos = df.isna().any() # Colunas com nulos
# ComNulos = ComNulos[ComNulos].index.tolist() # Nome das colunas com nulos

#tratar as colunas com nulos
#tratando Quantidade
df['Quantidade'] = pd.to_numeric(df['Quantidade'], errors='coerce')
moda = df['Quantidade'].median()
df['Quantidade'] = df['Quantidade'].fillna(moda)

#tratando Desconto_Pct
df['Desconto_Pct'] = df['Desconto_Pct'].fillna(0)

#tratando Idade_Cliente
mediana = df['Idade_Cliente'].median()
df['Idade_Cliente'] = df['Idade_Cliente'].fillna(mediana)

#tratando Forma_Pagamento
moda = df['Forma_Pagamento'].mode()[0]
df['Forma_Pagamento'] = df['Forma_Pagamento'].fillna(moda)

#atualizando Valor_Total
df['Valor_Total'] = df['Preco_Unitario'] * df['Quantidade'] * (1 - df['Desconto_Pct']/100)
print(df.isna().sum()) #Colunas limpas

#Criar a tabela limpa
df.to_csv("Tabela_Limpa.csv")
