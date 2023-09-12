#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

void error(const char *msg) {
    perror(msg);
    exit(1);
}

int main(int argc, char *argv[]) {
    int sockfd, newsockfd, portno;
    socklen_t clilen;
    char buffer[1024];
    struct sockaddr_in serv_addr, cli_addr;
    int n;

    if (argc < 2) {
        fprintf(stderr, "Uso: %s <porta>\n", argv[0]);
        exit(1);
    }

    sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0)
        error("Erro ao abrir socket.");

    bzero((char *) &serv_addr, sizeof(serv_addr));
    portno = atoi(argv[1]);

    serv_addr.sin_family = AF_INET;
    serv_addr.sin_addr.s_addr = INADDR_ANY;
    serv_addr.sin_port = htons(portno);

    if (bind(sockfd, (struct sockaddr *) &serv_addr, sizeof(serv_addr)) < 0)
        error("Erro ao realizar bind.");

    listen(sockfd, 5);
    clilen = sizeof(cli_addr);

    while (1) {
        newsockfd = accept(sockfd, (struct sockaddr *) &cli_addr, &clilen);
        if (newsockfd < 0)
            error("Erro ao aceitar conexão.");

        bzero(buffer, sizeof(buffer));
        n = read(newsockfd, buffer, sizeof(buffer) - 1);
        if (n < 0)
            error("Erro ao ler do socket.");

        printf("Solicitação HTTP recebida:\n%s\n", buffer);

        // Construa a resposta JSON com informações de 10 pessoas
        const char *json_response = "["
            "{\"nome\": \"João\", \"idade\": 32, \"endereco\": \"Rua A, Cidade A\", \"telefone\": \"(11) 1234-5678\", \"cpf\": \"123.456.789-01\"},"
            "{\"nome\": \"Maria\", \"idade\": 28, \"endereco\": \"Rua B, Cidade B\", \"telefone\": \"(22) 9876-5432\", \"cpf\": \"987.654.321-02\"},"
            "{\"nome\": \"Pedro\", \"idade\": 45, \"endereco\": \"Rua C, Cidade C\", \"telefone\": \"(33) 5678-1234\", \"cpf\": \"567.123.890-03\"},"
            "{\"nome\": \"Ana\", \"idade\": 29, \"endereco\": \"Rua D, Cidade D\", \"telefone\": \"(44) 4321-8765\", \"cpf\": \"432.567.901-04\"},"
            "{\"nome\": \"Carlos\", \"idade\": 38, \"endereco\": \"Rua E, Cidade E\", \"telefone\": \"(55) 8765-4321\", \"cpf\": \"876.890.123-05\"},"
            "{\"nome\": \"Julia\", \"idade\": 27, \"endereco\": \"Rua F, Cidade F\", \"telefone\": \"(66) 9870-1234\", \"cpf\": \"987.123.456-06\"},"
            "{\"nome\": \"Lucas\", \"idade\": 35, \"endereco\": \"Rua G, Cidade G\", \"telefone\": \"(77) 5432-8765\", \"cpf\": \"543.901.234-07\"},"
            "{\"nome\": \"Isabel\", \"idade\": 42, \"endereco\": \"Rua H, Cidade H\", \"telefone\": \"(88) 1234-5678\", \"cpf\": \"123.890.567-08\"},"
            "{\"nome\": \"Rafael\", \"idade\": 31, \"endereco\": \"Rua I, Cidade I\", \"telefone\": \"(99) 5678-1234\", \"cpf\": \"567.234.890-09\"},"
            "{\"nome\": \"Camila\", \"idade\": 26, \"endereco\": \"Rua J, Cidade J\", \"telefone\": \"(00) 8765-4321\", \"cpf\": \"876.567.123-10\"}"
        "]";

        // Configurar os cabeçalhos da resposta HTTP
        const char *response = "HTTP/1.1 200 OK\r\n"
                               "Content-Type: application/json\r\n"
                               "Content-Length: ";

        char content_length[20];
        sprintf(content_length, "%ld", strlen(json_response));

        // Concatenar o cabeçalho Content-Length
        strcat(response, content_length);
        strcat(response, "\r\n\r\n");

        // Concatenar o JSON de resposta
        strcat(response, json_response);

        n = write(newsockfd, response, strlen(response));
        if (n < 0)
            error("Erro ao escrever no socket.");

        close(newsockfd);
    }

    close(sockfd);
    return 0;
}
