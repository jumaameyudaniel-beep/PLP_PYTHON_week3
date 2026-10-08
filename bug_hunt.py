count = 1
total = 0

# BUG: The while statement was missing a colon (:), so I added it.

while count < 6:
# BUG: The loop originally stopped at 4 because it used count < 5. I changed it to count < 6 so that 5 is included.
total = total + count
count = count + 1

# BUG: total is an integer, so I used an f-string instead of adding it directly to a string.

print(f"Sum of 1 to 5 is: {total}")
