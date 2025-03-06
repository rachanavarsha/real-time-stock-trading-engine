import threading
import random
import time
import itertools
from collections import deque
import heapq
import ctypes

class AtomicInteger:
    """A lock-free integer using atomic operations."""
    def __init__(self, value=0):
        self.value = ctypes.c_int(value)
    
    def increment(self):
        with threading.Lock():
            self.value.value += 1
        return self.value.value

class Order:
    def __init__(self, order_id, order_type, ticker, quantity, price):
        self.order_id = order_id
        self.order_type = order_type  # 'BUY' or 'SELL'
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

    def __lt__(self, other):
        if self.order_type == 'BUY':
            return self.price > other.price  # Highest buy price first
        else:
            return self.price < other.price  # Lowest sell price first


class StockOrderBook:
    def __init__(self, ticker):
        self.ticker = ticker
        self.buy_orders = []  # Max-heap for Buy orders (use negation for min-heap behavior)
        self.sell_orders = []  # Min-heap for Sell orders
        self.lock = threading.Lock()

    def add_order(self, order):
        with self.lock:
            if order.order_type == 'BUY':
                heapq.heappush(self.buy_orders, order)
            else:
                heapq.heappush(self.sell_orders, order)
            
    def match_orders(self):
        with self.lock:
            trades = []
            while self.buy_orders and self.sell_orders and self.buy_orders[0].price >= self.sell_orders[0].price:
                buy_order = heapq.heappop(self.buy_orders)
                sell_order = heapq.heappop(self.sell_orders)
                
                trade_quantity = min(buy_order.quantity, sell_order.quantity)
                trades.append((buy_order.ticker, trade_quantity, sell_order.price))
                
                if buy_order.quantity > sell_order.quantity:
                    buy_order.quantity -= sell_order.quantity
                    heapq.heappush(self.buy_orders, buy_order)
                elif sell_order.quantity > buy_order.quantity:
                    sell_order.quantity -= buy_order.quantity
                    heapq.heappush(self.sell_orders, sell_order)
            return trades


class StockExchange:
    def __init__(self):
        self.order_id_counter = AtomicInteger()
        self.tickers = [StockOrderBook(f"TICKER_{i}") for i in range(1024)]
        self.lock = threading.Lock()

    def add_order(self, order_type, ticker_symbol, quantity, price):
        order_id = self.order_id_counter.increment()
        ticker_index = int(ticker_symbol.split('_')[-1])
        order = Order(order_id, order_type, ticker_symbol, quantity, price)
        self.tickers[ticker_index].add_order(order)

    def process_matching(self):
        for book in self.tickers:
            trades = book.match_orders()
            for trade in trades:
                print(f"Trade Executed: {trade}")




