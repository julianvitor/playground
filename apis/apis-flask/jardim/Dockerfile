# Use a imagem base Python 3.10
FROM python:3.11

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Copie tudo
COPY . .

# Instale as dependências do Flask
RUN pip install -r requirements.txt

# Exponha a porta em que o aplicativo Flask está sendo executado
EXPOSE 5000

# Comando para executar o aplicativo Flask
CMD ["python", "app.py"]
