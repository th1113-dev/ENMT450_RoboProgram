import time as tic

state = 0

for i in range(5):
 state = not state #The ! operator does not work. Use not instead
 tic.sleep(0.5)
 print(f"state: {state}") 
 # f stands for f-string. Allows everything in brackets to be replaced with their value