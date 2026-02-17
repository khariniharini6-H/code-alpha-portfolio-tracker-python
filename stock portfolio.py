# ================================
# Stock Portfolio Tracker
# Author: Your Name
# ================================

# Install required libraries before running:
# pip install yfinance pandas matplotlib

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# Step 1: Define Portfolio
# ------------------------------
# Format: "Stock Symbol": (Quantity, Buy Price)

portfolio = {
    "AAPL": (5, 150),
    "MSFT": (3, 280),
    "TSLA": (2, 200)
}

# ------------------------------
# Step 2: Calculate Portfolio Value
# ------------------------------

total_investment = 0
current_value = 0

print("\n📊 STOCK PORTFOLIO SUMMARY\n")

for stock, (quantity, buy_price) in portfolio.items():
    ticker = yf.Ticker(stock)
    current_price = ticker.history(period="1d")["Close"][0]

    invested_amount = quantity * buy_price
    present_value = quantity * current_price
    profit_loss = present_value - invested_amount

    total_investment += invested_amount
    current_value += present_value

    print(f"Stock: {stock}")
    print(f"  Buy Price: ${buy_price}")
    print(f"  Current Price: ${round(current_price,2)}")
    print(f"  Invested Amount: ${round(invested_amount,2)}")
    print(f"  Current Value: ${round(present_value,2)}")
    print(f"  Profit/Loss: ${round(profit_loss,2)}\n")

# ------------------------------
# Step 3: Total Summary
# ------------------------------

overall_profit = current_value - total_investment

print("===================================")
print(f"Total Investment: ${round(total_investment,2)}")
print(f"Current Portfolio Value: ${round(current_value,2)}")
print(f"Overall Profit/Loss: ${round(overall_profit,2)}")
print("===================================\n")

# ------------------------------
# Step 4: Portfolio Allocation Chart
# ------------------------------

values = []
labels = []

for stock, (quantity, _) in portfolio.items():
    ticker = yf.Ticker(stock)
    current_price = ticker.history(period="1d")["Close"][0]
    values.append(quantity * current_price)
    labels.append(stock)

plt.figure()
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Portfolio Allocation")
plt.show()

# ------------------------------
# Step 5: 1-Year Stock Trend
# ------------------------------

for stock in portfolio.keys():
    data = yf.download(stock, period="1y")
    plt.figure()
    plt.plot(data["Close"])
    plt.title(f"{stock} - 1 Year Price Trend")
    plt.xlabel("Date")
    plt.ylabel("Closing Price")
    plt.show()
