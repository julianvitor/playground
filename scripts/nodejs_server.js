const express = require('express');
const http = require('http');
const bodyParser = require('body-parser');

const app = express();
const port = 8082;

// Middleware para permitir solicitações POST com corpo JSON
app.use(bodyParser.json());

// Rota para lidar com as solicitações
app.get('/nodejs_server', (req, res) => {
    res.status(200).json({ message: 'Hello from Node.js Server!' });
});

// Crie o servidor HTTP com o Express.js
const server = http.createServer(app);

server.listen(port, () => {
    console.log(`Node.js Server listening at http://localhost:${port}`);
});
