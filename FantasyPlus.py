import pandas as pd

def create_f1_team():
    df = pd.read_csv("f1.csv")
    print(df)
    team = input("Enter team name: ")
    driver1 = input("Enter Driver 1: ")
    driver2 = input("Enter Driver 2: ")
    engine = input("Enter Engine Manufacturer: ")
    chassis = input("Enter Chassis: ")
    car = input("Enter Car: ")
    
    dict = {"Team": team, 
            "Driver 1": driver1, 
            "Driver ": driver2, 
            "Engine Manufacturer": engine, 
            "Chassis": chassis, 
            "Car": car
            }
    
    temp = pd.DataFrame.from_dict(dict, orient='index')
    temp.to_csv("f1_teams_choices.csv", mode='a', header=False)
    
    
    
    


    


def f1():
    print("----------Welcome to F1 FantasyPlus!----------")
    print("1. Create Team")
    print("2. Edit Team")
    print("3. View Team")
    choice = int(input())
    if choice == 1:
        create_f1_team()
    elif choice == 2:
        edit_team()
    elif choice == 3:
        view_team()
    else:
        print("Invalid choice")
        f1()
    


def cricket():
    print("----------Welcome to Cricket FantasyPlus!----------")
    print("1. IPL")
    print("2. T20 World Cup")
    print("3. ODI World Cup")
    choice = int(input())
    
    if choice == 1:
        ipl()
    elif choice == 2:
        t20()
    elif choice == 3:
        odi()
    else:
        print("Invalid choice")
        cricket()
        
def create_nba_team():
    df = pd.read_csv("nba.csv")
    print(df)
    team = input("Enter team name: ")
    player1 = input("Enter Player 1: ")
    player2 = input("Enter Player 2: ")
    player3 = input("Enter Player 3: ")
    player4 = input("Enter Player 4: ")
    player5 = input("Enter Player 5: ")
    
    dict = {"Team": team, 
            "Player 1": player1, 
            "Player 2": player2, 
            "Player 3": player3, 
            "Player 4": player4, 
            "Player 5": player5
            }
    
    temp = pd.DataFrame.from_dict(dict, orient='index')
    temp.to_csv("nba_teams_choices.csv", mode='a', header=False)
        
def nba():
    print("----------Welcome to NBA FantasyPlus!----------")
    print("1. Create Team")
    print("2. Edit Team")
    print("3. View Team")
    choice = int(input())
    if choice == 1:
        create_nba_team()
    elif choice == 2:
        edit_team()
    elif choice == 3:
        view_team()
    else:
        print("Invalid choice")
        nba()
        
        
def basketball():
    print("----------Welcome to Basketball FantasyPlus!----------")
    print("NBA loading.....")
    nba()






def start():
    print("----------Welcome to FantasyPlus!----------")
    print("1. Cricket")
    print("2. F1")
    print("3. Basketball")
    choice = int(input())
    
    if choice == 1:
        cricket()
    elif choice == 2:
        f1()
    elif choice == 3:
        basketball()
    else:
        print("Invalid choice")
        start()