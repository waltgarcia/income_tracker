markdown

# 💰 Monthly Income Simulator

![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

A interactive web application for simulating and visualizing monthly income patterns, built with Streamlit.

## 🌟 Features

- **Customizable income simulation**:
  - Set weekday and weekend daily income
  - Specify non-working weekdays
  - Select any month and year

- **Interactive visualizations**:
  - Daily income bar chart (color-coded by day type)
  - Cumulative income line graph
  - ±$100 daily income comparison

- **Comprehensive summary**:
  - Total monthly income
  - Average daily income (working days only)
  - Working/non-working day counts
  - Daily income range

## 🚀 Quick Start

1. **Install dependencies**:
   ```bash
   pip install streamlit pandas numpy matplotlib

    Run the application:
    bash

    streamlit run simulador_ingresos.py

    Access the app:

        The application will automatically open in your default browser

        Or visit http://localhost:8501

🖥️ Usage Guide
Sidebar Controls

    Month/Year: Select the simulation period

    Weekday Income: Set daily income for Monday-Friday

    Weekend Income: Set daily income for Saturday-Sunday

    Non-working Days: Number of weekdays with no income

Visualization Tabs

    Daily Income: Bar chart showing income each day

    Cumulative Sum: Line graph of running monthly total

    ±$100 Comparison: Scenario analysis with income variations

Key Metrics

    Total monthly income

    Average daily income (working days)

    Count of working/non-working days

    Daily income range (min-max)

📊 Example Output

https://i.imgur.com/JQ8wzEj.png
🛠️ Technical Details

Built with:

    Python 3.7+

    Streamlit (web framework)

    Pandas (data manipulation)

    Matplotlib (visualization)

    NumPy (numerical operations)

File Structure:
text

income-simulator/
├── simulador_ingresos.py  # Main application code
├── README.md              # This documentation
└── requirements.txt       # Dependencies

🌐 Deployment Options

    Streamlit Sharing (easiest):

        Upload to GitHub

        Connect repository at share.streamlit.io

    Docker Container:
    dockerfile

    FROM python:3.9-slim
    WORKDIR /app
    COPY . .
    RUN pip install -r requirements.txt
    CMD ["streamlit", "run", "simulador_ingresos.py"]

    Traditional Hosting:

        Requires WSGI server setup

        Use NGINX/Apache as reverse proxy

🤝 Contributing

    Fork the project

    Create your feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some amazing feature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

📜 License

Distributed under the MIT License. See LICENSE for more information.
✉️ Contact

Your Name - walter.garciaortiz@gmail.com

Project Link: https://github.com/waltgarcia/income-simulator
