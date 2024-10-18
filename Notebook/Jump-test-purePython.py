import pandas as pd  # type: ignore
import psutil
import time

# Função para checar uso de memória
def print_memory_usage():
    process = psutil.Process()
    memory_info = process.memory_info()
    print(f"Memória usada: {memory_info.rss / (1024 * 1024):.2f} MB")

# Marcar o início do tempo
start_time = time.time()

# Definindo o caminho do arquivo CSV
file_path = r'C:\Users\vinia\OneDrive\Documentos\Testes tecnicos\Jump\Data\vendas.csv'

# Função para processar os chunks
def processar_chunk(chunk):
    # Limpando e preparando os dados (remoção de linhas com dados faltantes nas colunas principais)
    chunk_clean = chunk.dropna(subset=["Order Date", "Item Type", "Units Sold", "Unit Price", "Sales Channel"])

    # Convertendo colunas para os tipos apropriados
    chunk_clean["Units Sold"] = chunk_clean["Units Sold"].astype(int)
    chunk_clean["Unit Price"] = chunk_clean["Unit Price"].astype(float)

    # Calculando o valor da venda
    chunk_clean["valor_venda"] = chunk_clean["Units Sold"] * chunk_clean["Unit Price"]

    return chunk_clean

# Checar memória antes de iniciar o processamento
print("Memória antes do processamento:")
print_memory_usage()

# Leitura em partes do arquivo CSV usando chunks
chunk_size = 1000000  # Tamanho do chunk
chunks = pd.read_csv(file_path, chunksize=chunk_size, parse_dates=["Order Date", "Ship Date"])

# Processando cada chunk e acumulando os resultados
df_full = pd.concat([processar_chunk(chunk) for chunk in chunks])

# Checar memória após o processamento dos chunks
print("\nMemória após o processamento dos chunks:")
print_memory_usage()

# 1. Produto mais vendido e canal de vendas
produto_mais_vendido = df_full.groupby(["Item Type", "Sales Channel"])["Units Sold"].sum().reset_index()
produto_mais_vendido = produto_mais_vendido.sort_values(by="Units Sold", ascending=False).head(1)
print(f"Produto mais vendido:\nProduto: {produto_mais_vendido.iloc[0]['Item Type']}, Canal: {produto_mais_vendido.iloc[0]['Sales Channel']}, Total vendido: {produto_mais_vendido.iloc[0]['Units Sold']} unidades")

# 2. País e região com maior volume de vendas
vendas_por_pais_regiao = df_full.groupby(["Country", "Region"])["valor_venda"].sum().reset_index()
pais_regiao_maior_venda = vendas_por_pais_regiao.sort_values(by="valor_venda", ascending=False).head(1)
print(f"\nPaís e região com maior volume de vendas:\nPaís: {pais_regiao_maior_venda.iloc[0]['Country']}, Região: {pais_regiao_maior_venda.iloc[0]['Region']}, Total de vendas: R${pais_regiao_maior_venda.iloc[0]['valor_venda']}")

# 3. Média de vendas mensais por produto
df_full["Year"] = df_full["Order Date"].dt.year
df_full["Month"] = df_full["Order Date"].dt.month
vendas_mensais = df_full.groupby(["Item Type", "Year", "Month"])["valor_venda"].sum().reset_index()
media_vendas_mensais = vendas_mensais.groupby("Item Type")["valor_venda"].mean().reset_index()
media_vendas_mensais = media_vendas_mensais.sort_values(by="valor_venda", ascending=False)

print("\nMédia de vendas mensais por produto:")
for idx, row in media_vendas_mensais.iterrows():
    print(f"Produto: {row['Item Type']}, Média mensal: R${row['valor_venda']:.2f}")

# Medir o tempo total
end_time = time.time()
execution_time = end_time - start_time
print(f"\nTempo total de execução: {execution_time:.2f} segundos")

# Checar memória no final do processamento
print("\nMemória no final do processamento:")
print_memory_usage()