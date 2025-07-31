from .game import CardGame
import time
import click

@click.command()
@click.option('--player1', prompt='Enter first player name')
@click.option('--player2', prompt='Enter second player name')
@click.option('--rounds', default=10, show_default=True, help='Number of rounds to play')
def start(player1, player2, rounds):
    click.echo("Welcome to the War ⚔️\nWar (also known as Battle in the United Kingdom) is a simple card game ♥️♦️♠️♣️\n"
               "typically played by two players using a standard playing card deck 🤼‍\n"
               "The objective of the game is to win all of the cards 🥇\nIn this game, "
               "the player with higher number of cards at the end of the rounds is the winner 🏆\nGood luck 🤝\n")

    game = CardGame(player1, 20, player2, 20)

    click.echo(f"\n{game.player1.name} hand: \n")
    for card in game.player1.cards:
        time.sleep(1)
        click.echo(card)

    click.echo(f"\n{game.player2.name} hand: \n")
    for card in game.player2.cards:
        time.sleep(1)
        click.echo(card)

    click.echo("\nGame moves:\n")

    played_cards = []

    for i in range(rounds):
        click.echo(f"Move {i + 1} 🎲")

        player1_card = game.player1.get_card()
        player2_card = game.player2.get_card()

        while player1_card in played_cards:
            game.player1.add_card(player1_card)
            player1_card = game.player1.get_card()
        else:
            played_cards.append(player1_card)

        while player2_card in played_cards:
            game.player2.add_card(player2_card)
            player2_card = game.player2.get_card()
        else:
            played_cards.append(player2_card)

        if player1_card > player2_card:
            game.player1.add_card(player1_card)
            game.player1.add_card(player2_card)
            click.echo(f"{game.player1.name} card is: {player1_card}")
            click.echo(f"{game.player2.name} card is: {player2_card}")
            click.echo(f"{game.player1.name} won this round\n")
        else:
            game.player2.add_card(player1_card)
            game.player2.add_card(player2_card)
            click.echo(f"{game.player1.name} card is: {player1_card}")
            click.echo(f"{game.player2.name} card is: {player2_card}")
            click.echo(f"{game.player2.name} won this round\n")

        time.sleep(3)

    winner = game.get_winner()
    if winner is not None:
        click.echo(winner)
    else:
        click.echo("The game ended with incredible tie!")


if __name__ == '__main__':
    start()
