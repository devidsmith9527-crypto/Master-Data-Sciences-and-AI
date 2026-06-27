def mutual_friends(graph, user1, user2):
    friends1 = set(graph.get(user1, []))
    friends2 = set(graph.get(user2, []))
    return list(friends1 & friends2)


g = {"Sok": ["Lim", "Dara", "Bopha"], "Lim": ["Sok", "Dara"]}
print("មិត្តរួមគ្នារវាង Sok និង Lim:", mutual_friends(g, "Sok", "Lim"))
