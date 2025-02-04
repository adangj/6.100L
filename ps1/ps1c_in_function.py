def part_c(initial_deposit):
	#########################################################################
	cost_of_dream_house = 800000
	portion_down_payment = 0.25
	down_payment = cost_of_dream_house * portion_down_payment
	amount_saved = initial_deposit
	r = 0.5
	l = 0
	h = 1
	steps = 0
	
	##################################################################################################
	## Determine the lowest rate of return needed to get the down payment for your dream home below ##
	##################################################################################################
	if initial_deposit * ((13 / 12) ** 36) < down_payment:
	    r = None
	else:
	    while abs(down_payment - amount_saved) > 100:
	        amount_saved = initial_deposit * ((1 + r / 12) ** 36)
	        steps += 1
	        if down_payment > amount_saved:
	            l = r
	            r = (r + h) / 2
	        else:
	            h = r
	            r = (r + l) / 2
	print(f"Best savings rate: {r}")
	print(f"Steps in bisection search: {steps}")
	return r, steps