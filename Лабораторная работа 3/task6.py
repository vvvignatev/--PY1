list_numbers = [2, 90, -2, 8, -36, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

maxindex_ = 0
maxvalue_ = list_numbers[maxindex_]
for i, value in enumerate(list_numbers):
    if value >= maxvalue_:
        maxindex_ = i
        maxvalue_ = list_numbers[maxindex_]
list_numbers[-1], list_numbers[maxindex_] = list_numbers[maxindex_], list_numbers[-1]
print(list_numbers)  # Ответ [2, 90, -2, 8, -36, -44, -1, -85, -14, 25, -22, -90, -100, -8, 38, -92, -45, 67, 53, 90]
