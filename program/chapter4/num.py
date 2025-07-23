for i in range(1, 21):
    print(i)
"""for i in range(1, 1_000_000):
    print(i)"""
numbers = list(range(1, 1_000_001))
print(min(numbers))
print(max(numbers))
print(sum(numbers))
for i in range(1, 20, 2):
    print(i)
th = list(range(3, 31, 3))
for num in th:
    print(num)

cubic_num = [num ** 3 for num in range(1, 11)]
print(cubic_num)