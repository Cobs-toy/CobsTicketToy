import typer
import random

def today_num(i: int,k:int):
    a = random.randint(i,k)
    return a
    print(a)

def entry_point():
    typer.run(today_num)    
