'''Individual Programming Assignment 3

70 points

This assignment will develop your ability to manipulate data.
'''

social_graph = {
    "@bongolpoc":{"first_name":"Joselito",
                  "last_name":"Olpoc",
                  "following":[
                  ]
    },
    "@joaquin":  {"first_name":"Joaquin",
                  "last_name":"Gonzales",
                  "following":[
                      "@chums","@jobenilagan"
                  ]
    },
    "@chums" : {"first_name":"Matthew",
                "last_name":"Uy",
                "following":[
                    "@bongolpoc","@miketan","@rudyang","@joeilagan"
                ]
    },
    "@jobenilagan":{"first_name":"Joben",
                   "last_name":"Ilagan",
                   "following":[
                    "@eeebeee","@joeilagan","@chums","@joaquin"
                   ]
    },
    "@joeilagan":{"first_name":"Joe",
                  "last_name":"Ilagan",
                  "following":[
                    "@eeebeee","@jobenilagan","@chums"
                  ]
    },
    "@eeebeee":  {"first_name":"Elizabeth",
                  "last_name":"Ilagan",
                  "following":[
                    "@jobenilagan","@joeilagan"
                  ]
    },
}   

def relationship_status(from_member, to_member, social_graph):
    '''Relationship Status.
    20 points.

    Let us pretend that you are building a new app.
    Your app supports social media functionality, which means that users can have
    relationships with other users.

    There are two guidelines for describing relationships on this social media app:
    1. Any user can follow any other user.
    2. If two users follow each other, they are considered friends.

    This function describes the relationship that two users have with each other.

    Please see "assignment-4-sample-data.py" for sample data. The social graph
    will adhere to the same pattern.

    Parameters
    ----------
    from_member: str
        the subject member
    to_member: str
        the object member
    social_graph: dict
        the relationship data

    Returns
    -------
    str
        "follower" if fromMember follows toMember,
        "followed by" if fromMember is followed by toMember,
        "friends" if fromMember and toMember follow each other,
        "no relationship" if neither fromMember nor toMember follow each other.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    
    if from_member in social_graph[to_member]["following"] and to_member in social_graph[from_member]["following"]:
        return "friends"
    elif from_member in social_graph[to_member]["following"]:
        return "followed by"
    elif to_member in social_graph[from_member]["following"]:
        return "follower"
    else:
        return "no relationship"
    
board1 = [
['X','X','O'],
['O','X','O'],
['O','','X'],
]

board2 = [
['X','X','O'],
['O','X','O'],
['','O','X'],
]

board3 = [
['O','X','O'],
['','O','X'],
['X','X','O'],
]

board4 = [
['X','X','X'],
['O','X','O'],
['O','','O'],
]

board5 = [
['X','X','O'],
['O','X','O'],
['X','','O'],
]

board6 = [
['X','X','O'],
['O','X','O'],
['X','',''],
]

board7 = [
    ['X', 'O', 'X', 'X'],
    ['', '', 'O', 'X'],
    ['O', 'O', 'O', 'X'],
    ['O', '', '', 'X']
]

board8 = [
    ['', '', '', '', 'O'],
    ['X', 'X', '', 'O', 'X'],
    ['X', 'O', 'O', 'O', 'X'],
    ['', 'O', '', '', 'X'],
    ['O', 'X', 'X', '', '']
]

board9 = [
    ['X', '', '', 'O', '', 'O'],
    ['', 'X', '', 'O', '', 'O'],
    ['O', '', 'X', 'O', '', ''],
    ['', 'O', '', 'X', '', 'O'],
    ['', '', 'X', 'O', 'X', ''],
    ['', '', 'X', 'O', '', 'X']
]

board10 = [
    ['', '', ''],
    ['', 'O', ''],
    ['', '', '']
]


def tic_tac_toe(board):
    '''Tic Tac Toe.
    25 points.

    Tic Tac Toe is a common paper-and-pencil game.
    Players must attempt to successfully draw a straight line of their symbol across a grid.
    The player that does this first is considered the winner.

    This function evaluates a tic tac toe board and returns the winner.

    Please see "assignment-4-sample-data.py" for sample data. The board will adhere
    to the same pattern. The board may by 3x3, 4x4, 5x5, or 6x6. The board will never
    have more than one winner. The board will only ever have 2 unique symbols at the same time.

    Parameters
    ----------
    board: list
        the representation of the tic-tac-toe board as a square list of lists

    Returns
    -------
    str
        the symbol of the winner or "NO WINNER" if there is no winner
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
 
    for row in board:  # check the row
        if "" not in row and len(set(row)) == 1:
            return row[0]
    for col in range(len(board)):  # check the column
        if "" not in [row[col] for row in board] and len(set(row[col] for row in board)) == 1:
            return board[0][col]
    # check the main diagonal
    if "" not in [board[i][i] for i in range(len(board))] and len(set(board[i][i] for i in range(len(board)))) == 1:
        return board[0][0]
    # check the anti-diagonal
    if "" not in [board[j][len(board) - 1 - j] for j in range(len(board))] and len(set(board[j][len(board) - 1 - j] for j in range(len(board)))) == 1:
        return board[0][len(board) - 1]
    return "NO WINNER"

legs = {
     ("upd","admu"):{
         "travel_time_mins":10
     },
     ("admu","dlsu"):{
         "travel_time_mins":35
     },
     ("dlsu","upd"):{
         "travel_time_mins":55
     }
}

legs = {
    ('a1', 'a2'): {
        'travel_time_mins': 10
    },
    ('a2', 'b1'): {
        'travel_time_mins': 10230
    },
    ('b1', 'a1'): {
        'travel_time_mins': 1
    }
}

def eta(first_stop, second_stop, route_map):
    '''ETA.
    25 points.

    A shuttle van service is tasked to travel along a predefined circlar route.
    This route is divided into several legs between stops.
    The route is one-way only, and it is fully connected to itself.

    This function returns how long it will take the shuttle to arrive at a stop
    after leaving another stop.

    Please see "mod-4-ipa-1-sample-data.py" for sample data. The route map will
    adhere to the same pattern. The route map may contain more legs and more stops,
    but it will always be one-way and fully enclosed.

    Parameters
    ----------
    first_stop: str
        the stop that the shuttle will leave
    second_stop: str
        the stop that the shuttle will arrive at
    route_map: dict
        the data describing the routes

    Returns
    -------
    int
        the time it will take the shuttle to travel from first_stop to second_stop
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    now = first_stop
    total_time = 0
    
    while now != second_stop: # hasn't arrived to destination yet
        if (now, second_stop) in route_map: # if this is true, there is a direct leg between now and the second stop so just add
            total_time = total_time + route_map[(now, second_stop)]['travel_time_mins'] 
            break
        else: # if not true then have to find the next stop
            next_stop = None
            for leg in route_map:
                if leg[0] == now:
                    next_stop = leg[1]
                    total_time += route_map[leg]['travel_time_mins']
                    now = leg[1]
                    break 
        if next_stop is None:
            # No direct leg or next stop found
            break 
            
    return total_time