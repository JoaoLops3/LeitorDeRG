import matplotlib
matplotlib.use('Agg')  # Força backend sem interface gráfica
import matplotlib.pyplot as plt

# Dados coletados
threads = [1, 2, 4]
tempos = [3.10, 3.20, 2.35]  # Tempos em segundos

# Criar o gráfico
plt.figure(figsize=(10, 6))
plt.bar(threads, tempos, color='skyblue')

# Adicionar rótulos e título
plt.xlabel('Número de Threads')
plt.ylabel('Tempo de Execução (segundos)')
plt.title('Tempo de Execução vs. Número de Threads')

# Adicionar valores acima das barras
for i, v in enumerate(tempos):
    plt.text(threads[i], v + 0.1, f'{v:.2f}s', ha='center')

# Salvar o gráfico
plt.savefig('tempo_execucao.png')
# plt.show()  # Removido para evitar erro de interface gráfica 