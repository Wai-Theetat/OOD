def fibo(n, memo):
	for i in range(2, n + 1):
		memo[i] = memo[i - 1] + memo[i - 2]

def get_all_case(total_value):
	return [(a, total_value - a) for a in range(1, total_value // 2 + 1)]

def main():
	purity_req, weight_req = map(int, input("Purity and Weight needed: ").split())

	# Fibonacci-based variation constants
	variation_constants = [0] * (purity_req + 1)
	variation_constants[0] = 0
	variation_constants[1] = 1
	fibo(purity_req, variation_constants)

	# Initialize DP table
	dp = [{} for _ in range(purity_req + 1)]

	# Base case: purity = 1 → just weight itself (if ≥ 1)
	for w in range(1, weight_req + 1):
		dp[1][w] = w

	# Build up from purity = 2 to purity_req
	for purity in range(2, purity_req + 1):
		vc = variation_constants[purity - 1]
		for weight in range(1, weight_req + 1):
			comb_weight = 2 * weight - vc + 1
			best = -1
			for a, b in get_all_case(comb_weight):
				left = dp[purity - 1].get(a, -1)
				right = dp[purity - 1].get(b, -1)
				if left >= 0 and right >= 0:
					best = max(best, left + right)
			if best >= 0:
				dp[purity][weight] = best


	result = dp[purity_req].get(weight_req, -1)
	if result >= 0:
		print(f"Total weight of used minerals with Purity 1 : {result}")
	else:
		print("Total weight of used minerals with Purity 1 : -1")

main()
