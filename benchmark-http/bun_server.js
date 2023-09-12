const app = Bun.serve({
    fetch(req) {
      if (req.url === 'http://localhost:8083/bun') {
        const pessoas = [
          {
            nome: 'João',
            idade: 32,
            endereco: 'Rua A, Cidade A',
            telefone: '(11) 1234-5678',
            cpf: '123.456.789-01',
          },
          {
            nome: 'Maria',
            idade: 28,
            endereco: 'Rua B, Cidade B',
            telefone: '(22) 9876-5432',
            cpf: '987.654.321-02',
          },
          {
            nome: 'Pedro',
            idade: 45,
            endereco: 'Rua C, Cidade C',
            telefone: '(33) 5678-1234',
            cpf: '567.123.890-03',
          },
          {
            nome: 'Ana',
            idade: 29,
            endereco: 'Rua D, Cidade D',
            telefone: '(44) 4321-8765',
            cpf: '432.567.901-04',
          },
          {
            nome: 'Carlos',
            idade: 38,
            endereco: 'Rua E, Cidade E',
            telefone: '(55) 8765-4321',
            cpf: '876.890.123-05',
          },
          {
            nome: 'Julia',
            idade: 27,
            endereco: 'Rua F, Cidade F',
            telefone: '(66) 9870-1234',
            cpf: '987.123.456-06',
          },
          {
            nome: 'Lucas',
            idade: 35,
            endereco: 'Rua G, Cidade G',
            telefone: '(77) 5432-8765',
            cpf: '543.901.234-07',
          },
          {
            nome: 'Isabel',
            idade: 42,
            endereco: 'Rua H, Cidade H',
            telefone: '(88) 1234-5678',
            cpf: '123.890.567-08',
          },
          {
            nome: 'Rafael',
            idade: 31,
            endereco: 'Rua I, Cidade I',
            telefone: '(99) 5678-1234',
            cpf: '567.234.890-09',
          },
          {
            nome: 'Camila',
            idade: 26,
            endereco: 'Rua J, Cidade J',
            telefone: '(00) 8765-4321',
            cpf: '876.567.123-10',
          },
        ];
  
        return new Response(JSON.stringify(pessoas), {
          headers: {
            'Content-Type': 'application/json',
          },
        });
      } else {
        return new Response('Não encontrado', { status: 404 });
      }
    },
    port: 8083,
  });
  