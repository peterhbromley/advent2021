from collections import defaultdict


def read_input(filename):
    with open(filename) as f:
        return [int(x) for x in f.readline().strip().split(",")]


def update_timers(timers):
    new_timers = []
    num_to_add = 0
    for timer in timers:
        if timer == 0:
            new_timers.append(6)
            num_to_add += 1
        else:
            new_timers.append(timer - 1)

    return new_timers + [8 for _ in range(num_to_add)]


def update_timers_better(timer_dict):
    new_timer_dict = {}
    for i in range(1, 9):
        new_timer_dict[i - 1] = timer_dict[i]
    new_timer_dict[6] += timer_dict[0]
    new_timer_dict[8] = timer_dict[0]

    return new_timer_dict


state = read_input("input.txt")
timer_counts = defaultdict(int)
for timer in state:
    timer_counts[timer] += 1

for i in range(256):
    timer_counts = update_timers_better(timer_counts)
    if i == 79:
        problem1 = sum(timer_counts.values())
    elif i == 255:
        problem2 = sum(timer_counts.values())

print(f"Problem 1: {problem1}")
print(f"Problem 2: {problem2}")
