import subprocess
import time

# Número de solicitações para cada servidor
num_requests = 1000

# URLs dos servidores Flask, Go, FastAPI e os servidores adicionais em C e Node.js
flask_url = 'http://localhost:5000/flask'
go_url = 'http://localhost:8080/go'
fastapi_url = 'http://localhost:8000/fastapi'
c_server_url = 'http://localhost:8081/c_server'  # Exemplo do servidor C
nodejs_server_url = 'http://localhost:8082/nodejs_server'  # Exemplo do servidor Node.js

def run_benchmark(url):
    response_times = []
    for _ in range(num_requests):
        start_time = time.time()
        subprocess.call(['curl', '-s', url], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        end_time = time.time()
        response_times.append(end_time - start_time)
    return response_times

def calculate_performance(reference_response_times, target_response_times):
    reference_avg_time = sum(reference_response_times) / len(reference_response_times)
    target_avg_time = sum(target_response_times) / len(target_response_times)
    return (reference_avg_time / target_avg_time) * 100

print("Iniciando teste de carga...")

# Realize o benchmark para Flask
flask_response_times = run_benchmark(flask_url)
flask_requests_per_second = num_requests / sum(flask_response_times)

# Realize o benchmark para Go
go_response_times = run_benchmark(go_url)
go_requests_per_second = num_requests / sum(go_response_times)

# Realize o benchmark para FastAPI
fastapi_response_times = run_benchmark(fastapi_url)
fastapi_requests_per_second = num_requests / sum(fastapi_response_times)

# Realize o benchmark para o servidor em C (substitua pelo comando real)
c_server_response_times = run_benchmark(c_server_url)
c_server_requests_per_second = num_requests / sum(c_server_response_times)

# Realize o benchmark para o servidor Node.js (substitua pelo comando real)
nodejs_server_response_times = run_benchmark(nodejs_server_url)
nodejs_server_requests_per_second = num_requests / sum(nodejs_server_response_times)

# Calcule a porcentagem de desempenho em relação ao Flask
go_performance = calculate_performance(flask_response_times, go_response_times)
fastapi_performance = calculate_performance(flask_response_times, fastapi_response_times)
c_server_performance = calculate_performance(flask_response_times, c_server_response_times)
nodejs_server_performance = calculate_performance(flask_response_times, nodejs_server_response_times)

# Imprima os resultados
print(f"Tempo total para Flask: {sum(flask_response_times):.2f} segundos")
print(f"Solicitações por segundo para Flask: {flask_requests_per_second:.2f}\n")

print(f"Tempo total para Go: {sum(go_response_times):.2f} segundos")
print(f"Solicitações por segundo para Go: {go_requests_per_second:.2f}")
print(f"Porcentagem de desempenho em relação ao Flask: {go_performance:.2f}%\n")

print(f"Tempo total para FastAPI: {sum(fastapi_response_times):.2f} segundos")
print(f"Solicitações por segundo para FastAPI: {fastapi_requests_per_second:.2f}")
print(f"Porcentagem de desempenho em relação ao Flask: {fastapi_performance:.2f}%\n")

print(f"Tempo total para o servidor em C: {sum(c_server_response_times):.2f} segundos")
print(f"Solicitações por segundo para o servidor em C: {c_server_requests_per_second:.2f}")
print(f"Porcentagem de desempenho em relação ao Flask: {c_server_performance:.2f}%\n")

print(f"Tempo total para o servidor Node.js: {sum(nodejs_server_response_times):.2f} segundos")
print(f"Solicitações por segundo para o servidor Node.js: {nodejs_server_requests_per_second:.2f}")
print(f"Porcentagem de desempenho em relação ao Flask: {nodejs_server_performance:.2f}%")
