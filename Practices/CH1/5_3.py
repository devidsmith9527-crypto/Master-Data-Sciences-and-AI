import time

arr = list(range(100000))  # arr មាន 100,000 ធាតុ

start = time.time()  # start = ពេលវេលាចាប់ផ្តើម
arr.append(-2)  # arr =
print(f"Append ចំណាយ: {time.time() - start:.6f} s")  # start =

start = time.time()
arr.insert(0, -1)  # Time O(n) ព្រោះត្រូវរុញកៅអី
print(f"Insert 0 ចំណាយ: {time.time() - start:.6f} s")
