from sys import stdin


def min_refills(distance, tank, stops):
    # write your code here
    current = 0
    count = 0
    while current <= stops:
        last = current
        while current <= stops and distance[current + 1] - distance[last] <= tank:
            current = current + 1
        if current == last:
            return -1
        if current <= stops:
            count = count + 1
    return count


if __name__ == '__main__':
    d, m, _, *stops = map(int, stdin.read().split())
    print(min_refills(d, m, stops))
