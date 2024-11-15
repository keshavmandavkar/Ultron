import requests
import pandas as pd

# Constants
API_KEY = 'SCHJLM4S2BQEZKJS'
BASE_URL = 'https://www.alphavantage.co/query'

# Portfolio class
class StockPortfolio:
    def __init__(self):
        self.portfolio = []

    def add_stock(self, symbol, quantity):
        
        for stock in self.portfolio:
            if stock['symbol'] == symbol:
                stock['quantity'] += quantity
                print(f"Updated {symbol} with additional {quantity} shares.")
                return
        
        self.portfolio.append({'symbol': symbol, 'quantity': quantity})
        print(f"Added {quantity} shares of {symbol} to portfolio.")

    def remove_stock(self, symbol, quantity):
        for stock in self.portfolio:
            if stock['symbol'] == symbol:
                if stock['quantity'] > quantity:
                    stock['quantity'] -= quantity
                    print(f"Removed {quantity} shares of {symbol}.")
                elif stock['quantity'] == quantity:
                    self.portfolio.remove(stock)
                    print(f"Removed all shares of {symbol}.")
                else:
                    print(f"Error: You don't have enough shares of {symbol} to remove.")
                return
        print(f"Error: {symbol} not found in portfolio.")

    def get_stock_price(self, symbol):
        
        try:
            response = requests.get(f"{BASE_URL}?function=GLOBAL_QUOTE&symbol={symbol}&apikey={API_KEY}")
            data = response.json()
            return float(data['Global Quote']['05. price'])
        except Exception as e:
            print(f"Error fetching price for {symbol}: {e}")
            return None

    def track_portfolio(self):
        if not self.portfolio:
            print("Portfolio is empty.")
            return

        
        portfolio_data = {
            'Symbol': [],
            'Quantity': [],
            'Current Price': [],
            'Total Value': []
        }

        total_portfolio_value = 0

        for stock in self.portfolio:
            price = self.get_stock_price(stock['symbol'])
            if price:
                quantity = stock['quantity']
                total_value = price * quantity
                portfolio_data['Symbol'].append(stock['symbol'])
                portfolio_data['Quantity'].append(quantity)
                portfolio_data['Current Price'].append(price)
                portfolio_data['Total Value'].append(total_value)
                total_portfolio_value += total_value

        
        df = pd.DataFrame(portfolio_data)
        print("\nCurrent Portfolio:")
        print(df)
        print(f"\nTotal Portfolio Value: ${total_portfolio_value:.2f}")


def main():
    portfolio = StockPortfolio()
    
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. Track Portfolio")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            symbol = input("Enter the stock symbol (e.g., AAPL, TSLA): ").upper()
            quantity = int(input("Enter the quantity: "))
            portfolio.add_stock(symbol, quantity)
        elif choice == '2':
            symbol = input("Enter the stock symbol to remove: ").upper()
            quantity = int(input("Enter the quantity to remove: "))
            portfolio.remove_stock(symbol, quantity)
        elif choice == '3':
            portfolio.track_portfolio()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
