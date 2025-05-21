#!/bin/bash

# Função auxiliar para rodar script com medição de tempo e memória
run_benchmark() {
  local cmd=$1
  local label=$2

  echo "Executando $label..."
  result=$(/usr/bin/time -f "%e;%M" $cmd 2>&1 >/dev/null)
  tempo=$(echo "$result" | cut -d';' -f1)
  memoria_kb=$(echo "$result" | cut -d';' -f2)
  memoria_mb=$(echo "scale=2; $memoria_kb / 1024" | bc)
  echo "$label => Tempo: ${tempo}s | Memória: ${memoria_mb} MB"
  echo ""
}

# Execuções
run_benchmark "python3 benchmarkNumpy.py"       "Python + NumPy"
run_benchmark "python3 benchmark.py"            "Python puro"
run_benchmark "go run benchmark.go"             "Go sequencial"
run_benchmark "go run benchmarkParalell.go"     "Go paralelo"

echo "===== FIM DO BENCHMARK ====="
