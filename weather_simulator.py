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