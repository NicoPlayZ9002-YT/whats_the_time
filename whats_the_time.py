import time,sys

def give_time(formatted=True, time_format=24):
	curr: float = time.time()
	if formatted == True:
		curr_time = time.localtime(curr)
		if time_format == 24:
			return time.strftime("%H:%M:%S", curr_time)
		elif time_format == 12:
			return time.strftime("%I:%M:%S %p", curr_time)
		else:
			print("ArgError: time_format must be 24 or 12")
			sys.exit(127)
	else:
		return curr
