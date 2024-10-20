import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import random

prev_moves = pd.DataFrame(columns=["Move_selected","Win", "Loss", "Draw"])
prev_results = pd.DataFrame(columns=["comp_move"])
moves = {1: "rock", 2: "paper", 3: "scissor"}
# 1 b 3, 3 b 2, 2b1 
#player moves:
running = True  
move_no = 0


def comp_move(prev_moves, prev_results, Curr_moves):
    X = prev_moves
    y = prev_results    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
    knn = KNeighborsClassifier(n_neighbors=2)
    knn.fit(X_train, y_train)
    #parameters_df = pd.DataFrame([parameters], columns=['Skin Tone', 'Gender', 'Temperature (°C)', 'Season', 'Occasion'])



while running:
    move_no += 1
    p_move = int(input("What move do you want to play?: \n 1: Rock \n 2: Paper \n 3: scissors \n 4: Quit game \n Select using the numbers: "))
    if p_move == 4:
        break
    if move_no <= 10: 
        c_move = random.randint(1,3)
    else: 
        c_move = comp_move(prev_moves, prev_results)
    win_cond = p_move == 1 and c_move == 3 or p_move == 2 and c_move == 1 or p_move == 3 and c_move == 2
    if p_move == c_move:
        print("This turn ended in a draw")
    elif win_cond:
        print("You won this turn")
    else:
        print("You lost this turn")
    prev_moves[move_no] = [p_move, win_cond,not p_move == c_move and win_cond, p_move == c_move  ]
    prev_results[move_no] =  [c_move]
    
