
import csv
import os

# Step 1: Create portfolio dictionary
portfolio = {}

print("\n======================================")
print("     INVESTMENT PORTFOLIO TRACKER")
print("======================================")

# Step 2: Get stock details
n = int(input("\nEnter number of stocks: "))

for i in range(n):

    print("\nEnter details for stock", i + 1)

    ticker = input("Enter stock ticker: ").upper().strip()

    if not ticker or ticker in portfolio:
        print("Invalid or duplicate ticker. Try again.")
        continue

    buy_price = float(input("Enter buying price: "))
    quantity = int(input("Enter quantity of shares: "))
    current_price = float(input("Enter current market price: "))

    if buy_price <= 0 or quantity <= 0 or current_price < 0:
        print("Invalid price or quantity. Skipping stock.")
        continue

    portfolio[ticker] = {
        "buy_price": buy_price,
        "quantity": quantity,
        "current_price": current_price
    }

# Step 3: Calculate portfolio values
total_invested = 0
total_value = 0

print("\n======================================")
print("          PORTFOLIO SUMMARY")
print("======================================")

for ticker, details in portfolio.items():

    invested = details["buy_price"] * details["quantity"]

    current_value = details["current_price"] * details["quantity"]

    profit = current_value - invested

    percentage = (profit / invested) * 100

    total_invested += invested
    total_value += current_value

    print("\nStock:", ticker)
    print("Buying Price:", details["buy_price"])
    print("Quantity:", details["quantity"])
    print("Current Price:", details["current_price"])
    print("Invested Amount:", round(invested, 2))
    print("Current Value:", round(current_value, 2))
    print("Profit/Loss:", round(profit, 2))
    print("Gain/Loss:", round(percentage, 2), "%")

# Step 4: Calculate total portfolio profit/loss
total_profit = total_value - total_invested

if total_invested > 0:
    total_percentage = (total_profit / total_invested) * 100
else:
    total_percentage = 0

print("\n======================================")
print("        TOTAL PORTFOLIO VALUE")
print("======================================")

print("Total Invested:", round(total_invested, 2))
print("Current Portfolio Value:", round(total_value, 2))
print("Total Profit/Loss:", round(total_profit, 2))
print("Total Gain/Loss:", round(total_percentage, 2), "%")

# Step 5: Save details into CSV file
filename = "portfolio_summary.csv"

file_exists = os.path.exists(filename) and os.path.getsize(filename) > 0

with open(filename, "a", newline="") as file:

    fieldnames = [
        "Ticker",
        "Buy Price",
        "Quantity",
        "Current Price",
        "Invested",
        "Current Value",
        "Profit/Loss",
        "Percentage"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    if not file_exists:
        writer.writeheader()

    for ticker, details in portfolio.items():

        invested = details["buy_price"] * details["quantity"]

        current_value = details["current_price"] * details["quantity"]

        profit = current_value - invested

        percentage = (profit / invested) * 100

        writer.writerow({
            "Ticker": ticker,
            "Buy Price": details["buy_price"],
            "Quantity": details["quantity"],
            "Current Price": details["current_price"],
            "Invested": invested,
            "Current Value": current_value,
            "Profit/Loss": profit,
            "Percentage": percentage
        })

print("\nPortfolio summary saved successfully!")
print("CSV File:", filename)

print("\nThank you for using Portfolio Tracker!")
