def calculate_no_spades_probability(num_cards):
    """
    Calculate the probability that none of the drawn cards are spades.
    Returns a list of intermediate probabilities for 1 to num_cards.
    """
    total_cards = 52
    non_spades = 39

    probabilities = []
    cumulative_prob = 1.0

    for i in range(1, num_cards + 1):
        # Probability that the i-th card is not a spade
        # given that previous (i-1) cards were not spades
        remaining_non_spades = non_spades - (i - 1)
        remaining_total = total_cards - (i - 1)

        if remaining_non_spades < 0 or remaining_total < 0:
            # Can't draw more non-spade cards than exist
            return probabilities

        cumulative_prob *= remaining_non_spades / remaining_total
        probabilities.append((i, cumulative_prob))
        print (remaining_non_spades/remaining_total)
        
    return probabilities


def main():
    print("Spades Probability Calculator")
    print("=" * 50)
    print("Calculate the probability of drawing cards with no spades")
    print("from a standard 52-card deck (no jokers).\n")

    while True:
        user_input = input("How many cards to draw? (Enter 'q' or 0 to quit): ").strip()

        # Check for quit conditions
        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        try:
            num_cards = int(user_input)

            if num_cards == 0:
                print("Goodbye!")
                break

            if num_cards < 0:
                print("Please enter a positive number.\n")
                continue

            if num_cards > 39:
                print("Cannot draw more than 39 non-spade cards from the deck!\n")
                continue

            # Calculate and display probabilities
            probabilities = calculate_no_spades_probability(num_cards)

            print(f"\nProbabilities of drawing no spades:\n")
            print(f"{'Cards Drawn':<15} {'Probability':<20} {'Percentage'}")
            print("-" * 50)

            for cards, prob in probabilities:
                print(f"{cards:<15} {prob:<20.12f} {prob * 100:.12f}%")

            print("\n")

        except ValueError:
            print("Invalid input. Please enter a number or 'q' to quit.\n")


if __name__ == "__main__":
    main()
