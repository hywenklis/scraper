# Projeto Integrador III-A (CESMAC) - Raspagem e Armazenamento de Filmes

Este repositório contém um projeto desenvolvido para o Projeto Integrador III-A (CESMAC), cujo objetivo é realizar a raspagem de informações sobre filmes de uma página web e armazená-las em um banco de dados. O código aqui presente utiliza Python, junto com as bibliotecas `requests`, `BeautifulSoup` e `sqlalchemy`, para atingir esse fim.

## Pré-requisitos

Antes de executar o código, certifique-se de ter as seguintes dependências instaladas:

- Python 3.x
- `requests`
- `beautifulsoup4`
- `sqlalchemy`

Você pode instalar as dependências executando:

```pip install requests beautifulsoup4 sqlalchemy```


## Como funciona

O script realiza os seguintes passos:

1. Envia uma solicitação GET para a página web onde os filmes estão listados.
2. Utiliza BeautifulSoup para analisar o HTML da página e extrair informações sobre os filmes, como título, URL da imagem, descrição e URL do vídeo do YouTube.
3. Conecta-se a um banco de dados SQL (PostgreSQL) usando sqlalchemy.
4. Cria uma tabela chamada `movies` no banco de dados, se ela ainda não existir, com colunas para armazenar as informações dos filmes.
5. Itera sobre os elementos HTML que contêm as informações dos filmes, extrai essas informações e insere no banco de dados.
6. Registra mensagens de log para acompanhar o progresso do processo.

## Como usar

1. Clone este repositório:

```git clone https://github.com/seu-usuario/seu-repositorio.git```


2. Navegue até o diretório clonado:

```cd seu-repositorio```


3. Execute o script Python:

```python scraper.py```


Certifique-se de adaptar o nome do arquivo Python conforme necessário.

## Nota

Este projeto foi desenvolvido como parte do Projeto Integrador III-A e pode ser adaptado ou expandido para atender a outros requisitos ou necessidades específicas do projeto.

Para mais informações, entre em contato com o autor do repositório.

--- 



