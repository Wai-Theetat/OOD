class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

def play_event(action: str):
    global enemies
    global actions
    event, value = action.split()
    killed = 0

    if value == '0':
        print("Invalid number")
        return

    if event == "spawn":
        print(f"spawn an enemy of {value} HP")
        enemies.push(int(value))
        print(enemies, end='\n\n')

    elif event == "dmg":
        value = int(value)
        print(f"deal {value} damage", end=', ')

        while value > 0 and not enemies.is_empty():
            enemy = enemies.pop()
            enemy -= value
            if enemy < 0:
                killed += 1
                value = -enemy
            elif enemy > 0:
                enemies.push(enemy)
                break
            else:
                killed += 1
                break

        print(f"killed {killed} enemy")
        print(enemies, end='\n\n')


def main():
    global enemies
    global actions
    raw = input("Enter Input : ")
    initial, raw_action = raw.split("/")

    for n in initial.split():
        if n == '0':
            continue
        enemies.push(int(n))

    for act in raw_action.split(","):
        actions.enqueue(act)

    print("\nstart")
    print(enemies, end='\n\n')

    while not actions.is_empty():
        play_event(actions.dequeue())

    if enemies.is_empty():
        print(">>>> Player Wins <<<<")

enemies = Stack()
actions = Queue()

main()
