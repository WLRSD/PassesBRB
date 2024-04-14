# Abre o arquivo em modo de leitura e escrita, especificando a codificação 'utf-8'
with open('itinerárioSAM.txt', 'r+', encoding='utf-8') as arquivo:
    # Lê todas as linhas do arquivo
    linhas = arquivo.readlines()
    
    # Move o cursor para o início do arquivo
    arquivo.seek(0)
    
    # Loop sobre cada linha do arquivo
    for i, linha in enumerate(linhas):
        # Remove espaços em branco no início e no final da linha
        linha = linha.strip()
        # Verifica se a linha é ímpar (começando do 0)
        if i % 2 == 0:
            # Se for ímpar, insere uma vírgula ou ponto e vírgula
            arquivo.write(linha + ';')
        else:
            # Se for par, insere uma quebra de linha
            arquivo.write(linha + '\n')

