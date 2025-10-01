def get_plate_comb(side_rq, plate_size):
	limit = 5

	def think(remain, comb, start):
		if remain == 0:
			return comb.copy()
		if remain < 0 or len(comb) >= limit:
			return None

		for i in range(start, len(plate_size)):
			plate = plate_size[i]
			comb.append(plate)
			result = think(remain - plate, comb, i)
			if result:
				return result
			comb.pop()
		return None

	return think(side_rq, [], 0)


def get_actions(prev_list, curr_list):
    actions = []
    
    #find how much plate that are same as old list
    common = 0
    while common < len(prev_list) and common < len(curr_list) and prev_list[common] == curr_list[common]:
        common += 1
        
    # Remove (PO) plates from top of old stack
    for plate in reversed(prev_list[common:]):
        actions.append(f"PO:{plate}")

    # Add (PU) plates to top of new stack
    for plate in curr_list[common:]:
        actions.append(f"PU:{plate}")

    return actions


def barbell_format(plates):
    # Calculate padding dashes dynamically, for nicer formatting
    # More plates -> fewer dashes
    base_dash = 5
    padding = max(0, base_dash - len(plates))
    left_dashes = '-' * padding
    right_dashes = '-' * padding

    left = "".join(f"[{p}]" for p in reversed(plates))
    right = "".join(f"[{p}]" for p in plates)
    
    return f"{left_dashes}{left}|======|{right}{right_dashes}"

def main():
	weights     = list(map(float,input("Enter needed weight(s): ").split()))
	weights		= [int(w) if w == int(w) else w for w in weights]
	plate_sizes = [25, 20, 15, 10, 5, 2.5, 1.25]
	bar_weight  = 20

	current_plates = []
 
	for target in weights:
		if target < bar_weight:
			print(f"It's impossible to achieve the weight you want({target}).")
			return

		side_rq = (target - bar_weight) / 2
		new_plates = get_plate_comb(side_rq, plate_sizes)

		if new_plates is None:
			print(f"It's impossible to achieve the weight you want({target}).")
			return

		actions = get_actions(current_plates, new_plates)

		has_float_plate = any(p != int(p) for p in new_plates)
		if has_float_plate:
			weight_str = f"{target:.1f}"
		else:
			weight_str = str(int(target)) if target == int(target) else str(target)

		if actions:
			print(" ".join(actions), end=" ")
			print(f"=> {barbell_format(new_plates)} => {weight_str} KG.")
		else:
			# No actions: print without leading =>
			print(f"{barbell_format(new_plates)} => {weight_str} KG.")

		current_plates = new_plates


main()



