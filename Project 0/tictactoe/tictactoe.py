"""
Tic Tac Toe Player
"""

import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1
    if count % 2 == 0:
        return 'X'
    else:
        return 'O' 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    ans = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                ans.add((i, j))
    return ans


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if len(action) != 2 or action[0] > 2 or action[1] > 2 or action[0] < 0 or action[1] < 0:
        raise Exception

    ans = copy.deepcopy(board)
    char = player(board)
    ans[action[0]][action[1]] = char

    return ans



def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    for i in range(3):
        if board[i][0] == 'X' and board[i][1] == 'X' and board[i][2] == 'X':
            return 'X'
        if board[i][0] == 'O' and board[i][1] == 'O' and board[i][2] == 'O':
            return 'O'

    for j in range(3):
        if board[0][j] == 'X' and board[1][j] == 'X' and board[2][j] == 'X':
            return 'X'
        if board[0][j] == 'O' and board[1][j] == 'O' and board[2][j] == 'O':
            return 'O'

    if board[0][0] == 'X' and board[1][1] == 'X' and board[2][2] == 'X':
        return 'X'
    if board[0][0] == 'O' and board[1][1] == 'O' and board[2][2] == 'O':
        return 'O'

    if board[0][2] == 'X' and board[1][1] == 'X' and board[2][0] == 'X':
        return 'X'
    if board[0][2] == 'O' and board[1][1] == 'O' and board[2][0] == 'O':
        return 'O'   
    
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    winnerr = winner(board)

    if winnerr != None:
        return True
    
    count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                count += 1

    if count == 9:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winnerr = winner(board)

    if winnerr == 'X':
        return 1
    elif winnerr == 'O':
        return -1
    else:
        return 0

def minn(board):
    if terminal(board):
        return utility(board)
    v = 2
    for action in actions(board):
        if maxx(result(board, action)) < v:
            v = maxx(result(board, action))
    return v

def maxx(board):
    if terminal(board):
        return utility(board)
    v = -2
    for action in actions(board):
        if minn(result(board, action)) > v:
            v = minn(result(board, action))
    return v

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None

    playerr = player(board)

    minimaxAns = tuple()

    if playerr == 'X':
        if terminal(board):
            return utility(board)
        v = -2
        for action in actions(board):
            if minn(result(board, action)) > v:
                v = minn(result(board, action))
                minimaxAns = action
    else:
        if terminal(board):
            return utility(board)
        v = 2
        for action in actions(board):
            if maxx(result(board, action)) < v:
                v = maxx(result(board, action))
                minimaxAns = action

    return minimaxAns