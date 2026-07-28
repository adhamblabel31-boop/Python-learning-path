# ----------------------------------------------------
#!------------- break , continue , pass --------------
# ----------------------------------------------------
nums = range(1, 11)

# ? continue --> skip current cycle if condition is true
for num in nums:
    if num == 6:
        continue
    print(num)

print("-" * 30)

# ? break --> stop loop if condition is true
for num in nums:
    if num == 6:
        break
    print(num)

print("-" * 30)

# ? pass --> continue and don't care --> i'll write condition later
for num in nums:
    if num == 5:
        pass
    print(num)
