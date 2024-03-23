import heapq
import random


def minimum_connection_cost(lengths):
    # Create min-heap
    heapq.heapify(lengths)
    # Initialize total connection cost
    result = 0
    while len(lengths) > 1:
        # Get sum of 2 minimum elements (current cost) as new element
        current = heapq.heappop(lengths) + heapq.heappop(lengths)
        # Add current cost to total
        result += current
        # Return current cost to heap
        heapq.heappush(lengths, current)
    return result


if __name__ == "__main__":
    length_range = 10
    cable_lengths = list(
        [random.randint(length_range // 4, length_range) for _ in range(length_range)])
    print("Cable lengths:", cable_lengths)
    print("Minimum connection cost:", minimum_connection_cost(cable_lengths))
