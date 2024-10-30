# Desafio: Utilização do Docker para criação de containers em arquivos python
## Arquivo carguru.py:
<p>Para resolução da etapa fiz o downloand do arquivo como solicitado e realizei os teste para ver qual era o output da aplicação, depois
de ver como funcionava parti para criação do Dockerfile para criação do container.</p>
<h2>Estrutura do Projeto</h2>
carguru.py: script Python responsável por gerar aleatoriamento um modelo de carro para saida e exibi-lo.
Dockerfile: arquivo de configuração para criação da imagem Docker. <br>
<strong>1. Script Python</strong>
<ul>
  <li>Utiliza a biblioteca <strong>random</strong> para selecionar um dado da lista <strong>carros</strong></li>
  <li>Gera o carros aletoriamento com o metodo <strong>.choice</strong></li>
  <li>Print da saida do carro com a frase</li>
</ul>
<strong>2. Criação da Imagem Docker</strong>
<strong>Arquivo Dockerfile</strong>
<p>Para criar a imagem Docker que executará o script Python, foi criado o Dockerfile com as seguintes instruções:</p>
<ul>
<strong>Base image</strong>
<li><code>FROM python</code></li>
<strong>Define o diretório de trabalho</strong>
<li><code>WORKDIR /app</code></li>
<strong>Copia o script Python para o container</strong>
<li><code>COPY carguru.py . </code></li>
<strong>Comando para executar o script Python</strong>
<li><code>CMD ["python", "carguru.py"] </code></li>
</ul>
<h2>Construção e Execução da Imagem Docker</h2> <br>
<img src="/Sprint-4/Evidencias/build_carguru.png"  width="500px" alt="Construção da imagem Carguru">
<p>Fiz o build da imagem por meio do comando <code>docker build -t carguru-image .</code> que faz a construção da imagem do arquivo Dockerfile, utilizando a flag <strong>-t</strong> para gerar o nome da imagem e o <strong>.</strong> para usar o arquivo presente no diretório</p>
<img src="/Sprint-4/Evidencias/teste_carguru.png" width="700px" alt="Execução do container com  base na imagem docker">
<p>Em seguida, fiz a execução do container com o comando <code>docker run --name carguru-container carguru-image</code> que inicia o container docker com a flag <strong>--name</strong> que permite colocar um nome no container docker e utilizei como base a imagem gerada anteriormente.</p>
<img src="/Sprint-4/Evidencias/execução_carguru.png" width="500px" alt="Teste de execução do container">
<p>Para o teste de execução do container e verificação da contrução concluida, utilizei o comando <code>docker ps -a</code> que mostra os que já finalizaram o processo de execução, utilizando a flag -a para isso</p>
<img src="/Sprint-4/Evidencias/execuçoes_carguru.png" width="500px" alt="Resposta da Segunda Etapa">
<p>Respondendo a <strong>Segunta Etapa</strong>, sim é possivel reutilizar o mesmo container, por meio do comando <code>docker start carguru-container</code> que permite a inicialização de um container que está com estado de execução desativado, fiz alguns teste de execução e o arquivo docker gerou carros diferentes como apresentado na imagem acima. Para verificar as saidas podemos utilizar o comando <code>docker logs -f carguru-container</code> que mostra as execuções, caso queira que a cada execução mostre a saida, podemos modificar o start passando a flag <strong>-i</strong> que permite a interabilidade no processamento do container. </p>
