import csv
import yfinance as yf

def get_current_price(ticker):
    """
    Fetches the real-time or latest available closing price for a given stock ticker using yfinance.
    """
    try:
        stock = yf.Ticker(ticker)
        # Try to get the regular market price or the previous close price
        info = stock.info
        current_price = info.get('regularMarketPrice') or info.get('previousClose')
        
        if current_price:
            return round(float(current_price), 2)
        else:
            # Fallback if specific keys are missing
            history = stock.history(period="1d")
            if not history.empty:
                return round(float(history['Close'].iloc[-1]), 2)
            else:
                print(f"Warning: Could not fetch price for {ticker}. Returning $0.0")
                return 0.0
    except Exception as e:
        print(f"Error fetching data for {ticker}: {e}")
        return 0.0

def track_portfolio():
    portfolio = {}
    
    print("--- Investment Portfolio Tracker (LIVE API) ---")
    print("Enter your stock holdings. Type 'done' to finish.")
    
    while True:
        ticker = input("Enter Stock Ticker (e.g., AAPL): ").strip().upper()
        if ticker == 'DONE':
            break
            
        try:
            buy_price = float(input(f"Enter Buy Price for {ticker}: $"))
            shares = int(input(f"Enter Number of Shares for {ticker}: "))
            
            portfolio[ticker] = {
                'buy_price': buy_price,
                'shares': shares
            }
        except ValueError:
            print("Invalid input. Please enter numerical values for price and shares.")
            continue

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    print("\n--- Generating Portfolio Summary (Fetching Live Prices...) ---")
    
    summary_data = []
    total_invested = 0.0
    total_current_value = 0.0
    
    for ticker, data in portfolio.items():
        buy_price = data['buy_price']
        shares = data['shares']
        invested = buy_price * shares
        total_invested += invested
        
        # Fetching live price here!
        current_price = get_current_price(ticker)
        current_value = current_price * shares
        total_current_value += current_value
        
        profit_loss = current_value - invested
        pct_change = (profit_loss / invested) * 100 if invested > 0 else 0
        
        summary_data.append([
            ticker, shares, f"${buy_price:.2f}", f"${invested:.2f}", 
            f"${current_price:.2f}", f"${current_value:.2f}", 
            f"${profit_loss:.2f}", f"{pct_change:.2f}%"
        ])
        
        print(f"Ticker: {ticker} | Shares: {shares} | Invested: ${invested:.2f} | Current Value: ${current_value:.2f} | P/L: ${profit_loss:.2f} ({pct_change:.2f}%)")

    total_pl = total_current_value - total_invested
    total_pct_change = (total_pl / total_invested) * 100 if total_invested > 0 else 0

    print("\n--- Total Portfolio ---")
    print(f"Total Invested: ${total_invested:.2f}")
    print(f"Total Current Value: ${total_current_value:.2f}")
    print(f"Total Profit/Loss: ${total_pl:.2f} ({total_pct_change:.2f}%)")

    # Save to CSV
    csv_filename = 'portfolio_summary.csv'
    try:
        with open(csv_filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Ticker', 'Shares', 'Buy Price', 'Total Invested', 'Current Price', 'Current Value', 'Profit/Loss ($)', 'Profit/Loss (%)'])
            writer.writerows(summary_data)
            
            writer.writerow([])
            writer.writerow(['TOTAL', '', '', f"${total_invested:.2f}", '', f"${total_current_value:.2f}", f"${total_pl:.2f}", f"{total_pct_change:.2f}%"])
            
        print(f"\nPortfolio summary successfully saved to '{csv_filename}'.")
    except Exception as e:
        print(f"Error saving to CSV: {e}")

if __name__ == '__main__':
    track_portfolio()