import random
import json
import os

ACTIONS = [
    "Send Notification",
    "Recommend Content",
    "Offer Discount",
    "Trigger Email"
]


Q_TABLE_FILE = "models/q_table.json"

#Load Q-table if exists
if os.path.exists(Q_TABLE_FILE):
    with open(Q_TABLE_FILE, "r") as f:
        Q = json.load(f)
else:
    Q = {}

def save_q_table():
    with open(Q_TABLE_FILE, "w") as f:
        json.dump(Q, f, indent=4)


def choose_action(user_segment):
    epsilon = 0.2  #exploration

    if user_segment not in Q:
        Q[user_segment] = {a: 0 for a in ACTIONS}

    #Explore
    if random.random() < epsilon:
        return random.choice(ACTIONS)

    #Exploit
    return max(Q[user_segment], key=Q[user_segment].get)

def update_q(user_segment, action, reward):
    lr = 0.1

    if user_segment not in Q:
        Q[user_segment] = {a: 0 for a in ACTIONS}

    Q[user_segment][action] += lr * (reward - Q[user_segment][action])

    save_q_table()