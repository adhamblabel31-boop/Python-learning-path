# ------------------------------------------------------
#! ---------------- timing with timeit -----------------
# ------------------------------------------------------
# ? timeit: - get execution time of code by running 1m time and give you minimal time
# ?         - it used for performance by testing all functionality
# ? timeit(stmt, setup, timer, number)
# ? timeit(pass, pass, default, 1.000.000) <--  default values
#  ------------------------------------------------------
# ? stmt: code you want to measure the execution time
# ? setup: setup done before the code execution (import module or anything)
# ? timer: the timer value
# ? number: how many execution that will run
# -------------------------------------------------------
import timeit, random

# print(dir(timeit))

print(timeit.timeit("'Adham' * 1000"))

# define variable and use it in timeit
# print("Adham\n"*1000)
print(timeit.timeit("name = 'Adham'; name * 1000"))

# use setup to import module and use it in timeit
print(timeit.timeit(stmt="random.randint(0,50)", setup="import random"))


# use setup to import module and use it in timeit and repeat it 5 times
# print(random.randint(0,50)) <-- this is the code that will be executed in timeit
print(timeit.repeat(stmt="random.randint(0,50)", setup="import random", repeat=5))
