class Solution:
    def main(self):
        products, k_box = input("Enter Input : ").split('/')
        
        products    = list(map(int, products.split()))
        k_box       = int(k_box)

        low         = max(products)
        high        = sum(products)
        result      = high

        while low <= high:
            mid = (low + high) // 2
            if self.is_dividable(products, k_box, mid):
                result  = mid
                high = mid - 1                   #Try smaller result
            else:
                low = mid + 1                    #Mid too low

        print(f"Minimum weigth for {k_box} box(es) = {result}")

    def is_dividable(self, weights, k, cap):
        box_used    = 1
        cur_sum     = 0

        for w in weights:
            if cur_sum + w <= cap:
                cur_sum += w            #Can add more
            else:
                box_used += 1           #Need more box
                cur_sum   = w
                if box_used > k:        #Use Too much boxes
                    return False
        return True

sol = Solution()
sol.main()
