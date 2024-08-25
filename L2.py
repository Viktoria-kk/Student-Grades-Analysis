
def apply_operation(numbers, operation):
    return [operation(number) for number in numbers if operation(number) is not None]


list = [1, 2, 3, 4, 5]
print(f"Input: {list}  Doubled: {apply_operation(list, lambda n: n * 2)}")
print(f"Input: {list}  Squared: {apply_operation(list, lambda num: num ** 2)}")
print(f"Input: {list}  Odd Numbers: {apply_operation(list,lambda number: number if number % 2 != 0 else None)}")

