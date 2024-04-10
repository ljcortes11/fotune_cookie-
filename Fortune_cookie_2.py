import random

# Generating 6 unique random numbers for the lotto
lucky_numbers = random.sample(range(1, 55), 6)

# List of fortunes
fortune_list = [
    "You will have a great day today",
    "You will find a new friend",
    "You will find love",
    "You will win the lottery",
    "You will have a great job",
    "You will make more money"
]

# Print a random fortune
print(random.choice(fortune_list))
# Print the lucky numbers
print("Lucky numbers: ", lucky_numbers)
