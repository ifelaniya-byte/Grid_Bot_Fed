# Grid Trading Bot

A comprehensive grid trading bot designed for automated trading on Jupiter DEX.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ifelaniya-byte/Grid_Bot_Fed.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Grid_Bot_Fed
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Copy the `.env.example` to `.env` and fill in your environment variables.
2. Run the bot:
   ```bash
   python main.py
   ```

## Structure

- `requirements.txt`: Python dependencies for the trading bot
- `.env.example`: Environment variables template
- `config.py`: Configuration management
- `main.py`: Main entry point for the trading bot
- `grid_strategy.py`: Grid trading strategy implementation
- `exchange_api.py`: Jupiter DEX API integration
- `risk_manager.py`: Risk management system
- `wallet_manager.py`: Wallet and balance management
- `database.py`: Local database for trades and history
- `utils.py`: Utility functions