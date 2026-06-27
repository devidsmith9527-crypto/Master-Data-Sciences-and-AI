import gc


class Node:
    pass


n1 = Node()
n2 = Node()
n1.ref = n2
n2.ref = n1  # ចង្អុលកន្ទុយគ្នាឯង (Cyclic)

del n1
del n2  # លុបឈ្មោះក្រៅ តែពួកវានៅចង្អុលគ្នា

collected = gc.collect()  # បង្ខំ GC ឱ្យបោសសម្អាតកាកសំណល់
print("ចំនួន Object ដែលលុបចោល:", collected)
