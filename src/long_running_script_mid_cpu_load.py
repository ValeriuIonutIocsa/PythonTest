import time


while True:
    time.sleep(0.1)
    product = 1
    max_range = 1000_000
    print('computing product')
    for i in range(max_range):
        product *= i
    print('product computed')
