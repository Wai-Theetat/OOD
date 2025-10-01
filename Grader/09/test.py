def quicksort(data, low, high):
    if low < high:
        p = partition(data, low, high)
        quicksort(data, low, p - 1)
        quicksort(data, p + 1, high)

def partition(data, low, high):
    pivot = data[high][1]   # pivot = price at the last element
    i = low - 1
    for j in range(low, high):
        if data[j][1] <= pivot:  # compare by price
            i += 1
            data[i], data[j] = data[j], data[i]
    data[i+1], data[high] = data[high], data[i+1]
    return i + 1

def print_items(data):
    for i, (name, price) in enumerate(data, start=1):
        print(f"{i:2}. {name:<12}{price:>4}")

# ---------------- MAIN ----------------
user_input = input("Enter Input : ")
items = []
for pair in user_input.split(","):
    name, price = pair.split()
    items.append((name, int(price)))

print("-" * 40)
print("Sort by price :")
quicksort(items, 0, len(items)-1)
print_items(items)
