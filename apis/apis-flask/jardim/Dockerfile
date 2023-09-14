# Use a imagem base Python 3.11
FROM python:3.11

# Atualize o sistema e instale o Git
RUN apt-get update && apt-get install -y git

# Defina o diretório de trabalho no contêiner
WORKDIR /app

# Clone o repositório Git
RUN git clone https://github.com/julianvitor/playground.git

# Copie o script de inicialização para o contêiner
COPY /app/playground/apis/apis-flask/jardim/startup.sh /app/startup.sh

# Torne o script de inicialização executável
RUN chmod +x /app/startup.sh

# Exponha a porta em que o aplicativo Flask está sendo executado (se necessário)
EXPOSE 5000

# Comando para executar o script de inicialização
CMD ["/bin/bash", "/app/startup.sh"]
