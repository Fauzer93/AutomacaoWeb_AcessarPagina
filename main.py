from playwright.sync_api import sync_playwright
import time
import os
import dotenv
from dotenv import load_dotenv

# Carregar variáveis do arquivo .env
load_dotenv(override=True)

# Variáveis do arquivo .env no ambiente
email_secrets = os.getenv("email_linkedin")
senha_secrets = os.getenv("senha_linkedin")

with sync_playwright() as p:
    navegador = p.chromium.launch(headless=False)
    pagina = navegador.new_page()
    # informar o link da pagina que será acessado
    pagina.goto("https://www.linkedin.com/home")
    # Clica no botão "Entrar"
    pagina.locator('xpath=//*[@id="main-content"]/section[1]/div/div/a').click()
    # Insere e-mail no campo
    pagina.fill('xpath=//*[@id="username"]', email_secrets)
    time.sleep(3)
    # Insere senha no campo
    pagina.fill('xpath=//*[@id="password"]',  senha_secrets)
    time.sleep(3)
    # Após o preenchimento das informações de login será clicado no botão "Entrar"
    pagina.locator('xpath=//*[@id="organic-div"]/form/div[3]/button').click()

    time.sleep(60)

