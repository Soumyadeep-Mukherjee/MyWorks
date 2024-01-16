def two_level_sort(scores):
    # Sort the list based on marks (Level-1) in ascending order and then by name (Level-2)
    sorted_scores = sorted(scores, key=lambda x: (x[1], x[0]))

    return sorted_scores
print(two_level_sort([('Harish', 80), ('Ram', 90), ('Harshita', 80)]))