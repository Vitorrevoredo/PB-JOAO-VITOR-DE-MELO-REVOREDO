<h1>README - Sprint da utilização do s3 com python</h1>
  
  <h2>Objetivos da Sprint</h2>
<ul>
    <li>Praticar comandos python </li>
    <li>Utilizar o serviço s3 da AWS para criação de um ambiente de armazenamento de objetos<li>
    <li>Explorar o tratamento de dados para simular diferentes execuções de script.</li>
</ul>

  
  <h1><strong>Exercicicio</strong> Projeto de Hospedagem de Site Estático no Amazon S3</h1>

  <p>Este exercício teve como objetivo a hospedagem de um site estático na Amazon Web Services (AWS) usando o serviço <strong>Amazon S3</strong>. O site consiste em um simples <code>index.html</code> e um documento de erro personalizado <code>404.html</code>. A hospedagem é configurada para permitir acesso público, com um documento de índice padrão e um documento de erro para páginas não encontradas.</p>

  <h2>Etapas de Configuração</h2>

  <h3>1. Criando um Bucket no S3</h3>
  <ul>
      <li>No Console AWS, busquei pelo serviço <strong>S3</strong> e cliquei em <strong>Create bucket</strong>.</li>
      <li>Defini um nome único para o bucket <code>exercicios3.com</code> e selecionei a região (recomenda-se <strong>US East (N. Virginia)</strong>).</li>
      <li>Cliquei em <strong>Create</strong> para criar o bucket.</li>
  </ul>
    <img src="/Sprint-5/Exercicios/Evidencias/selecionando_regiao_s3.png" width="500px" alt=""> <br>
    <img src="/Sprint-5/Exercicios/Evidencias/criacao_bucket.png" width="500px" alt=""> <br>


  <h3>2. Habilitar a Hospedagem de Site Estático</h3>
  <ul>
      <li>No Console AWS, fui até o serviço <strong>S3</strong> e selecionei o bucket criado.</li>
      <li>Fui para a aba <strong>Properties</strong> e, na seção <strong>Static website hosting</strong>, cliquei em <strong>Edit</strong>.</li>
      <li>Marquei a opção <strong>Use this bucket to host a website</strong>.</li>
      <li>Defini o <strong>Index document</strong> como <code>index.html</code>.</li>
      <li>(Opcional) Defini o <strong>Error document</strong> como <code>404.html</code>.</li>
      <li>Salvei as alterações.</li>
  </ul>
      <img src="/Sprint-5/Exercicios/Evidencias/criacao_hospedagem.png" width="500px" alt=""> <br>
     
  <h3>3. Editar as Configurações de Bloqueio de Acesso Público</h3>
  <ul>
      <li>No Console AWS, fui até a aba <strong>Permissions</strong> e cliquei em <strong>Edit</strong> nas configurações de <strong>Block public access</strong>.</li>
      <li>Desmarquei <strong>Block all public access</strong> e cliquei em <strong>Save changes</strong>.</li>
  </ul>
   <img src="/Sprint-5/Exercicios/Evidencias/endpoint_site.png" width="500px" alt=""> <br>
   <img src="/Sprint-5/Exercicios/Evidencias/teste_endpoint.png" width="500px" alt=""> <br>


  <h3>4. Adicionar Política de Acesso Público ao Bucket</h3>
  <ul>
      <li>Na aba <strong>Permissions</strong> do bucket, cliquei em <strong>Edit</strong> na seção <strong>Bucket Policy</strong>.</li>
      <li>Inseri a seguinte política de bucket para conceder acesso público de leitura:</li>
  </ul>
<img src="/Sprint-5/Exercicios/Evidencias/criando_politica.png" width="500px" alt=""> <br>
<img src="/Sprint-5/Exercicios/Evidencias/alterando_politica.png" width="500px" alt=""> <br>


  <pre><code>
{
  "Version": "2012-10-17",
  "Statement": [
      {
          "Sid": "PublicReadGetObject",
          "Effect": "Allow",
          "Principal": "*",
          "Action": [
              "s3:GetObject"
          ],
          "Resource": [
              "arn:aws:s3:::exercicios3.com/*"
          ]
      }
  ]
}
  </code></pre>

  <p>Substituí <code>Bucket-Name</code> por <code>exercicios3.com</code>.</p>

  <h3>5. Fazer Upload dos Arquivos do Site</h3>
  <ul>
      <li>Na página do bucket, cliquei na aba <strong>Objects</strong> e selecionei <strong>Upload</strong>.</li>
      <li>Arrastei e soltei os arquivos <code>index.html</code> e <code>404.html</code> no campo de upload.</li>
      <li>Cliquei em <strong>Upload</strong> para enviar os arquivos para o S3.</li>
  </ul>
  <img src="/Sprint-5/Exercicios/Evidencias/erro_html.png" width="500px" alt=""> <br>
  <img src="/Sprint-5/Exercicios/Evidencias/configurando_arquivos.png" width="500px" alt=""> <br>
 <img src="/Sprint-5/Exercicios/Evidencias/upload_arquivos.png" width="500px" alt=""> <br>


  <h3>6. Testar o Acesso Público ao Site</h3>
  <ul>
      <li>Após a conclusão do upload, a URL pública do site estará disponível na seção <strong>Static website hosting</strong>, onde a URL do endpoint estará visível.</li>
      <li>Acessei a URL do site no navegador para testar a hospedagem.</li>
      <li>Em caso de erro 404, o arquivo <code>404.html</code> será exibido conforme configurado.</li>
     <img src="/Sprint-5/Exercicios/Evidencias/executando_site.png" width="500px" alt=""> <br>

  </ul>

  <h3>7. Site funcionando </h3>
  <p>Fiz os testes do site estático e exclui o bucket </p>
       <img src="/Sprint-5/Exercicios/Evidencias/excluindo_objetos.png" width="500px" alt=""> <br>
     <img src="/Sprint-5/Exercicios/Evidencias/excluindo_bucket.png" width="500px" alt=""> <br>
     <img src="/Sprint-5/Exercicios/Evidencias/conclusao_bucket.png" width="500px" alt=""> <br>

  <h2>Conclusão</h2>
  <p>Após completar estas etapas, o site estará hospedado no Amazon S3 e acessível publicamente. O serviço S3 permite que você armazene e entregue conteúdo estático de maneira altamente escalável, e sua integração com outros serviços da AWS pode permitir funcionalidades avançadas, como distribuição de conteúdo através do Amazon CloudFront ou análise de tráfego através do AWS CloudWatch.</p>


<h2>Certificados</h2>
<p>Concluí cursos específicos para aprimorar meus conhecimentos em Docker e Python, essenciais para o desenvolvimento desta Sprint e o curso em Aws, que anexei o certificado.</p>
<ul>
    <li>=<a href="/Sprint-5/Certificados">Certificado AWS</a></li>
</ul>
<hr>

<h2>Comentários Finais</h2> 
<p>A Sprint proporcionou um aprendizado significativo na manipulação, análise de dados e armazenamento com AWS s3, destacando a importância de tratar erros comuns, como inconsistências em arquivos CSV. A prática reforçou a necessidade de validar dados antes do processamento e explorar estratégias eficientes para resolução de problemas. Esses conhecimentos são essenciais para garantir a integridade e qualidade em projetos futuros de ciência de dados.</p>