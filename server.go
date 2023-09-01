package main

import (
    "fmt"
    "net/http"
    "sync"
)

// Contador de solicitações
var requestCount int
var mu sync.Mutex

func handler(w http.ResponseWriter, r *http.Request) {
    mu.Lock()
    requestCount++
    mu.Unlock()
    fmt.Fprintf(w, "Hello from Go!")
}

func main() {
    http.HandleFunc("/go", handler)
    http.ListenAndServe(":8080", nil)
}
