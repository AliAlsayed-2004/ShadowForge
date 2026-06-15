import random

def generate_numbers(min_d, max_d, mode="random"):
    nums = []

    for length in range(min_d, max_d + 1):
        if mode == "random":
            for _ in range(50):
                nums.append(''.join(random.choices("0123456789", k=length)))

        elif mode == "sequence":
            for i in range(min(5000, 10 ** length)):
                nums.append(str(i).zfill(length))

    return nums