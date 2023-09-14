const Bun = require('bun');

const app = Bun.serve({
  fetch(req) {
    if (req.method === 'POST' && req.url === '/check-prime') {
      return req.text().then(body => {
        const formData = new URLSearchParams(body);
        const number = parseInt(formData.get('number'));
        let result = '';

        if (!isNaN(number)) {
          if (isPrime(number)) {
            result = `${number} é um número primo.`;
          } else {
            result = `${number} não é um número primo.`;
          }
        } else {
          result = 'Por favor, insira um número válido.';
        }

        return new Response(result, {
          headers: {
            'Content-Type': 'text/plain',
          },
        });
      });
    } else {
      return new Response('Não encontrado', { status: 404 });
    }
  },
  port: 8083,
});


function isPrime(num) {
  if (num <= 1) {
    return false;
  }
  if (num <= 3) {
    return true;
  }
  if (num % 2 === 0 || num % 3 === 0) {
    return false;
  }
  let i = 5;
  while (i * i <= num) {
    if (num % i === 0 || num % (i + 2) === 0) {
      return false;
    }
    i += 6;
  }
  return true;
}
