import time
import random
from finite_state import finiteState
from threading import Thread

def choice(fs, item):
    print(f"Choice: {item}")
    if item == 1:
        fs.set_state(give_money)
        return {"choice": 1}
    return {}

def give_money(fs, item):
    data = fs.variables
    if "money" in data:
        data["money"] += item
    else:
        data["money"] = item

    print(f"Give money: {item}")
    fs.set_state(check_money)
    time.sleep(5)
    return data

def check_money(fs, item):
    if fs.variables["money"] == 2:
        fs.set_state(dispense)
        return {}
    fs.set_state(give_money)
    return fs.variables

def dispense(fs, item):
    print(f"Dispense")
    fs.global_variables["rij"] = fs.global_variables["rij"] - 1
    fs.set_state(choice)
    fs.stop = True
    return {}

def run_fs():
    fs.run(alfabet)

# run functions
def run():
    while True:
        time.sleep(5)
        if fs.stop and fs.global_variables["rij"] > 0:
            fs.stop = False
            t2 = Thread(target=run_fs)
            t2.start()
        
def add_queue():
    while True:
        fs.global_variables["rij"] += 1
        queue = "Rij 🧃 : "
        for i in range(0, fs.global_variables["rij"]):
            queue = queue + "🙃  "
        print(queue)
        time.sleep(10)
    
states = [
    choice,
    give_money,
    check_money,
    dispense,
]

alfabet = [
    0, 1
]

fs = finiteState(states)
fs.global_variables["rij"] = 0
t = Thread(target=add_queue)
t.start()
t1 = Thread(target=run_fs)
t1.run()
run()