package main

import (
	"fmt"
	"github.com/gin-gonic/gin"
	"sync"
)

// Contador de solicitações
var requestCount int
var mu sync.Mutex

func main() {
	r := gin.Default()

	r.GET("/go", func(c *gin.Context) {
		mu.Lock()
		requestCount++
		mu.Unlock()
		c.String(200, "Hello from Go!")
	})

	err := r.Run(":8080")
	if err != nil {
		fmt.Println(err)
	}
}
