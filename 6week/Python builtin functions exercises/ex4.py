import time
import math

def okay(tims, root):
    time.sleep(tims/1000)
    return math.sqrt(root)

print("Sample Input:")
a = int(input())
b = int(input())
print("Sample Output:")
print(f"Square root of {a} after {b} miliseconds is {okay(b ,a)}")