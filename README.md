# Electricity-Bill-Forecasting-and-Anomaly-Detection-using-SQL-Python-Streamlit

---

# ⚡ Electricity Bill Forecasting System

A simple and intelligent web-based system to **predict future electricity bills** using **machine learning** and **SQL Server** data.

---

## 📌 Project Summary

This project helps predict a user's upcoming electricity bill using past consumption and billing data. It uses a **Polynomial Regression** model and presents insights via an intuitive **Streamlit dashboard**.

### Key Features:

* 📊 Forecasts next month’s electricity bill.
* ⚠️ Detects abnormal billing spikes.
* 🧠 Built using machine learning (Polynomial Regression).
* 🖥️ Visualizes trends in consumption and billing.
* 🗃️ Uses **SQL Server** as a backend database.

---

## 🔧 Technologies Used

| Component     | Tool/Library         |
| ------------- | -------------------- |
| Frontend      | Streamlit            |
| Backend       | Microsoft SQL Server |
| Programming   | Python               |
| ML Libraries  | Scikit-learn, Pandas |
| Visualization | Matplotlib           |
| DB Connector  | pyodbc               |

---

## 🧾 Database Structure

### 🧍 `users` Table

| Column   | Type     | Description            |
| -------- | -------- | ---------------------- |
| user\_id | INT      | Unique user identifier |
| name     | NVARCHAR | User's name            |
| address  | NVARCHAR | User's address         |

### 🧾 `bills` Table

| Column       | Type    | Description                     |
| ------------ | ------- | ------------------------------- |
| bill\_id     | INT     | Unique bill ID                  |
| user\_id     | INT     | Foreign key referencing `users` |
| month        | VARCHAR | Month in `YYYY-MM` format       |
| usage\_kwh   | FLOAT   | Electricity usage in kWh        |
| bill\_amount | FLOAT   | Monthly electricity bill (₹)    |

---

## 🧪 Sample Data

The system is currently trained on **30 months** of data for **one user**, ranging from **January 2021 to June 2023**.

### Example Record:

```sql
(1, '2021-01', 160, 1120),
(1, '2021-02', 165, 1160),
...
(1, '2023-06', 275, 1920);
```

* `1`: User ID
* `'2021-01'`: Billing month
* `160`: Units consumed (kWh)
* `1120`: Bill amount in ₹

This historical dataset is used to train the ML model and predict future bills.

---

## 📈 How It Works

1. **User Input**: No input required — the dashboard auto-loads.
2. **Data Retrieval**: Connects to SQL Server and fetches user billing history.
3. **Model Training**: Trains a Polynomial Regression model on past bills.
4. **Prediction**: Forecasts the upcoming bill amount.
5. **Spike Detection**: Checks if the last bill was unusually high.
6. **Visualization**: Shows both actual and predicted bills on a graph.

---

## ✅ Output Example

```
Predicted next bill: ₹1944
Last actual bill: ₹1920
MAE: ₹54.29
MSE: 4776.59
R² Score: 0.90
Status: ✅ Bill is normal.
```

---

## 🚀 How to Run the App

1. Install required libraries:

   ```bash
   pip install streamlit pandas scikit-learn pyodbc matplotlib
   ```

2. Make sure SQL Server is running with your data.

3. Run the app:

   ```bash
   streamlit run app.py
   ```

4. Open the browser at `http://localhost:8501`

---

## 📂 Folder Structure

```
project/
│
├── app.py                  # Main Streamlit App
├── requirements.txt        # Python dependencies (optional)
├── README.md               # Project overview
└── user_1_bill_predictions.csv  # Output file (generated)
```

---

## 🧑‍💼 Who Can Use This?

* Utility service providers for predictive billing.
* Households monitoring monthly usage.
* Students learning time-series + SQL + Streamlit.
* Developers building dashboards with real-time DBs.

---

## 📣 Contribution

Currently designed for a single user. You can extend it by:

* Adding dropdowns to select users.
* Adding login/authentication.
* Making the model more robust with seasonal patterns.

---

🙋‍♂️ Author
Vishwanath Kulal
Mangalore, India

