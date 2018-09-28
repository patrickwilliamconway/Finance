from matplotlib import pyplot as plt
import numpy as np
import scipy as sp

def generate_random_returns(average_return, volatility, years):
    nums = np.random.rand(years)
    nums -= nums.mean()
    nums /= nums.std()
    nums *= volatility
    nums += average_return
    return nums

def model_returns(average_return, volatility, years, start = 1):
    nums = generate_random_returns(average_return, volatility, years)

    total = 1
    returns = []
    for n in nums:
        total *= 1.0 + n/100.0
        returns.append(total)
    plt.plot(range(start,years+start), returns, label = f"V:{volatility}")

    cagr = (np.power(total, (1./years)) - 1) *100

    print("Average Return:", average_return, "Volatility:", volatility, "CAGR:", cagr, "Multiplier:", total)

    total = 1
    returns = []
    
    for i in range(years):
        total *= 1.0 + cagr/100.0
        returns.append(total)
    #plt.plot(range(start,years+start), returns)

if __name__ == "__main__":
    years = 100
    plt.title("CAGR of Different Volatility Levels")
    plt.xlabel("Year")
    plt.ylabel("Return Multiplier (Average 7% Returns)")
    model_returns(7, 1, years)
    model_returns(7, 11.5, years)
    model_returns(7, 20, years)
    plt.legend()
    plt.show()
