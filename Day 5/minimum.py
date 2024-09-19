candidates_grades = [104, 28, 51, 29, 8, 26, 31, 64, 18, 133, 80, 60, 40, 134, 141, 81, 33, 125, 33, 137, 84, 83, 138, 8, 47, 73, 41, 10, 55, 147, 115, 116, 27, 11, 129, 54, 115, 113, 5, 90, 27, 118, 5, 33, 49, 69, 125, 126, 67, 20, 62, 106, 5, 142, 69, 49, 101, 108, 35, 118, 78, 91, 93, 66, 38, 114, 137, 35, 39, 104, 104, 110, 100, 76, 96, 127, 126, 30, 10, 136, 13, 93, 89, 39, 49, 55, 73, 40, 50, 122, 105, 7, 112, 11, 127, 44, 22, 102, 90, 112]

minimum = candidates_grades[0]

for candidate in candidates_grades:
    if(candidate < minimum):
        minimum = candidate

print(minimum)

maxim = candidates_grades[0]

for candidate in candidates_grades:
    if(candidate > maxim):
        maxim = candidate
print(maxim)

allSum = 0
for candidate in candidates_grades:
    allSum += candidate
print(allSum)

print()

print(min(candidates_grades))
print(max(candidates_grades))
print(sum(candidates_grades))