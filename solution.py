import pandas as pd
import numpy as np


chat_id = 82953459 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    avg_shipments = np.mean(x)
    L = avg_shipments / 2
    return L
