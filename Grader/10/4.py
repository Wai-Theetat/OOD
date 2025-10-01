class Solution:
    def main(self):
        print(" ***** Rehashing *****")
        raw_val, raw_data = input("Enter Input : ").split('/')

        table_size = int(raw_val.split()[0])
        max_collision = int(raw_val.split()[1])
        threshold = int(raw_val.split()[2])

        data_list = list(map(int, raw_data.split()))
        table = [None] * table_size
        progression = []

        print("Initial Table :")
        self.print_table(table)

        for data in data_list:
            inserted = False
            table_current_size = len(table)
            print(f"Add : {data}")
            progression.append(data)

            if self.is_met_threshold(progression, table_current_size, threshold):
                print("****** Data over threshold - Rehash !!! ******")
                extended_table_size = self.find_next_prime(2 * table_current_size + 1, 4 * table_current_size)
                table = [None] * extended_table_size
                table = self.rehash(progression, table, max_collision)
                self.print_table(table)
                continue

            for i in range(max_collision):
                interested_slot = (data + (i ** 2)) % table_current_size

                if table[interested_slot] is None:
                    table[interested_slot] = data
                    inserted = True
                    break
                else:
                    print(f"collision number {i+1} at {interested_slot}")

            if not inserted:
                print("****** Max collision - Rehash !!! ******")
                extended_table_size = self.find_next_prime(2 * table_current_size + 1, 4 * table_current_size)
                table = [None] * extended_table_size
                table = self.rehash(progression, table, max_collision)

            self.print_table(table)

    def is_met_threshold(self, prog, mx, trhd):
        cur = len(prog)

        if (((cur/mx)*100) >= trhd):
            #print(cur, mx, cur/mx*100, trhd)
            return True
        else:
            return False

    def rehash(self, lstnum, table, max_collision):
        for num in lstnum:
            inserted = False
            table_size = len(table)
            for i in range(max_collision):
                interested_slot = (num + (i ** 2)) % table_size
                if table[interested_slot] is None:
                    table[interested_slot] = num
                    inserted = True
                    break
                else:
                    print(f"collision number {i+1} at {interested_slot}")
            if not inserted:
                print("****** Max collision - Rehash !!! ******")
                extended_table_size = self.find_next_prime(2 * table_size + 1, 4 * table_size)
                table = [None] * extended_table_size
                return self.rehash(lstnum, table, max_collision)  # recursive rehash
        return table

    def print_table(self, table):
        for i, item in enumerate(table):
            print(f"#{i+1}\t{item if item is not None else 'None'}")
        print("----------------------------------------")

    def find_next_prime(self, a, b):
        for p in range(a, b):
            if p < 2:
                continue
            for i in range(2, int(p ** 0.5) + 1):
                if p % i == 0:
                    break
            else:
                return p

sol = Solution()
sol.main()

