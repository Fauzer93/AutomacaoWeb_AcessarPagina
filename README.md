Automação com Playwright

Este projeto demonstra como configurar e utilizar o Playwright para automação de testes ou outras tarefas automatizadas em um ambiente Python. 
Abaixo estão as instruções para configurar o ambiente e executar o código.

Requisitos
  Python 3.8 ou superior
  Pip (gerenciador de pacotes do Python)


Passos para Configuração
1. Criação do Arquivo Principal
    Crie um arquivo Python para armazenar o código da automação. O arquivo pode ter qualquer nome, mas deve terminar com a extensão .py.
Por exemplo: main.py

3. Instalação do Playwright
    Instale a biblioteca python-playwright usando o pip. Isso pode ser feito diretamente no terminal ou dentro do interpretador de código que você está utilizando.
pip install python-playwright

3. Importação da Biblioteca Playwright
    No seu arquivo principal (como main.py), você precisa importar a biblioteca Playwright. Isso permite que você utilize as funções do Playwright para automação.
from playwright.sync_api import sync_playwright

4. Configuração de Variáveis de Ambiente
    Para manter informações sensíveis (como credenciais) fora do código principal, é recomendável usar um arquivo .env para armazenar variáveis de ambiente.

4.1 Criação do Arquivo .env
    Crie um arquivo .env na raiz do seu projeto. Dentro desse arquivo, defina suas variáveis de ambiente:
USER=meu_usuario
PASSWORD=minha_senha

4.2 Instalação da Biblioteca python-dotenv
    Instale a biblioteca python-dotenv para carregar as variáveis do arquivo .env no seu código Python.
pip install python-dotenv

4.3 Carregamento das Variáveis de Ambiente no Código
    No arquivo Python, importe e carregue as variáveis do arquivo .env:
from dotenv import load_dotenv
import os
# Carrega as variáveis de ambiente do arquivo .env
load_dotenv()
# Acessa uma variável de ambiente
user = os.getenv('USER')
password = os.getenv('PASSWORD')


Execução do Código
    Após configurar o ambiente e o código, execute o arquivo principal (main.py) para iniciar a automação:
python main.py


Observações:
Certifique-se de não compartilhar o arquivo .env publicamente, pois ele pode conter informações sensíveis.
O Playwright permite automatizar navegadores, realizar testes ou scraping de forma eficiente. 
Este projeto é apenas um ponto de partida; explore a documentação do Playwright para funcionalidades avançadas.
