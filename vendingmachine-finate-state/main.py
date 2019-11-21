import time
import random
from finite_state import finiteState
from threading import Thread

def choice(fs, item):
    print(f"Choice: {item}")
    fs.set_state(give_money)
    print("Price: {}".format(item + 1))
    time.sleep(7)
    return {"choice": 1, "price": item + 1} # choice = 0, price = 0+1

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
    if fs.variables["money"] >= fs.variables["price"]:
        fs.set_state(change)
        return fs.variables
    fs.set_state(give_money)
    return fs.variables

def change(fs, item):
    print("return money: {}".format(fs.variables["money"] - fs.variables["price"] ))
    fs.global_variables["revenue"] += fs.variables["price"]
    fs.set_state(dispense)
    time.sleep(3)
    return fs.variables

def dispense(fs, item):
    print(f"Dispense")
    fs.global_variables["rij"] = fs.global_variables["rij"] - 1
    fs.set_state(done)
    time.sleep(10)
    return {}

def done(fs, item):
    fs.set_state(choice)
    fs.stop = True
    print("Done")
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
        print("Revenue: {}".format(fs.global_variables["revenue"]))
        for i in range(0, fs.global_variables["rij"]):
            queue = queue + "🙃  "
        print(queue)
        time.sleep(30)
    
states = [
    choice,
    give_money,
    check_money,
    change,
    dispense,
    done
]
 # alfabet in FSM, staat ook gelijk aan product0 1 euro, product1 2 euro, en product2 3 euro. 
alfabet = [
    0, 1, 2
]

fs = finiteState(states)
fs.global_variables["rij"] = 0
fs.global_variables["revenue"] = 0
t = Thread(target=add_queue)
t.start()
t1 = Thread(target=run_fs)
t1.start()
run()
