import time

def give_time(unix=False, time_format=24):
	curr: float = time.time()
	if not unix:
		curr_time = time.localtime(curr)
		if time_format == 24:
			return time.strftime("%H:%M:%S", curr_time)
		elif time_format == 12:
			return time.strftime("%I:%M:%S %p", curr_time)
		else:
			raise ValueError("time_format must be 24 or 12")
	else:
		return curr
