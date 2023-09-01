from flask import Flask, render_template, request, jsonify
import random
import time

app = Flask(__name__)

# Dados iniciais de temperatura, umidade e luminosidade
temperatura = 25.0
umidade = 50
luminosidade = 200

def atualizar_dados():
    global temperatura, umidade, luminosidade
    while True:
        # Simula a obtenção de novos dados em tempo real
        temperatura += random.uniform(-1, 1)
        umidade += random.uniform(-2, 2)
        luminosidade += random.uniform(-5, 5)
        
        # Limita os valores dentro de faixas razoáveis
        temperatura = max(10.0, min(40.0, temperatura))
        umidade = max(0, min(100, umidade))
        luminosidade = max(0, min(1000, luminosidade))
        
        #time.sleep()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/dados', methods=['GET'])
def obter_dados():
    global temperatura, umidade, luminosidade
    return jsonify({'temperatura': temperatura, 'umidade': umidade, 'luminosidade': luminosidade})

if __name__ == '__main__':
    import threading
    # Inicia a thread para atualizar os dados em segundo plano
    data_thread = threading.Thread(target=atualizar_dados)
    data_thread.daemon = True
    data_thread.start()
    
    app.run(debug=True)
