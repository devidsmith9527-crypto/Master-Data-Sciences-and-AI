import heapq


def dijkstra(graph, start):
    # កំណត់ចម្ងាយដំបូងទៅគ្រប់ទីតាំងទាំងអស់ជា អនន្ត (Infinity)
    distances = {node: float("inf") for node in graph}
    distances[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight
            # បើរាវរកឃើញផ្លូវដែលខ្លីជាង ធ្វើបច្ចុប្បន្នភាពចម្ងាយ
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# ឧទាហរណ៍ផែនទីតំបន់ និងចម្ងាយ (គិតជាគីឡូម៉ែត្រ) តំណាងឲ្យ Graph
map_graph = {
    "ផ្សារចាស់": {"វត្តបូព៌": 2, "Pub Street": 1},
    "វត្តបូព៌": {"ផ្សារចាស់": 2, "អង្គរវត្ត": 6},
    "Pub Street": {"ផ្សារចាស់": 1, "អង្គរវត្ត": 7},
    "អង្គរវត្ត": {"វត្តបូព៌": 6, "Pub Street": 7},
}

shortest_paths = dijkstra(map_graph, "ផ្សារចាស់")
print("ចម្ងាយខ្លីបំផុតពី [ផ្សារចាស់] ទៅទីតាំងផ្សេងៗ៖")
for location, distance in shortest_paths.items():
    print(f"- ទៅ {location}: {distance} គ.ម")
