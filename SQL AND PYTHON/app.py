import streamlit as st
import pandas as pd
import pyodbc
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import matplotlib.pyplot as plt

# --- Connect to SQL Server ---
@st.cache_resource
def connect_db():
    return pyodbc.connect(
        'Driver={SQL Server};'
        'Server=LAPTOP-DI9HFMRT;'  # Replace with your server name if different
        'Database=UtilityBilling;'
        'Trusted_Connection=yes;'
    )
conn = connect_db()

# Get users from database
users_df = pd.read_sql("SELECT user_id, name FROM users", conn)

# User selection
user_name = st.selectbox("Select User", users_df['name'])
user_id = users_df[users_df['name'] == user_name]['user_id'].values[0]

# Get billing data for selected user
query = f"SELECT month, bill_amount FROM bills WHERE user_id = {user_id} ORDER BY month"
df = pd.read_sql(query, conn)
df['month_num'] = range(len(df))

# Train model
X = df[['month_num']]
y = df['bill_amount']
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)
model = LinearRegression()
model.fit(X_poly, y)

# Predict next bill
next_input = pd.DataFrame({"month_num": [len(df)]})
predicted = model.predict(poly.transform(next_input))[0]
latest_actual = df.iloc[-1]['bill_amount']
y_pred = model.predict(X_poly)

# Metrics
mae = mean_absolute_error(y, y_pred)
mse = mean_squared_error(y, y_pred)
r2 = r2_score(y, y_pred)

# Display metrics
st.subheader("📊 Prediction Report")
st.write(f"**User:** {user_name}")
st.write(f"**Predicted Next Bill:** ₹{int(predicted)}")
st.write(f"**Last Actual Bill:** ₹{int(latest_actual)}")
st.write(f"**MAE:** ₹{mae:.2f}")
st.write(f"**MSE:** {mse:.2f}")
st.write(f"**R² Score:** {r2:.2f}")
st.write("**Status:**", "⚠️ Spike detected!" if latest_actual > predicted * 1.3 else "✅ Bill is normal.")

# Plot
df['predicted'] = y_pred
df.loc[len(df)] = ['Next Month', predicted, len(df), None]
plt.figure(figsize=(10, 5))
plt.plot(df['month'], list(y) + [None], marker='o', label='Actual')
plt.plot(df['month'], list(y_pred) + [predicted], linestyle='--', marker='x', label='Predicted')
plt.axhline(predicted * 1.3, color='red', linestyle=':', label='Spike Threshold')
plt.xticks(rotation=45)
plt.xlabel("Month")
plt.ylabel("Bill Amount (₹)")
plt.title(f"Electricity Bill Forecast for {user_name}")
plt.legend()
plt.tight_layout()
st.pyplot(plt)
