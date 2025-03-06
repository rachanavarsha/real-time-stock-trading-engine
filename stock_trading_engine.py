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


