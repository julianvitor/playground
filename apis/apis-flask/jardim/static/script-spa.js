document.addEventListener("DOMContentLoaded", function () {
    const waterButton = document.getElementById("water-button");
    const sensorContainer = document.getElementById("sensor-container");
    const darkModeToggle = document.getElementById("dark-mode-toggle");
    const container = document.querySelector(".container");
    const body = document.body;
    const preferredMode = localStorage.getItem("preferredMode");

    // Defina o idioma preferido inicialmente (por exemplo, inglês)
    let preferredLanguage = "portuguese"; // Defina o idioma padrão

    // Objeto com traduções
    const translatedText = {
        // Traduções para o inglês
        english: {
            darkMode: "Dark Mode",
            lightMode: "Light Mode",
            manualWatering: "Manual Watering",
            sensorSection: "Air and Soil Sensors",
            airTemperature: "Air Temperature",
            soilTemperature: "Soil Temperature",
            soilPH: "Soil pH",
            airHumidity: "Air Humidity",
            soilMoisture: "Soil Moisture",
            electricitySection: "Electricity and Reservoirs",
            electricalConsumption: "Electrical Consumption",
            reservoirLevel1: "Reservoir Level 1",
            reservoirLevel2: "Reservoir Level 2",
            environmentalSensors: "Environmental Sensors",
            co2Level: "CO2 Level",
            lightLevel: "Light Level",
        },
        // Traduções para o português
        portuguese: {
            darkMode: "Modo Escuro",
            lightMode: "Modo Claro",
            manualWatering: "Regar Manualmente",
            sensorSection: "Sensores de Ar e Solo",
            airTemperature: "Temperatura do Ar",
            soilTemperature: "Temperatura do Solo",
            soilPH: "pH do Solo",
            airHumidity: "Umidade do Ar",
            soilMoisture: "Umidade do Solo",
            electricitySection: "Eletricidade e Reservatórios",
            electricalConsumption: "Consumo de Eletricidade",
            reservoirLevel1: "Nível do Reservatório 1",
            reservoirLevel2: "Nível do Reservatório 2",
            environmentalSensors: "Sensores Ambientais",
            co2Level: "Nível de CO2",
            lightLevel: "Nível de Luz",
        },
    };

    function setMode(mode) {
        if (mode === "dark") {
            container.classList.add("dark-mode");
            body.classList.add("dark-mode");
            darkModeToggle.innerText = translatedText[preferredLanguage].lightMode;
        } else {
            container.classList.remove("dark-mode");
            body.classList.remove("dark-mode");
            darkModeToggle.innerText = translatedText[preferredLanguage].darkMode;
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

    // Função para buscar dados do sensor a partir da API do Flask e atualizar a página
    function fetchAndUpdateSensorData() {
        fetch('/sensor-data')
            .then((response) => response.json())
            .then((data) => {
                // Atualizar os dados dos sensores com base nos dados recebidos da API do Flask
                updateSensorData(data);
            });
    }

    // Função para atualizar os dados dos sensores na página
    function updateSensorData(data) {
        // Atualizar os dados do sensor na página
        sensorContainer.innerHTML = `
            <h2>${translatedText[preferredLanguage].sensorSection}</h2>
            <div class="sensor-item">
                <i class="material-icons">thermostat</i>
                <span>${translatedText[preferredLanguage].airTemperature}: ${data.air_temperature}</span>
            </div>
            <div class="sensor-item">
                <i class="material-icons">thermostat</i>
                <span>${translatedText[preferredLanguage].soilTemperature}: ${data.soil_temperature}</span>
            </div>
            <div class="sensor-item">
                <i class="material-icons">invert_colors</i>
                <span>${translatedText[preferredLanguage].soilPH}: ${data.soil_ph}</span>
            </div>
            <div class="sensor-item">
                <i class="material-icons">wb_sunny</i>
                <span>${translatedText[preferredLanguage].airHumidity}: ${data.air_humidity}</span>
            </div>
            <div class="sensor-item">
                <i class="material-icons">opacity</i>
                <span>${translatedText[preferredLanguage].soilMoisture}: ${data.soil_moisture}</span>
            </div>

            <h2>${translatedText[preferredLanguage].electricitySection}</h2>
            <div class="sensor-item">
                <i class="material-icons">power</i>
                <span>${translatedText[preferredLanguage].electricalConsumption}: ${data.electrical_consumption}</span>
            </div>
            <div class="sensor-item">
                <i class="material-icons">local_drink</i>
                <span>${translatedText[preferredLanguage].reservoirLevel1}: ${data.reservoir_level_1}</span>
            </div>
            <div class="sensor-item">
                <i class="material-icons">local_drink</i>
                <span>${translatedText[preferredLanguage].reservoirLevel2}: ${data.reservoir_level_2}</span>
            </div>

            <h2>${translatedText[preferredLanguage].environmentalSensors}</h2>
            <div class="sensor-item">
                <i class="material-icons">cloud</i>
                <span>${translatedText[preferredLanguage].co2Level}: ${data.co2_level}</span>
            </div>
            <div class="sensor-item">
                <i class="material-icons">wb_incandescent</i>
                <span>${translatedText[preferredLanguage].lightLevel}: ${data.light_level}</span>
            </div>
        `;
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
    fetchAndUpdateSensorData();

    // Configurar um temporizador para buscar dados do sensor periodicamente (por exemplo, a cada 5 segundos)
    setInterval(fetchAndUpdateSensorData, 5000);

    // Event listener para alternar entre inglês e português
    const languageSwitchBtn = document.getElementById("language-switch-btn");
    languageSwitchBtn.addEventListener("click", function () {
        // Alternar entre inglês e português
        preferredLanguage = preferredLanguage === "english" ? "portuguese" : "english";

        // Atualize os textos na página com base no novo idioma
        darkModeToggle.innerText = translatedText[preferredLanguage].darkMode;
        waterButton.innerText = translatedText[preferredLanguage].manualWatering;

        // Atualize o texto do botão de alternância de idioma
        languageSwitchBtn.innerText = preferredLanguage === "english" ? "Português" : "English";
    });
});