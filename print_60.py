import time

def print_60():
    for x in range(60):
        print time.time()
        time.sleep(1)

print_60()
