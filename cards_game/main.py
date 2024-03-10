from CardGame import CardGame
import time

print("Welcome to the War ⚔️\nWar (also known as Battle in the United Kingdom) is a simple card game ♥️♦️♠️♣️\n"
      "typically played by two players using a standard playing card deck 🤼‍\n"
      "The objective of the game is to win all of the cards 🥇\nIn this game, "
      "the player with higher number of cards at the end of 10 rounds is the winner 🏆\nGood luck 🤝\n")


# Create a new instance of the CardGame class by taking inputs for player names and initial card numbers
game = CardGame(input("Enter first player name: "), 20, input("Enter second player name: "), 20)


# Print the cards of the first player
print(f"\n{game.player1.name} hand: \n")
for card in game.player1.cards:
    time.sleep(1)
    print(card)


# Print the cards of the second player
print(f"\n{game.player2.name} hand: \n")
for card in game.player2.cards:
    time.sleep(1)
    print(card)


# Print the game moves
print("\n")
print("game moves:\n")

# Creation of list of the cards been played
played_cards = []

# Play 10 rounds of the game
for i in range(10):

    # Print the move number
    print(f"move {i+1} 🎲")

    # Using get_card to play card against card
    player1_card = game.player1.get_card()
    player2_card = game.player2.get_card()

    # Using while loop to ensure the same card will not play again next round
    while player1_card in played_cards:
        # Add the card back to player hand
        game.player1.add_card(player1_card)
        # Get different card
        player1_card = game.player1.get_card()
    else:
        # Append it to a list, so it will not appear next round
        played_cards.append(player1_card)

    # Same for second player
    while player2_card in played_cards:
        game.player2.add_card(player2_card)
        player2_card = game.player2.get_card()
    else:
        played_cards.append(player2_card)

    # Player 1 wins the round
    if player1_card > player2_card:
        game.player1.add_card(player1_card)
        game.player1.add_card(player2_card)
        print(f"{game.player1.name} card is: {player1_card}")
        print(f"{game.player2.name} card is: {player2_card}")
        print(f"{game.player1.name} won this round\n")

    # Player 2 wins the round
    else:
        game.player2.add_card(player1_card)
        game.player2.add_card(player2_card)
        print(f"{game.player1.name} card is: {player1_card}")
        print(f"{game.player2.name} card is: {player2_card}")
        print(f"{game.player2.name} won this round\n")

    # Waiting between rounds to build tension
    time.sleep(3)

# Determine the winner of the game and print the player details
if game.get_winner() is not None:
    print(game.get_winner())
else:
    print("The game ended with incredible tie!")
