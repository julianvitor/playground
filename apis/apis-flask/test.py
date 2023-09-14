import aiohttp
import asyncio
import time

async def make_request(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return 1  # Retorna 1 para cada requisição bem-sucedida
    except Exception as e:
        print(f"Erro na requisição para {url}: {str(e)}")
        return 0  # Retorna 0 para requisições com erro

async def main():
    url = "http://julianvitor.ddns.net:8082/api/sensores"
    total_requisicoes = 0
    tempo_duracao = 20  # Duração total do teste em segundos

    async with aiohttp.ClientSession() as session:
        while time.time() - tempo_inicial < tempo_duracao:
            tasks = [make_request(session, url) for _ in range(60)]  # Envia 10 requisições simultaneamente
            resultados = await asyncio.gather(*tasks)
            total_requisicoes += sum(resultados)

    print(f"Tempo total de teste: {tempo_duracao} segundos")
    print(f"Total de requisições: {total_requisicoes}")

if __name__ == "__main__":
    tempo_inicial = time.time()
    asyncio.run(main())
