# Electricity-Bill-Forecasting-and-Anomaly-Detection-using-SQL-Python-Streamlit

# Electricity Bill Forecasting System

This project is a web-based tool that predicts the next month's electricity bill using machine learning. It uses data stored in a SQL Server database and is built with Python and Streamlit.

---

## 📌 Project Summary

- Connects to a local SQL database with electricity usage and billing data.
- Uses Polynomial Regression (Machine Learning) to forecast future bills.
- Detects abnormal spikes in electricity bills.
- Displays results in a simple, interactive Streamlit web dashboard.

---

## 🔧 Technologies Used

- **Python**
- **Streamlit**
- **Pandas**
- **Scikit-learn**
- **Matplotlib**
- **pyodbc**
- **Microsoft SQL Server**

---

## 🧾 Database Structure

### `users` table
| Column    | Type     |
|-----------|----------|
| user_id   | INT      |
| name      | NVARCHAR |
| address   | NVARCHAR |

### `bills` table
| Column      | Type   |
|-------------|--------|
| bill_id     | INT    |
| user_id     | INT    |
| month       | VARCHAR|
| usage_kwh   | FLOAT  |
| bill_amount | FLOAT  |

---

## 🧪 Sample Data

This project works with one user and 30 months of billing data (from Jan 2021 to June 2023).

Example:
```sql
(1, '2021-01', 160, 1120),
(1, '2023-06', 275, 1920);
