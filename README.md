``` 
# 💰 Monthly Income Simulator

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://streamlit.io/)
![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)

An interactive web application for simulating monthly income patterns with customizable parameters.

---

## 📌 Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## 🌟 Features

- **Customizable Income Simulation**
  - Set different rates for weekdays vs. weekends
  - Specify number of non-working weekdays
  - Select any month/year combination

- **Interactive Visualizations**
  - Daily income breakdown (bar chart)
  - Cumulative income tracker (line graph)
  - Scenario comparison (±$100 variations)

- **Comprehensive Analytics**
  - Total monthly income calculation
  - Average daily income (working days)
  - Working/non-working day statistics

---

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/waltgarcia/income_tracker.git
   cd income_tracker
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 Usage

Run the application with Streamlit:
```bash
streamlit run simulador_ingresos.py
```

**Configure your simulation:**
- Select month and year
- Set weekday and weekend rates
- Specify non-working days
- View results in interactive tabs

---

## 📊 Examples

**Daily Income View**

![Daily Income View](https://i.imgur.com/JQ8wzEj.png)

**Cumulative Income**

![Cumulative Income](https://i.imgur.com/9LkQY2a.png)

---

## 🌐 Deployment

### Streamlit Community Cloud

1. Push your code to GitHub.
2. Deploy at [share.streamlit.io](https://share.streamlit.io/).

### Docker

Build and run with Docker:
```bash
docker build -t income-simulator .
docker run -p 8501:8501 income-simulator
```

---

## 🤝 Contributing

1. Fork the project
2. Create your feature branch  
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. Commit your changes  
   ```bash
   git commit -m 'Add AmazingFeature'
   ```
4. Push to the branch  
   ```bash
   git push origin feature/AmazingFeature
   ```
5. Open a Pull Request

---

## 📜 License

MIT License – see [LICENSE](LICENSE) for details

---

## ✉️ Contact

Project Maintainer – Walter García 
Project Link: [https://github.com/waltgarcia/income_tracker](https://github.com/waltgarcia/income_tracker)

```
