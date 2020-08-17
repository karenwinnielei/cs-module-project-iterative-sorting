# if we increase input size, howmnay more steps does this function need to take?

my_list = [1, 2, 3, 4, 5]

def print_list(arr):
  for thing in arr:
    print(thing)

print_list(my_list) # 5 steps

longer_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print_list(longer_list) # 10 steps

# double input size
# doubled the steps
# one-to-one ratio!
# linear
# O(n)

def nested_loop(arr):
  for thing in arr:
    for other_thing in arr:
      print(thing, other_thing)

nested_loop(my_list) # takes 25 steps

nested_loop(longer_list) # takes 100 steps

nested_loop(list_100_long) # 10000 steps
# 100x steps

# doubled input size
# quadrupled the steps!
# two-to-four ratio
# quadratic time complexity

# Count all the steps
# Then calculate Big O

def my_func(arr):
  a = 1
  b = 2
  c = a * b

  for x in range(1000):
    print(x)
  
  for thing in arr:
    x = 10
    y = 20
    z = x * y
    print(thing)
  
  my_func(my_list)
  my_func(longer_list)

  # 3 + 1000 + 5
  # 3 + 1000 + 10
  # 3 + 1000 + len(arr)
  # 3 + 1000 + (4 * len(arr))

  # 3 + 1000 + (4 trillion)

  # O(n)

  # (3 + 1000 + (4 * n)) =>
  # (4n) ->
  # (n) ->
  # O(n) - linear line

  # "on the order of"
  # n, n^2, n^3

  def two_loops(arr):
    for x in range(10000000000):
      z = x * x
      print(z)

    for thing in arr:
      print(thing)

    for thing_again in arr:
      print(thing_again)

# Big O?

# Line by line walkthrough
## (big_num * 2) + len(arr) + len(arr)
## (big_num * 2) + (2 * len(arr))
# O(n)


def foo(n):
    sq_root = int(math.sqrt(n))
    for i in range(0, sq_root):
        print(i)

# 36 --> 6
# 100 --> 10
# 10000 --> 100
# O(log(n))

def bisect(n): # O(log(n))
  while n > 1:
    n = n/2
# 100
# 50
# 25
# 12.5
# 6.25
# 3.125
# ~1.575
# 


def bar(x):
    sum = 0
    for i in range(0, 1463):
        i += 1
        for j in range(0, x):
            for k in range(x, x + 15):
                sum += 1

# 1463 * (1 + n * (15 *1)))
# 1463 * (1 + 15n)
# 1463 + (1463 * 15n)
# O(n)

def baz(array):
    print(array[1])
    midpoint = len(array) // 2
    for i in range(0, midpoint):
        print(array[i])
    for _ in range(1000):
        print('hi')

# 1 + 1 + n/2 + 1000
# 1002 + n/2
# O(n/2)
# O(n)

## increase input size
## compare the increase in steps

def make_num_pairs(n):
    for num_one in range(n):
        for num_two in range(n):
            print(num_one, num_two)



def make_item_pairs(items):
    for item_one in items:
        for item_two in items:
            print(item_one, item_two)


def simple_recurse(n):
  if n <= 1:
    return n
  simple_recurse(n - 1)

simple_recurse(5) # 10 steps
# 5, 4, 3, 2, 1
simple_recurse(10) # 20 steps
# O(n)


def weird_recurse(n):
  if n <= 1:
    return n
  simple_recurse(n - 1)
  simple_recurse(n - 1)

# exponential: 2^n
