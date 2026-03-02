import pickle
import logging
from datetime import datetime

# Configure logging
logging.basicConfig(level=logging.INFO, filename='trade_history.log',
                    format='%(asctime)s:%(levelname)s:%(message)s')

class DataHandler:
    def __init__(self, filename='trade_history.pkl'):
        self.filename = filename
        self.trades = self.load_trades()

    def load_trades(self):
        """Load trade history from a pickle file."""
        try:
            with open(self.filename, 'rb') as f:
                return pickle.load(f)
        except (FileNotFoundError, EOFError):
            return []

    def save_trades(self):
        """Save trade history to a pickle file."""
        with open(self.filename, 'wb') as f:
            pickle.dump(self.trades, f)
            logging.info('Trade history saved.')

    def add_trade(self, trade):
        """Add a new trade to the history and save it."""
        self.trades.append(trade)
        self.save_trades()
        logging.info(f'Trade added: {trade}')

    def get_trade_history(self):
        """Return the list of trades."""
        return self.trades

# Example usage
if __name__ == '__main__':
    dh = DataHandler()
    # Example trade
    dh.add_trade({'symbol': 'AAPL', 'action': 'buy', 'amount': 10, 'price': 150, 'timestamp': datetime.now()})
    print(dh.get_trade_history())