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

