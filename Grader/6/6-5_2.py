def fibo(n, memo):
	if not n in memo:
		memo[n] = fibo(n-1, memo) + fibo(n-2, memo)
	return memo[n]

#def get_all_case(total_value, a=1):
#	if a > total_value // 2:
#		return []
#	return [(a, total_value - a)] + get_all_case(total_value, a + 1)

def get_all_case(total_value):
	lst = []
	a = 1
	while a <= total_value // 2:
		lst.append((a, total_value - a))
		a += 1
	return lst


def max_from_case_list(cases, purity, vc, alchem_table, idx=0, current_best=-1):
	if idx >= len(cases):
		return current_best

	a, b = cases[idx]
	left = think(purity - 1, a, vc, alchem_table)
	right = think(purity - 1, b, vc, alchem_table)

	if left >= 0 and right >= 0:
		current_best = max(current_best, left + right)

	return max_from_case_list(cases, purity, vc, alchem_table, idx + 1, current_best)

def think(purity, weight, vc, alchem_table):
	if purity == 1:
		return weight if weight >= 1 else -1

	if alchem_table[purity] is None:
		alchem_table[purity] = {}

	if weight in alchem_table[purity].keys():
		return alchem_table[purity][weight]

	comb_weight = 2 * weight - vc[purity - 1] + 1

	best = -1
	cases = get_all_case(comb_weight)
 
	#best = max_from_case_list(cases, purity, vc, alchem_table)

	for a, b in cases:
		left = think(purity - 1, a, vc, alchem_table)
		right = think(purity - 1, b, vc, alchem_table)
		if left >= 0 and right >= 0:
			best = max(best, left + right)


	alchem_table[purity][weight] = best
	return best

def main():
	purity_req, weight_req = map(int, input("Purity and Weight needed: ").split())

	variation_constants = [None]*(purity_req + 1)
	variation_constants[0] = 0
	variation_constants[1] = 1
	fibo(purity_req, variation_constants)
	
	alchem_table = [None] * (purity_req + 1)
 
	result = think(purity_req, weight_req, variation_constants, alchem_table)

	if result >= 0:
		print("Total weight of used minerals with Purity 1 : ", result)
	else:
		print('Total weight of used minerals with Purity 1 : -1')

main()
