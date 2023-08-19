package main

import (
	"fmt"
	"net/http"
)

var gostou bool

func uploadHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodPost {
		r.ParseMultipartForm(10 << 20) // Define o limite de tamanho do arquivo
		file, _, err := r.FormFile("video")
		if err != nil {
			http.Error(w, "Erro ao receber o arquivo", http.StatusInternalServerError)
			return
		}
		defer file.Close()

		// Aqui você pode fazer algo com o arquivo, como salvá-lo em disco ou processá-lo

		fmt.Println("Vídeo recebido e processado com sucesso!")
	}
}

func likeHandler(w http.ResponseWriter, r *http.Request) {
	if r.Method == http.MethodPost {
		liked := r.FormValue("liked")
		if liked == "true" {
			gostou = true
		} else if liked == "false" {
			gostou = false
		}

		fmt.Println("Opinião do usuário registrada:", gostou)
	}
}

func main() {
	http.HandleFunc("/upload", uploadHandler)
	http.HandleFunc("/like", likeHandler)
	http.Handle("/", http.FileServer(http.Dir("static")))

	fmt.Println("Servidor rodando em http://localhost:8080")
	http.ListenAndServe(":8080", nil)
}
