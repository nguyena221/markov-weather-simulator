import random
from collections import Counter

# Possible weather states
states = ["Sunny", "Cloudy", "Rainy", "Foggy", "Stormy", "Snowy"]

# Transition probabilities: P(next_weather | current_weather)
transition_poss = {
    "Sunny": {
        "Sunny": 0.4, "Cloudy": 0.2, "Rainy": 0.1, "Foggy": 0.1, "Stormy": 0.1, "Snowy": 0.1
    },
    "Cloudy": {
        "Sunny": 0.2, "Cloudy": 0.3, "Rainy": 0.2, "Foggy": 0.1, "Stormy": 0.1, "Snowy": 0.1
    },
    "Rainy": {
        "Sunny": 0.2, "Cloudy": 0.2, "Rainy": 0.3, "Foggy": 0.1, "Stormy": 0.1, "Snowy": 0.1
    },
    "Foggy": {
        "Sunny": 0.2, "Cloudy": 0.3, "Rainy": 0.2, "Foggy": 0.2, "Stormy": 0.05, "Snowy": 0.05
    },
    "Stormy": {
        "Sunny": 0.3, "Cloudy": 0.2, "Rainy": 0.2, "Foggy": 0.1, "Stormy": 0.1, "Snowy": 0.1
    },
    "Snowy": {
        "Sunny": 0.2, "Cloudy": 0.2, "Rainy": 0.1, "Foggy": 0.1, "Stormy": 0.1, "Snowy": 0.3
    }
}

# Choose the next weather state based on transition probabilities.
def get_next_weather(current_weather):
    next_states = list(transition_poss[current_weather].keys())
    prob = list(transition_poss[current_weather].values())
    choice = random.choices(next_states, weights=prob, k=1)[0]
    return choice

# Simulate weather for next couple of days (given)
def simulate_weather(start_weather, days):
    forecast = [start_weather]
    curr_we = start_weather

    for i in range(days - 1):
        curr_we = get_next_weather(curr_we)
        forecast.append(curr_we)

    return forecast

# Print the weather forecast 
def print_forecast(forecast):
    print("\nWeather Simulation")
    print("-" * 30)
    for i, weather in enumerate(forecast, start=1):
        print(f"Day {i}: {weather}")

    counts = Counter(forecast)
    print("\nSummary")
    print("-" * 30)
    for state in states:
        print(f"{state}: {counts[state]} day(s)")

def main():
    print("Markov Weather Simulator")

    # Get starting weather
    while True:
        start_weather = input("Enter starting weather: ").strip().title()
        if start_weather in states:
            break
        print("Invalid input.")

    # Get number of days
    while True:
        try:
            days = int(input("Enter number of days: "))
            if days > 0:
                break
            print("Must be positive.")
        except ValueError:
            print("Invalid number.")

    forecast = simulate_weather(start_weather, days)
    print_forecast(forecast)


if __name__ == "__main__":
    main()