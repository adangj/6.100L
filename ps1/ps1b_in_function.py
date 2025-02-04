def part_b(yearly_salary, portion_saved, cost_of_dream_home, semi_annual_raise):
	#########################################################################
	portion_down_payment = 0.25
	amount_saved = 0
	r = 0.05
	down_payment = portion_down_payment * cost_of_dream_home
	monthly_savings = portion_saved * yearly_salary / 12
	months = 0
	
	###############################################################################################
	## Determine how many months it would take to get the down payment for your dream home below ##
	###############################################################################################
	while amount_saved < down_payment:
	    amount_saved += monthly_savings + amount_saved * (r / 12)
	    months += 1
	    if months % 6 == 0:
	        monthly_savings *= 1 + semi_annual_raise
	print(f"Number of months: {months}")
	return months