def hbd(age):
    for base in range(2, age):
        s = ""
        n = age
        while n > 0:
            s = str(n % base) + s
            n //= base
        if s == "20" or s == "21":
            return f"saimai is just {s}, in base {base}!"    
    return "No suitable base found"

year = int(input("Enter year : "))
print(hbd(year))