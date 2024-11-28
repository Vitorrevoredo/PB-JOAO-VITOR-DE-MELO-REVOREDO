 <h1>Resolvendo Problemas de Permissão no Lambda</h1>
  <p>
  Sprint passada como tive um problema de acesso com o aws CLI já imaginava que o erro de permissão fosse algo relacionado ao IAM e li a documentação para tentar solucionar o problema pois durante a execução da minha função Lambda, encontrei o seguinte erro:
  </p>
  <pre><strong>AccessDeniedException: User: arn:aws:sts::123456789012:assumed-role/role-name/lambda-function-name is not authorized to perform: s3:GetObject on resource: arn:aws:s3:::bucket-name</strong></pre>
  <p>
    Após pesquisar bastante, descobri que a função estava configurada com a política padrão <code>AWSLambdaBasicExecutionRole</code>. Essa política permite apenas gravar logs no CloudWatch e, por isso, não inclui permissões para acessar buckets do S3, resultando no erro ao tentar acessar os objetos.
  </p>

  <h2>Solução</h2>

  <p>
    Para resolver, realizei as seguintes etapas:
  </p>
  <ol>
    <li>Acessei o console do <strong>IAM</strong>.</li>
    <li>Pesquisei à função Lambda chamada <code>vitor-nomes</code>.</li>
    <li>Coloquei uma role do <strong>AmazonS3FullAccess</strong> com as permissões necessárias para acessar o bucket S3.</li>
  </ol>

  <p>
    Após salvar as alterações, minha função Lambda conseguiu acessar o bucket <code>exercicio-vitor</code> sem mais problemas.
  </p>
