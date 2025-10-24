# Weather CLI 🌤️

**Weather CLI** is a simple Python console application that allows you to get current weather information for your location or any city in the world using the OpenWeatherMap API.

---

## 🔹 Features

- Get current weather for your **IP-based location** or **any city**  
- Displays:
  - Temperature and "feels like"  
  - Main weather condition and description  
  - Humidity and wind speed  
- Supports **language and unit settings**  
- Cross-platform CLI (Windows, Linux, macOS)

---

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/weather-cli.git
cd weather-cli
```

2. Create and activate a virtual environment:
```bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# Linux / macOS
source .venv/bin/activate
```

3. Install dependencies:

```Bash
pip install -r requirements.txt
```

4. Create a .env file in the project root and add your OpenWeatherMap API key.
You can find API key here: https://home.openweathermap.org/api_keys
```
API_KEY=your_api_key_here
```

## 🚀 Usage 
Run the application:
```Bash
python main.py
```
The program will automatically show weather for your current location (based on IP).

You can also search for weather in other cities by entering:

- City name
- Optional country code
- Optional state code

## 🌐 Example

```
Weather in London:
  Main: Clouds
  Description: broken clouds
  Temperature: 18°C
  Feels Like: 17°C
  Humidity: 65%
  Wind Speed: 3 m/s
```

## 📦 Dependencies

- Python 3.10+
- requests
- python-dotenv
- geocoder
