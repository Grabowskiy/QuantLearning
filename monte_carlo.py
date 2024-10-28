
# MONTE CARLO SIMULATION FOR OPTION PRICING

import math
import numpy as np
import matplotlib.pyplot as plt

S0 = 100
K = 105
r = 0.06
sigma = 0.2
T = 1

rounds = 100000


def calculate_montecarlo(S0: float, K: float, T: float, o: float, r: float, call_or_not: bool = True) -> float:
    payoff = 0
    for i in range(1, rounds):
        St = S0 * math.exp((r - math.pow(o, 2)/2)*T + o*math.sqrt(T) *
        np.random.normal(0.0, 1.0))

        if call_or_not:
            payoff += max(St - K, 0.0)
        else:
            payoff += max(K - St, 0.0)

    option_price = math.exp(-r * T) * (payoff / rounds)
    return round(option_price, 4)


def simulate_paths(S0: float, K: float, T: float, o: float, r: float, num_paths: int, tims_steps: int):
    dt = T / time_steps
    paths = np.zeros((time_steps + 1, num_paths))
    paths[0] = S0

    for path in range(num_paths):
        for t in range(1, time_steps + 1):
            Z = np.random.normal(0.0, 1.0)
            paths[t, path] = paths[t-1, path] * math.exp((r - 0.5 * o ** 2) * dt + o * math.sqrt(dt) * Z)

    mean = np.mean(paths, axis=1)

    plt.figure(figsize=(12, 6))
    for path in range(num_paths):
        plt.plot(paths[:, path], lw=1)
    plt.plot(mean, color="blue", lw=3, linestyle="--")
    plt.xlabel("Time [days]")
    plt.ylabel("Asset price [$]")
    plt.title("Asset prices over time")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    call_price = calculate_montecarlo(S0, K, T, sigma, r)
    put_price =  calculate_montecarlo(S0, K, T, sigma, r, False)

    print(f"Call price calculated with monte carlo method: {call_price}")
    print(f"Put  price calculated with monte carlo method: {put_price}")

    time_steps = 360
    num_paths = 100
    paths = simulate_paths(S0, K, T, sigma, r, num_paths, time_steps)
