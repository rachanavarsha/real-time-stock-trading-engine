# Real-Time Stock Trading Engine

##  Overview
This project is a high-performance real-time **Stock Trading Engine** that efficiently matches **BUY** and **SELL** orders using lock-free mechanisms and optimized data structures.

##  Features
- **Efficient Order Matching**: Uses a heap-based approach to match buy and sell orders in **O(n)** time complexity.
- **Lock-Free Atomic Order ID Generation**: Ensures fast and thread-safe order creation.
- **Multi-Ticker Support**: Handles up to **1,024 stock tickers** simultaneously.
- **Real-Time Trading Simulation**: Randomized order execution for realistic trading.
- **Thread-Safe & Optimized**: Uses per-ticker locking for high-performance concurrent trading.

##  How It Works
1. `add_order(order_type, ticker, quantity, price)`: Adds a **BUY** or **SELL** order to the system.
2. `match_orders()`: Matches orders based on **price priority** and executes trades.
3. **Concurrency Handling**: Orders are processed in a thread-safe manner without global locking.

