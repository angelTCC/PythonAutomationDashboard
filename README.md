# Python automation Dashboard

## Project Overview

This project is a **Python-based desktop application** designed to **automate the collection, storage, and visualization** of agricultural market prices and weather data relevant to farming and energy consumption. It scrapes live data from websites, fetches weather info through APIs, stores data locally in organized files, and displays real-time updates in a graphical user interface (GUI).

## Motivation

This project helps to:
```
┌───────────────────────────── AgroOps Dashboard ─────────────────────────────┐
│ Weather | Market | Inventory | Tasks | Alerts | Reports | Config           │
├─────────────────────────────────────────────────────────────────────────────┤
│ 🌦 Weather (Auto-Refresh in 30 mins)                                        │
│ Region: [Lima ▾]     Date: [2025-06-08]       Forecast: ☀️ High: 28°C       │
│ ┌────────────┬────────────┬────────────┬────────────┐                      │
│ │ Today      │ +1 Day     │ +2 Days    │ +3 Days     │                      │
│ │ 🌧 90% rain │ 🌤         │ 🌧 40%     │ ☀️ Clear     │                      │
│ └────────────┴────────────┴────────────┴────────────┘                      │
│ → [⚙ Configure Regions]   [🔄 Refresh Now]                                  │
├─────────────────────────────────────────────────────────────────────────────┤
│ 📦 Inventory Snapshot       | 💰 Market Prices       | 🛠 Today's Tasks       │
│ Crop      | Qty | Spoil %  | Crop   | S/ per kg | ▲▼ | Task        | Status│
│ Potatoes  | 13T | 15% risk | Onion  | 2.10      | ▲  | Harvest Lima| ⏳     │
│ Tomatoes  | 3T  | OK       | Potato | 1.70      | ▼  | Irrigate Jauja| ✅   │
│ Corn      | 10T | 5% risk  | Corn   | 1.20      | →  | Spray Fungicide| 🕒 │
│ → [📁 View Full Inventory]  → [📊 Price History]    → [📝 View All Tasks]     │
├─────────────────────────────────────────────────────────────────────────────┤
│ ⚠️ Active Alerts                                                            │
│ - Rain expected today in Cusco (check irrigation)                           │
│ - Maize price up 5% in Huancayo (consider selling)                          │
│ - Onion batch at risk of spoilage (4 days left)                             │
├─────────────────────────────────────────────────────────────────────────────┤
│ [🧲 Run Scraping] [☁️ Fetch Weather] [📤 Generate Daily Report]              │
│ [⚙ Set Auto-Scrape] [📆 Schedule Next Task]                                 │
└─────────────────────────────────────────────────────────────────────────────┘

```

* Practice Python scripting for automation tasks.
* Learn web scraping with BeautifulSoup/Scrapy.
* Interact with REST APIs using the requests library.
* Automate file handling and data storage.
* Build a simple desktop GUI to visualize real-time data.
* Schedule tasks to run automatically.

https://polygon.io/pricing
https://openweathermap.org/api
https://official-joke-api.appspot.com/random_joke
https://www.agriculture.com/markets/commodity-prices
https://www.bloomberg.com/markets/commodities/futures/agriculture
https://www.agroperu.pe/
https://www.emmsa.com.pe/index.php/precios-diarios/
https://www.meteored.pe/tiempo-en-America+Sur-Peru-Lima-1-6-139-5711.html
https://www.preciocombustible.com/lima/

## Features

* **Web Scraping**: Extract live agricultural prices from local market websites.
* **API Integration**: Fetch current and forecasted weather data from OpenWeatherMap API.
* **File Automation**: Store scraped data and API responses in CSV or JSON files, organized by date.
* **Real-Time GUI**: Display data tables and interactive charts in a Tkinter-based desktop app.
* **Task Scheduling**: Schedule automated scraping and data fetching on intervals (e.g., hourly or daily).
* **Manual Controls**: Buttons to trigger scraping, fetching, and report generation manually.
* **Data Visualization**: Use matplotlib or Plotly to visualize price trends and weather changes.

## Technologies Used

| Technology              | Purpose                                  |
| ----------------------- | ---------------------------------------- |
| Python                  | Core programming language for automation |
| BeautifulSoup / Scrapy  | Web scraping                             |
| requests                | API interaction                          |
| pandas                  | Data manipulation and storage            |
| Tkinter / CustomTkinter | Desktop GUI development                  |
| matplotlib / Plotly     | Data visualization                       |
| schedule                | Task scheduling                          |
| threading               | Keep GUI responsive during tasks         |


## Getting Started

### Prerequisites

* Python 3.8+
* Packages (install via `pip install -r requirements.txt`)

### Installation

1. Clone the repository
   ```bash
   git clone https://github.com/yourusername/agro-weather-scraper.git
   cd agro-weather-scraper
   ```
2. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```
3. Obtain an API key from [OpenWeatherMap](https://openweathermap.org/api) (free tier)
4. Configure your API key in `config.py` (create this file with your key)


## How to Use

1. Run the desktop app:
```bash
python main.py
```
2. Use buttons in the GUI to:
   * Scrape crop prices from predefined websites.
   * Fetch current weather and forecasts.
   * View data tables and charts.
   * Enable or disable auto-scheduling of data updates.

3. Scraped and fetched data will be stored automatically in the `data/` folder, organized by date.
4. Data visualization will update dynamically after each fetch/scrape.

## Project Structure

```
agroops_dashboard/
├── main.py                            # App entry point (starts GUI)
├── config/
│   └── settings.py                    # API keys, URLs, config variables
│   └── constants.py                   # Static labels, icons, paths
├── data/
│   ├── weather/YYYY-MM-DD_weather.json
│   ├── prices/YYYY-MM-DD_prices.csv
│   ├── inventory/YYYY-MM-DD_inventory.csv
│   ├── tasks/tasks.json
│   └── reports/daily_2025-06-08.pdf
├── gui/
│   ├── __init__.py
│   ├── main_window.py                # Main layout with tabs
│   ├── tabs/
│   │   ├── weather_tab.py           # Weather forecast display
│   │   ├── price_tab.py             # Market prices and charts
│   │   ├── inventory_tab.py         # Stock levels and spoilage tracker
│   │   ├── tasks_tab.py             # Daily tasks and field ops
│   │   ├── alerts_tab.py            # Critical alerts panel
│   │   └── reports_tab.py           # Generate/export reports
│   ├── components/
│   │   ├── table_widget.py          # Custom QTableWidget
│   │   ├── chart_widget.py          # Plotly or matplotlib canvas
│   │   ├── button_panel.py          # Common button bar
│   │   └── icons.qrc                # Qt Resource file (icons/images)
├── backend/
│   ├── __init__.py
│   ├── scraper/
│   │   ├── crop_scraper.py          # Scrape data from EMMSA, AgroPeru, etc.
│   │   ├── price_sources.py         # URLs, parsing rules
│   ├── weather/
│   │   ├── weather_api.py           # Fetch from OpenWeatherMap
│   │   └── forecast_utils.py        # Preprocess + normalize forecast data
│   ├── inventory/
│   │   ├── inventory_manager.py     # Update and check stock levels
│   │   └── spoilage_estimator.py    # Estimate risk from time/conditions
│   ├── tasks/
│   │   └── task_manager.py          # Create, update, complete tasks
│   ├── alerts/
│   │   └── alert_engine.py          # Generate alerts from data rules
│   └── reports/
│       └── report_generator.py      # Build daily PDF or CSV report
├── automation/
│   ├── scheduler.py                 # schedule & threading logic
│   ├── auto_runner.py               # Trigger scraping/weather updates
│   └── notifier.py                  # (Optional) Email/Telegram alerts
├── assets/
│   ├── icons/                       # PNG/SVG icons
│   ├── images/                      # Static background/header images
│   └── templates/                   # HTML or Jinja templates for reports
├── requirements.txt
├── README.md
└── .env                            # (Optional) for storing API keys

```

## Explanation of Each Part

### 1. `data/`

* Stores all collected data files.
* Organized into subfolders by data type and date, e.g., crop prices CSVs and weather JSONs.
* Makes historical data easy to find and analyze later.

### 2. `gui/`

* Contains all code related to the desktop user interface.
* `app.py` builds the main window, buttons, tables, and graphs.
* `components.py` modularizes UI parts like buttons, tables, etc.
* `plots.py` handles data visualization (generating charts from data).

### 3. `scraper/`

* Responsible for data acquisition.
* `crop_prices.py` scrapes live crop prices using BeautifulSoup or Scrapy.
* `weather_api.py` fetches weather data by calling OpenWeatherMap’s API.

### 4. `automation/`

* Core automation scripts.
* `scheduler.py` manages running scraping and fetching on set intervals.
* `file_handler.py` manages file operations like moving, renaming, or archiving.
* `email_report.py` (optional) automates sending summary reports by email.

### 5. `config.py`

* Holds configuration variables such as API keys and target URLs.
* Keeps sensitive data separate from code for security.

### 6. `main.py`

* The app entry point.
* Initializes and runs the GUI application.


## Future Enhancements

* Add **email notifications** with key alerts (price spikes, weather warnings).
* Integrate **cloud storage** (Dropbox, Google Drive) for backups.
* Implement **machine learning** models to forecast crop prices or energy usage.
* Build a **React web dashboard** as a front-end alternative.
* Containerize the app with **Docker** and orchestrate with **Kubernetes** for scalable deployment.

## Contributing

Feel free to open issues or submit pull requests if you want to improve the project!

## License

This project is open-source and free to use.

