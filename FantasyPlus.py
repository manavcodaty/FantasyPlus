import pandas as pd

def create_f1_team():
    df = pd.read_csv("f1.csv")
    print(df)
    team = input("Enter team name: ")
    driver1 = input("Enter Driver 1: ")
    driver2 = input("Enter Driver 2: ")
    engine = input("Enter Engine Manufacturer: ")
    
    
    
    


    


def f1():
    print("Welcome to F1 FantasyPlus!")
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
    print("Welcome to Cricket FantasyPlus!")
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






def start():
    print("Welcome to FantasyPlus!")
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