def rps(player1, player2):
    # your code here
    win_combo = {
        'rock': 'scissors',
        'scissors': 'paper',
        'paper': 'rock'
    }
    if player1 == player2:
        return 'Draw!'
    if win_combo[player1] == player2:
        return 'Player 1 won!'
    else:
        return 'Player 2 won!'
