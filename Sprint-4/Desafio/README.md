<h1>Desafios de Docker e Python</h1>

<h2>Desafio: Carguru - Geração Aleatória de Modelos de Carros</h2>

<p><strong>Objetivo</strong>: Criar um container Docker que execute um script Python para gerar aleatoriamente um modelo de carro e exibi-lo na saída.</p>
<a href="/Sprint-4/Desafio/Carguru/carguru.py"> Arquivo carguru python</a> <br>
<a href="/Sprint-4/Desafio/Carguru/Dockerfile"> Dockerfile</a> <br>

<h3>Estrutura do Projeto</h3>

<ul>
    <li><strong>carguru.py</strong>: Script Python que utiliza a biblioteca <code>random</code> para selecionar e exibir aleatoriamente um modelo de carro.</li>
    <li><strong>Dockerfile</strong>: Arquivo de configuração para criação da imagem Docker.</li>
</ul>

<h3>1. Implementação do Script Python</h3>

<p>O script <code>carguru.py</code> realiza os seguintes passos:</p>
<ol>
    <li>Utiliza a biblioteca <code>random</code> para selecionar um modelo de carro da lista <code>carros</code>.</li>
    <li>Exibe o modelo de carro selecionado.</li>
</ol>

<h3>2. Criação da Imagem Docker</h3>

<p>O <strong>Dockerfile</strong> foi configurado com as seguintes instruções:</p>

<ul>
    <li><strong>Imagem base</strong>: <code>FROM python</code></li>
    <li><strong>Define o diretório de trabalho</strong>: <code>WORKDIR /app</code></li>
    <li><strong>Copia o script Python para o container</strong>: <code>COPY carguru.py .</code></li>
    <li><strong>Comando para executar o script Python</strong>: <code>CMD ["python", "carguru.py"]</code></li>
</ul>

<h3>3. Construção e Execução da Imagem Docker</h3>

<p>Para construir a imagem, executei:</p>

<pre><code>docker build -t carguru-image .</code></pre>

<p><strong>Exemplo de Construção da Imagem</strong></p>
<img src="/Sprint-4/Evidencias/build_carguru.png" width="500px" alt="Construção da imagem Carguru">

<p>Em seguida, executei o container:</p>

<pre><code>docker run --name carguru-container carguru-image</code></pre>

<p><strong>Exemplo de Execução do Container</strong></p>
<img src="/Sprint-4/Evidencias/teste_carguru.png" width="700px" alt="Execução do container com base na imagem Docker">

<p>Para visualizar containers que já finalizaram a execução:</p>

<pre><code>docker ps -a</code></pre>

<p><strong>Exemplo de Listagem de Containers Finalizados</strong></p>
<img src="/Sprint-4/Evidencias/execução_carguru.png" width="500px" alt="Teste de execução do container">

<p>Para responder a pergunta da <strong>Segunda Etapa</strong> e mostrar que era possivel reutilizar o mesmo container e gerar novos resultados:</p>

<pre><code>docker start carguru-container</code></pre>

<img src="/Sprint-4/Evidencias/execuçoes_carguru.png" width="500px" alt="Teste de execuções do container">

<h2>Desafio: Mascaramento de Dados com SHA-1</h2>

<p><strong>Objetivo</strong>: Criar um script em Python que receba strings de entrada e retorne o hash SHA-1 da string, executando-o dentro de um container Docker.</p>
<a href="/Sprint-4/Desafio/Criptografia SHA-1/mascarar.py"> Arquivo de mascaramento python</a> <br>
<a href="/Sprint-4/Desafio/Criptografia SHA-1/Dockerfile"> Dockerfile</a> <br>

<h3>Estrutura do Projeto</h3>

<ul>
    <li><strong>mascarar.py</strong>: Script Python que recebe a string, gera o hash SHA-1 e exibe o resultado.</li>
    <li><strong>Dockerfile</strong>: Arquivo de configuração para criação da imagem Docker.</li>
</ul>

<h3>1. Implementação do Script Python</h3>

<p>O script <code>mascarar.py</code> realiza os seguintes passos:</p>
<ol>
    <li>Recebe uma string via input.</li>
    <li>Gera o hash da string usando o algoritmo SHA-1.</li>
    <li>Exibe o hash em formato hexadecimal com o método <code>hexdigest()</code>.</li>
</ol>

<p><strong>Código do Script (mascarar.py)</strong></p>

<pre><code>
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
</code></pre>
<h3>2. Criação da Imagem Docker</h3>
<p>O <strong>Dockerfile</strong> foi configurado com as seguintes instruções:</p>

<ul>
    <li><strong>Imagem base</strong>: <code>FROM python</code></li>
    <li><strong>Define o diretório de trabalho</strong>: <code>WORKDIR /app</code></li>
    <li><strong>Copia o script Python para o container</strong>: <code>COPY mascarar.py .</code></li>
    <li><strong>Comando para executar o script Python</strong>: <code>CMD ["python", "mascarar.py"]</code></li>
</ul>

<h3>3. Construção e Execução da Imagem Docker</h3>

<p>Para construir a imagem, execute:</p>

<pre><code>docker build -t mascarar-dados .</code></pre>

<p><strong>Construção da Imagem</strong></p>
<img src="/Sprint-4/Evidencias/build_mascara_dados.png" width="500px" alt="Criação da imagem mascaramento">

<p>Em seguida, iniciei o container com o modo interativo:</p>

<pre><code>docker run -it --name mascara-container mascarar-dados</code></pre>

<p><strong>Exemplo de Erro ao Executar sem Interatividade</strong></p>
<img src="/Sprint-4/Evidencias/erro_mascarar_dados.png" width="500px" alt="Teste do mascaramento">

<p>Para reutilizar o container e gerar novos hashes:</p>

<pre><code>docker start -i mascara-container</code></pre>
<img src="/Sprint-4/Evidencias/start_mascara.png" width="500px" alt="Solução do mascaramento">
<p><strong>Exemplo de Uso</strong></p>
<img src="/Sprint-4/Evidencias/teste_container_mascara.png" width="500px" alt="Solução do mascaramento">

<h3>Conclusão</h3> 
<p>Esses desafios foram fundamentais para reforçar o aprendizado em Docker e Python. A prática de criar containers para executar scripts mostrou como é fácil e eficiente isolar aplicações, garantindo que funcionem de forma consistente em qualquer ambiente.</p> <p>Além disso, aprendi a importância de automatizar processos e a utilizar ferramentas modernas, o que facilita o desenvolvimento e aumenta a segurança dos dados. Essa experiência é um passo importante para projetos futuros mais complexos e escaláveis.</p>






