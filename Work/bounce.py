# bounce.py
#
# Exercise 1.5

height = 100
for bounce in range(1,11):
    height *= 3/5
    # print(bounce, height)
    # print(f"{bounce} {height:.4f}")
    print(f"{bounce} {round(height, 4)}")
