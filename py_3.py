# 1. List of squares of even numbers from 1 to 10
result = []
for n in range(1, 11):
    if n % 2 == 0:
        result.append(n * n)
print(result)

# 2. Dictionary of each word and its length
print({word: len(word) for word in ["ai", "python", "data"]})

# 3. Set of unique letters in "banana"
print({ch for ch in "banana"})