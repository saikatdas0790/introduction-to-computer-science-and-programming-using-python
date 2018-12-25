s = "azcbobobegghakl"
vowelCount = 0
for character in s:
    if character in "aeiou":
        vowelCount += 1

print("Number of vowels: " + str(vowelCount))
