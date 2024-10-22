# Flask Color Palette Picker

## Projeto em Andamento 🚧

Este projeto está em desenvolvimento contínuo. Estamos aprimorando a aplicação para melhorar o desempenho do processamento de imagens e a geração de paletas de cores usando o algoritmo KMeans.

Fique atento para novas atualizações e funcionalidades futuras!

## Objetivo

Este projeto Flask foi desenvolvido para receber uma imagem e gerar uma paleta de cores utilizando o algoritmo **KMeans**. Ele é baseado na estrutura **Onio**, inspirada no [cookiecutter-python-flask-clean-architecture](https://github.com/microsoft/cookiecutter-python-flask-clean-architecture).

## Funcionalidades

- Upload de imagens pelo usuário.
- Processamento da imagem para extrair cores dominantes.
- Exibição de uma paleta de cores gerada pelo algoritmo KMeans.

## Estrutura do Projeto

Este projeto segue a estrutura **Onio**, organizada conforme o modelo Clean Architecture:

```
root/
├── Makefile
├── requirements.txt
├── README.md
├── src/
│   ├── application/
│   │   ├── interfaces/
│   │   │   ├── repositories/
│   │   │   │   └── user_repository.py
│   │   ├── services/
│   │   │   ├── picture_service.py
│   │   │   └── user_service.py
│   ├── core/
│   │   ├── config/
│   │   │   ├── .env
│   │   │   └── example.env
│   │   ├── database.py
│   │   ├── di.py
│   │   └── startup.py
│   ├── domains/
│   │   ├── picture.py
│   │   └── user.py
│   ├── infra/
│   │   ├── models/
│   │   │   ├── picture_model.py
│   │   │   └── user_model.py
│   │   └── repositories/
│   │       └── user_repository.py
│   ├── web/
│   │   ├── controllers/
│   │   └── interfaces/
│   │       └── services/
└── tests/
    ├── integration/
    │   ├── config.py
    │   └── database_test.py
    ├── unit/
    │   ├── core/
    │   │   └── di_test.py
    │   ├── domains/
    │   │   └── picture_test.py

```

## Principais Diretórios

- **src/application/**: Contém a lógica de negócio, incluindo interfaces, repositórios e serviços, como o processamento de imagens.
- **src/core/config/**: Contém arquivos de configuração, incluindo variáveis de ambiente, como o arquivo `.env` e `example.env`.
- **src/domains/**: Contém as definições das entidades do domínio, como `picture` e `user`.
- **src/infra/**: Contém os modelos de banco de dados e repositórios relacionados à infraestrutura.
- **src/web/**: Contém os controladores e interfaces que expõem a lógica de negócio via rotas da API.
- **tests/**: Contém os testes automatizados do projeto, organizados em testes de integração e de unidade.

## Configuração de Variáveis de Ambiente

Na pasta `src/core/config`, existe um arquivo `example.env` que contém as variáveis de ambiente necessárias para a configuração do banco de dados NoSQL (MongoDB). 

Você deve copiar este arquivo e renomeá-lo para `.env`:

```bash
cp src/core/config/example.env src/core/config/.env
```

No arquivo `.env`, você deverá configurar os seguintes valores:

```env
MONGO_URI=your_mongo_connection_string
MONGO_DB_NAME=colorpalettepicker
```

- `MONGO_URI`: A URI de conexão com o MongoDB.
- `MONGO_DB_NAME`: O nome do banco de dados utilizado para armazenar os dados relacionados às paletas de cores.

## Pré-requisitos

Antes de rodar a aplicação, certifique-se de que você tem os seguintes itens instalados:

- Python 3.8 ou superior
- pip (gerenciador de pacotes do Python)
- Virtualenv (opcional, mas recomendado)
- MongoDB (deve estar rodando na máquina local ou acessível remotamente)

## Instalação

Siga as etapas abaixo para configurar e rodar a aplicação localmente.

1. Clone o repositório:

```bash
git clone https://github.com/tjusto2023/flask-color-palette-picker.git
cd flask-color-palette-picker
```

2. Crie um ambiente virtual:

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências do projeto:

```bash
pip install -r requirements.txt
```

4. Configure as variáveis de ambiente:

- Renomeie o arquivo `example.env` para `.env` e preencha as informações de conexão com o MongoDB conforme descrito acima.

## Executando a Aplicação

Para rodar a aplicação localmente, você pode usar o comando `make`:

```bash
make run
```

Isso iniciará o servidor Flask. Acesse a aplicação no navegador através do endereço:

```
http://127.0.0.1:5000
```

## Executando os Testes

Para rodar os testes automatizados, execute o comando:

```bash
make test
```

Isso iniciará os testes utilizando o **pytest** e exibirá os resultados no terminal.

## Algoritmo KMeans

A aplicação utiliza o algoritmo KMeans, que agrupa os pixels da imagem em clusters com base na similaridade das cores. O número de clusters pode ser configurado conforme a necessidade, e a saída é uma paleta de cores representando as cores dominantes da imagem fornecida.

## Licença

Desenvolvido por [tjusto2023](https://github.com/tjusto2023)