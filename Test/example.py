def simple_hash(key_string, array_size):
    total = 0
    for char in key_string:
        total += ord(char)  # យកតម្លៃ ASCII របស់អក្សរមួួយៗមកបូកបញ្ចូលគ្នា
    return total % array_size  # ចែកយកសំណល់ដើម្បីកុំឱ្យហួសទំហំ Array


print("ពាក្យ Sok ធ្លាក់ចូលប្រអប់ទី:", simple_hash("Sok", 20))
print("ពាក្យ Lim ធ្លាក់ចូលប្រអប់ទី:", simple_hash("Lim", 20))
