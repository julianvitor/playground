#!/bin/bash

# Navegue até o diretório do repositório
cd /app/playground/apis/apis-flask/jardim

# Atualize o código do repositório com git pull
git pull

# Instale as dependências do Flask
pip install -r requirements.txt

# Inicie o aplicativo Flask
python app.py
