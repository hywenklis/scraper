import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine, Table, MetaData, Column, String, Integer
import logging

# Configurando os logs
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_movie_info(movie_element):
    title = movie_element.get_text(strip=True)
    img_element = movie_element.find_next_sibling('div', class_='wp-block-image')
    img_url = None
    if img_element and 'srcset' in img_element.find('img').attrs:
        srcset = img_element.find('img')['srcset']
        img_url = srcset.split(' ')[0] if 'jpg' in srcset.split(' ')[0] else None

    description_element = movie_element.find_next_sibling('p')
    description = description_element.get_text(strip=True) if description_element else None

    youtube_element = movie_element.find_next_sibling('figure', class_='wp-block-embed-youtube')
    youtube_url = youtube_element.find('iframe')['src'] if youtube_element else None

    return title, img_url, description, youtube_url


def insert_movie_to_database(connection, movie_info):
    title, img_url, description, youtube_url = movie_info
    if img_url and description and youtube_url:
        connection.execute(movies_table.insert().values(title=title, img_url=img_url, description=description, youtube_url=youtube_url))
        logger.info("Filme '%s' inserido no banco de dados", title)
    else:
        logger.info("Ignorando '%s' porque falta alguma informação", title)


# Fazendo a requisição para a página
link = "https://nahoradoocio.lowlevel.com.br/2020/12/22/15-filmes-para-assistir-no-natal/"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

logger.info("Enviando solicitação GET para %s", link)
response = requests.get(link, headers=headers)

# Criando o objeto BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Encontrando os elementos da página que contêm os títulos e descrições dos filmes
movie_elements = soup.select('h2')

# Conectando ao banco de dados SQL
engine = create_engine('postgresql://scraper:password@localhost:5432/scraper-db')

# Criando a tabela de filmes, se ela não existir
metadata = MetaData()
movies_table = Table(
    'movies', metadata,
    Column('id', Integer, primary_key=True),
    Column('title', String),
    Column('img_url', String),
    Column('description', String),
    Column('youtube_url', String)
)
metadata.create_all(engine)
logger.info("Tabela 'movies' criada")

# Inserindo os dados raspados na tabela de filmes
with engine.connect() as connection:
    for movie_element in movie_elements:
        movie_info = get_movie_info(movie_element)
        insert_movie_to_database(connection, movie_info)
        connection.commit()

logger.info("Finalizado a raspagem e armazenamento dos filmes")
