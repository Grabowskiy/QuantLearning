
# BLACK-SCHOLES-MERTON FORMULA FOR OPTIOONS PRICING

import math
from datetime import datetime
from scipy.stats import norm

STOCK_PRICE = 100
EXERCISE_PRICE = 100
EXERCISE_DATE = datetime(2024, 12, 20)
VOLATILTY = 0.2
RISK_FREE_INTEREST_RATE = 0.05


def calculate_maturity(exercise_date: datetime) -> float:
    return round((( exercise_date - datetime.now()).days) / 365.25, 4)


def calculate_call_option(S0: float, K: float, T_t:float, o: float, r: float) -> float:
    d1 = (math.log(S0/K) + (r+math.pow(o, 2)/2) * T_t) / (o * math.sqrt(T_t))
    d2 = d1 - o * math.sqrt(T_t)

    call_price = S0 * norm.cdf(d1) - K * math.exp(-r * T_t) * norm.cdf(d2)
    return call_price


def calculate_put_option(S0: float, K: float, T_t:float, o: float, r: float) -> float:
    d1 = (math.log(S0/K) + (r+math.pow(o, 2)/2) * T_t) / (o * math.sqrt(T_t))
    d2 = d1 - o * math.sqrt(T_t)

    put_price = K * math.exp(-r*T_t) * norm.cdf(-d2) - S0 * norm.cdf(-d1)
    return put_price


if __name__ == "__main__":
    S0 = STOCK_PRICE
    K = EXERCISE_PRICE
    T_t = calculate_maturity(EXERCISE_DATE)
    if T_t < 0:
        print("The exercise date should be later than today.")
        exit()

    o = VOLATILTY
    r = RISK_FREE_INTEREST_RATE

    print(f"The options call price is: {round(calculate_call_option(S0, K, T_t, o, r), 4)} $")
    print(f"The options put  price is: {round(calculate_put_option(S0, K, T_t, o, r), 4)} $")