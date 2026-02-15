import csv

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 300
}

def calculate_portfolio():
    portfolio = {}
    total_investment = 0

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()

        if stock == "DONE":
            break

        if stock in stock_prices:
            quantity = int(input("Enter quantity: "))
            portfolio[stock] = quantity
        else:
            print("Stock not available.")

    print("\n----- Portfolio Summary -----")
    for stock, quantity in portfolio.items():
        investment = stock_prices[stock] * quantity
        total_investment += investment
        print(f"{stock} - {quantity} shares = ${investment}")

    print(f"\nTotal Investment Value: ${total_investment}")

    # Save to CSV
    with open("portfolio_summary.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Stock", "Quantity", "Investment"])
        for stock, quantity in portfolio.items():
            writer.writerow([stock, quantity, stock_prices[stock] * quantity])

    print("Portfolio saved to portfolio_summary.csv")

calculate_portfolio()