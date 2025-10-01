def fibo(n, vc):
	if vc[n] is None:
		vc[n] = fibo(n - 1, vc) + fibo(n - 2, vc)
	return vc[n]

def think(purity, weight, vc, alchem_table):
	if purity == 1:
		return weight if weight >= 1 else -1

	if alchem_table[purity] is None:
		alchem_table[purity] = {}

	if weight in alchem_table[purity]:
		return alchem_table[purity][weight]

	comb_weight = 2 * weight - vc[purity - 1] + 1

	a = 1
	result = -1

	# Use iteration to avoid recursion limit exceed
	# pick the first valid answer for time
	while a <= comb_weight // 2:
		b = comb_weight - a
		if a > b:
			break

		left = think(purity - 1, a, vc, alchem_table)
		if left < 0:
			a += 1
			continue

		right = think(purity - 1, b, vc, alchem_table)
		if right < 0:
			a += 1
			continue

		result = left + right
		break

	alchem_table[purity][weight] = result
	return result

def main():
	purity_req, weight_req = map(int, input("Purity and Weight needed: ").split())

	vc = [None] * (purity_req + 1)
	vc[0] = 0
	vc[1] = 1
	fibo(purity_req, vc)

	alchem_table = [None] * (purity_req + 1)

	result = think(purity_req, weight_req, vc, alchem_table)

	if result >= 0:
		print("Total weight of used minerals with Purity 1 :", result)
	else:
		print("Total weight of used minerals with Purity 1 : -1")

main()
