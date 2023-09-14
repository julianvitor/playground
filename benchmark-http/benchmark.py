import concurrent.futures
import requests
import time

# Número de solicitações para cada servidor
num_requests = 10000

# Número de threads pré-estabelecido
num_threads = 1

# URLs dos servidores Flask, Go, FastAPI e os servidores adicionais em C, Node.js e bun
flask_url = 'http://localhost:5000/flask'
go_url = 'http://localhost:8080/go'
fastapi_url = 'http://localhost:8000/fastapi'
c_server_url = 'http://localhost:8081/c_server'
nodejs_server_url = 'http://localhost:8082/nodejs_server'
bun_server_url = 'http://localhost:8083/bun'

"""def run_benchmark(url):
    response_times = []
    for _ in range(num_requests):
        start_time = time.time()
        subprocess.call(['curl', '-s', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        end_time = time.time()
        response_times.append(end_time - start_time)
    return response_times"""

"""def run_benchmark(url):
    response_times = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(requests.get, url) for _ in range(num_requests)]
        for future in concurrent.futures.as_completed(futures):
            try:
                response = future.result()
                response_times.append(response.elapsed.total_seconds())
            except requests.exceptions.RequestException:
                # Trata a exceção se a solicitação falhar (por exemplo, servidor offline)
                pass
    return response_times"""


def run_benchmark(url):
    response_times = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_threads) as executor:
        futures = [executor.submit(requests.get, url) for _ in range(num_requests)]
        for future in concurrent.futures.as_completed(futures):
            try:
                response = future.result()
                response_times.append(response.elapsed.total_seconds())
            except requests.exceptions.RequestException:
                # Trata a exceção se a solicitação falhar (por exemplo, servidor offline)
                pass
    return response_times

def calculate_performance(reference_response_times, target_response_times):
    if not target_response_times:
        return 0.0  # Retorna 0% de desempenho se não houver respostas
    reference_avg_time = sum(reference_response_times) / len(reference_response_times)
    target_avg_time = sum(target_response_times) / len(target_response_times)
    return (reference_avg_time / target_avg_time) * 100

print("Iniciando teste de carga...")

# Realize o benchmark para o servidor bun (referência)
bun_server_response_times = run_benchmark(bun_server_url)
bun_requests_per_second = num_requests / sum(bun_server_response_times)

# Cabeçalho da tabela
print("\n{:<25} {:<20} {:<30} {:<35}".format("Servidor", "Tempo Total (s)", "Solicitações por Segundo", "Porcentagem em relação ao bun"))

# Realize o benchmark para Flask
flask_response_times = run_benchmark(flask_url)
flask_requests_per_second = num_requests / sum(flask_response_times) if flask_response_times else 0.0
flask_performance = calculate_performance(bun_server_response_times, flask_response_times)
print("{:<25} {:<20.2f} {:<30.2f} {:<35.2f}%".format("Flask", sum(flask_response_times), flask_requests_per_second, flask_performance))

# Realize o benchmark para Go
go_response_times = run_benchmark(go_url)
go_requests_per_second = num_requests / sum(go_response_times) if go_response_times else 0.0
go_performance = calculate_performance(bun_server_response_times, go_response_times)
print("{:<25} {:<20.2f} {:<30.2f} {:<35.2f}%".format("Go", sum(go_response_times), go_requests_per_second, go_performance))

# Realize o benchmark para FastAPI
fastapi_response_times = run_benchmark(fastapi_url)
fastapi_requests_per_second = num_requests / sum(fastapi_response_times) if fastapi_response_times else 0.0
fastapi_performance = calculate_performance(bun_server_response_times, fastapi_response_times)
print("{:<25} {:<20.2f} {:<30.2f} {:<35.2f}%".format("FastAPI", sum(fastapi_response_times), fastapi_requests_per_second, fastapi_performance))

# Realize o benchmark para o servidor em C
c_server_response_times = run_benchmark(c_server_url)
c_server_requests_per_second = num_requests / sum(c_server_response_times) if c_server_response_times else 0.0
c_server_performance = calculate_performance(bun_server_response_times, c_server_response_times)
print("{:<25} {:<20.2f} {:<30.2f} {:<35.2f}%".format("Servidor em C", sum(c_server_response_times), c_server_requests_per_second, c_server_performance))

# Realize o benchmark para o servidor Node.js
nodejs_server_response_times = run_benchmark(nodejs_server_url)
nodejs_server_requests_per_second = num_requests / sum(nodejs_server_response_times) if nodejs_server_response_times else 0.0
nodejs_server_performance = calculate_performance(bun_server_response_times, nodejs_server_response_times)
print("{:<25} {:<20.2f} {:<30.2f} {:<35.2f}%".format("Servidor Node.js", sum(nodejs_server_response_times), nodejs_server_requests_per_second, nodejs_server_performance))

# Realize o benchmark para o servidor bun
bun_requests_per_second = num_requests / sum(bun_server_response_times)
print("{:<25} {:<20.2f} {:<30} {:<35}".format("Servidor bun", sum(bun_server_response_times), bun_requests_per_second, 100.0))

