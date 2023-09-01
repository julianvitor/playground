import subprocess
import time

# Número de solicitações para cada servidor
num_requests = 2500

# URLs dos servidores Flask, Go e FastAPI
flask_url = 'http://localhost:5000/flask'
go_url = 'http://localhost:8080/go'
fastapi_url = 'http://localhost:8000/fastapi'

def run_benchmark(url):
    start_time = time.time()
    for _ in range(num_requests):
        subprocess.call(['curl', '-s', url])
    end_time = time.time()
    return end_time - start_time

print("Iniciando teste de carga...")

# Realize o benchmark para Flask
flask_time = run_benchmark(flask_url)
flask_requests_per_second = num_requests / flask_time

# Realize o benchmark para Go
go_time = run_benchmark(go_url)
go_requests_per_second = num_requests / go_time

# Realize o benchmark para FastAPI
fastapi_time = run_benchmark(fastapi_url)
fastapi_requests_per_second = num_requests / fastapi_time

# Imprima os resultados
print(f"Tempo total para Flask: {flask_time:.2f} segundos")
print(f"Solicitações por segundo para Flask: {flask_requests_per_second:.2f}")

print(f"Tempo total para Go: {go_time:.2f} segundos")
print(f"Solicitações por segundo para Go: {go_requests_per_second:.2f}")

print(f"Tempo total para FastAPI: {fastapi_time:.2f} segundos")
print(f"Solicitações por segundo para FastAPI: {fastapi_requests_per_second:.2f}")
