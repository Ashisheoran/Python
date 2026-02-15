import threading
import time
import yfinance as yf

# List of stock tickers to track
TICKERS = ["AAPL", "GOOGL", "TSLA", "MSFT", "AMZN"]

# Function to fetch and display stock price
def track_stock(ticker):
    while True:
        stock = yf.Ticker(ticker)
        price = stock.info.get("regularMarketPrice", "N/A")
        prev_price = stock.info.get("previousClose","N/A")
        valuation = stock.info.get("marketCap","N/A")
        sector = stock.info.get("sector","N/A")
        industry = stock.info.get("industry","N/A")

        print(f"{ticker}: ₹{price} .......previous close: {prev_price}......Company Valuation: {valuation}......sector: {sector}......industry: {industry}")
        time.sleep(5)  # Refresh every 5 seconds

def main():
    threads = []

    for ticker in TICKERS:
        t = threading.Thread(target=track_stock, args=(ticker,))
        t.daemon = True  # So program exits when main thread exits
        t.start()
        threads.append(t)

    print("📊 Tracking live stock prices. Press Ctrl+C to stop.\n")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Stopped tracking.")

if __name__ == "__main__":
    main()
