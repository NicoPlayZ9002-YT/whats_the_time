# whats_the_time
`whats_the_time` is a small Python module that lets you display the time, with 24h and AM/PM support.

## usage
```py
import whats_the_time as wtt
print(wtt.give_time(time_format=24)) # Prints time in 24H format
print(wtt.give_time(time_format=12)) # Prints time in AM/PM format
print(wtt.give_time(unix=True)) # Prints time in raw unix
```
