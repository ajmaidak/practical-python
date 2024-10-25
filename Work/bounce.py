# bounce.py
#
# Exercise 1.5
#
# A rubber ball is dropped from a height of 100m and hits
# the ground it bounces back up 3/5 the height it fell
# pinrt a table showing the height of the first 10 bounces
#

height = 100
bounce_back = 3/5

for i in range(10):
    height *= bounce_back
    print(i+1, round(height, 4))
    