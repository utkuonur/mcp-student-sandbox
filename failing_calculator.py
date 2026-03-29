def average_ratios(numbers):
    ratios = []
    for num in numbers:
        if num != 0:
            ratios.append(100 / num)
    if not ratios:
        raise ValueError("Cannot calculate average: all numbers are zero")
    return sum(ratios) / len(ratios)

print(average_ratios([10, 5, 0]))
