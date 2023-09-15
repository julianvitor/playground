document.addEventListener("DOMContentLoaded", function () {
    const waterButton = document.getElementById("water-button");
    const sensorContainer = document.getElementById("sensor-container");
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    const container = document.querySelector(".container");
    const body = document.body;
    const preferredMode = localStorage.getItem("preferredMode");



    function setMode(mode) {
        if (mode === "dark") {
            container.classList.add("dark-mode");
            body.classList.add("dark-mode");
            darkModeToggle.innerText = "Modo Claro";
        } else {
            container.classList.remove("dark-mode");
            body.classList.remove("dark-mode");
            darkModeToggle.innerText = "Modo Escuro";
        }
        // Salvar a preferência do usuário
        localStorage.setItem("preferredMode", mode);
    }

    // Event listener para o botão de alternar o modo escuro
    darkModeToggle.addEventListener("click", function () {
        if (body.classList.contains("dark-mode")) {
            setMode("light");
        } else {
            setMode("dark");
        }
    });

    // Definir o modo inicial com base na preferência do usuário ou na preferência do sistema
    if (preferredMode === "dark" || (preferredMode === null && window.matchMedia("(prefers-color-scheme: dark)").matches)) {
        setMode("dark");
    } else {
        setMode("light");
    } 

    // Função para buscar dados do sensor a partir da API do Flask
    function fetchSensorData() {
        fetch('/sensor-data')
            .then((response) => response.json())
            .then((data) => {
                // Atualizar os dados do sensor na página
                sensorContainer.innerHTML = `
                
                <span>Sensores de Ar e Solo</span>
                    <div class="sensor-item">
                        <i class="material-icons">thermostat</i>
                        <span>Temperatura do Ar: ${data.air_temp}</span>
                    </div>
                    <div class="sensor-item">
                        <i class="material-icons">thermostat</i>
                        <span>Temperatura do Solo: ${data.soil_temp}</span>
                    </div>
                    <div class="sensor-item">
                        <i class="material-icons">invert_colors</i>
                        <span>pH do Solo: ${data.ph}</span>
                    </div>
                    <div class="sensor-item">
                        <i class="material-icons">wb_sunny</i>
                        <span>Umidade do Ar: ${data.air_humidity}</span>
                    </div>
                    <div class="sensor-item">
                        <i class="material-icons">opacity</i>
                        <span>Umidade do Solo: ${data.soil_moisture}</span>
                    </div>
                    
                    <h2>Eletricidade e Reservatórios</h2>
                    <div class="sensor-item">
                        <i class="material-icons">power</i>
                        <span>Consumo de Eletricidade: ${data.electrical_consumption}</span>
                    </div>
                    <div class="sensor-item">
                        <i class="material-icons">local_drink</i>
                        <span>Nível do Reservatório 1: ${data.reservoir_l1}</span>
                    </div>
                    <div class="sensor-item">
                        <i class="material-icons">local_drink</i>
                        <span>Nível do Reservatório 2: ${data.reservoir_l2}</span>
                    </div>
                    
                    <h2>Sensores Ambientais</h2>
                    <div class="sensor-item">
                        <i class="material-icons">cloud</i>
                        <span>Nível de CO2: ${data.co2}</span>
                    </div>
                    <div class="sensor-item">
                        <i class="material-icons">wb_incandescent</i>
                        <span>Nível de Luz: ${data.light}</span>
                    </div>
                `;
            });
    }

    // Event listener para o botão "Regar Manualmente"
    waterButton.addEventListener("click", function () {
        fetch('/water-plant', { method: 'POST' })
            .then((response) => response.json())
            .then((data) => {
                // Exibir uma mensagem indicando que a planta foi regada
                alert(data.message);
            });
    });

    // Buscar dados do sensor inicialmente quando a página carrega
    fetchSensorData();

    // Configurar um temporizador para buscar dados do sensor periodicamente (por exemplo, a cada 5 segundos)
    setInterval(fetchSensorData, 7000);
});