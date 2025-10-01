class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"({self.key}, {self.value})"


class Solution:
    def main(self):
        print(" ***** Fun with hashing *****")
        raw_value, raw_data = input("Enter Input : ").split('/')

        table_size, max_collision = map(int, raw_value.strip().split())
        data_list = [tuple(item.strip().split()) for item in raw_data.strip().split(',')]

        table = [None] * table_size
        full_warning_printed = False

        for key, value in data_list:
            data = Data(key, value)
            hashed = self.hashing(key, table_size)
            inserted = False

            for i in range(max_collision):
                index = (hashed + i ** 2) % table_size

                if table[index] is None:
                    table[index] = data
                    inserted = True
                    break
                elif not full_warning_printed:
                    print(f"collision number {i+1} at {index}")

            if not inserted and not full_warning_printed:
                print("Max of collisionChain")

            if not full_warning_printed:
                self.print_table(table)

            if not full_warning_printed and all(slot is not None for slot in table):
                print("This table is full !!!!!!")
                full_warning_printed = True

    def hashing(self, key, size):
        return sum(ord(ch) for ch in key) % size

    def print_table(self, table):
        for i, item in enumerate(table):
            print(f"#{i+1}\t{item if item else 'None'}")
        print("---------------------------")

sol = Solution()
sol.main()
