def read_input(filename):
    with open(filename) as f:
        return [l.strip() for l in f.readlines()]


def most_common_digit(numbers, position):
    return str(int(
        sum(num[position] == "1" for num in numbers) >= (len(numbers) // 2)
    ))


def least_common_digit(numbers, position):
    return str(int(
        sum(num[position] == "0" for num in numbers) > (len(numbers) // 2)
    ))


def search(numbers, digit_fn):
    for i in range(len(numbers[0])):
        digit = digit_fn(numbers, i)
        numbers = [num for num in numbers if num[i] == digit]
        if len(numbers) == 1:
            return numbers[0]

    assert False


numbers = read_input("input.txt")
gamma = "".join([most_common_digit(numbers, i) for i in range(len(numbers[0]))])
epsilon = "".join([str(int(not bool(int(d)))) for d in gamma])

print(f"Problem 1: {int(gamma, 2) * int(epsilon, 2)}")

oxygen = search(numbers, most_common_digit)
scrubber = search(numbers, least_common_digit)

print(f"Problem 2: {int(oxygen, 2) * int(scrubber, 2)}")
