Este programa foi desenvolvido para ser utilizado em conjunto com [Ollama](https://github.com/ollama/ollama).

Dependências:
`pip install flask ollama`

Ao carregar a página, a mensagem enviada pelo usuário é recebida pela aplicação Python que chama a função chat da biblioteca Ollama para que o modelo de linguagem seja acionado. O servidor Ollama então retorna contendo, dentre muitas outras informações, a resposta que deve ser encaminhada à página do usuário. Inicialize o ambiente virtual Python e instale as dependências. Tenha o servidor Ollama rodando e execute o programa Flask com o comando `flask --app run virtutoria`.

No momento, o programa apresenta um bug onde, após enviar o prompt, a requisição enviada ao backend recebe uma resposta de erro.
