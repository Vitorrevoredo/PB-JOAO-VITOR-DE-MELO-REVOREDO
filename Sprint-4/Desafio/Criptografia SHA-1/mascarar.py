import hashlib

while True:
    # Recebe uma string do usuário
    string_entrada = input("Digite uma palavra para mascarar (ou 'exit' para encerrar o programa): ")

    if string_entrada.lower() == 'exit': #Quebra o loop
        print("Encerrando programa...")
        break

    else:     # Gera o hash SHA-1 da string de entrada
        hash_senha = hashlib.sha1(string_entrada.encode())
        hash_hex = hash_senha.hexdigest()
        # Imprime o hash em formato hexadecimal:
    print(f"Hash SHA-1 da string '{string_entrada}': {hash_hex}")