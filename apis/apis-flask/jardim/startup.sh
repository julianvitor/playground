#!/bin/bash

# Navegue até o diretório do repositório
cd /app/playground

# Atualize o código do repositório com git pull
git pull

cd /app/playground/apis/apis-flask/jardim

# Instale as dependências do Flask
pip install -r requirements.txt

# Inicie o aplicativo Flask
python app.py
