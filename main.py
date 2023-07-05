import random

def roll_dice(num_dice):
    results = []
    for _ in range(num_dice):
        roll = random.randint(1, 6)
        results.append(roll)
    return results

def display_results(results):
    print("Dice rolls:")
    for roll in results:
        print(f"Dice: {roll}")
    print(f"Total: {sum(results)}")


while True:
        num_dice = int(input("Enter the number of dice to roll (or 0 to quit): "))
        if num_dice == 0:
            break
        results = roll_dice(num_dice)
        display_results(results)
        print()

