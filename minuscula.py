def contar_letra_a(s):
    # Converte a string para minúsculas para simplificar a contagem
    s = s.lower()
    
    # Conta a ocorrência da letra 'a'
    quantidade = s.count('a')
    
    # Verifica se há ocorrências e retorna o resultado
    if quantidade > 0:
        return True, quantidade
    else:
        return False, 0

# Entrada do usuário
entrada = input("Digite uma string para verificar a ocorrência da letra 'a': ")

# Verifica a presença da letra 'a' e obtém a quantidade
presente, quantidade = contar_letra_a(entrada)

# Exibe o resultado
if presente:
    print(f"A letra 'a' ocorre {quantidade} vez(es) na string.")
else:
    print("A letra 'a' não ocorre na string.")
