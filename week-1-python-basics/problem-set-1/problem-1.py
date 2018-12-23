s = "azcbobobegghakl"
vowelCount = 0
for character in s:
    if character == "a" or character == "e" or character == "i" or character == "o" or character == "u":
        vowelCount += 1

print("Number of vowels: " + str(vowelCount))
