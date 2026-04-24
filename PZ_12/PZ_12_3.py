def max_digit_sum(numbers):
    digit_sum = lambda x: sum(int(number) for number in str(x))

    return max(numbers, key=digit_sum)

numbers = [123, 456, 789, 234]
result = max_digit_sum(numbers)
print(result)
