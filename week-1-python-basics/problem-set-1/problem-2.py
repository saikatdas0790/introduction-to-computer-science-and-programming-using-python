s = "azcBobobegghakl"
bobCount = 0
lastFoundAt = 0
s = s.lower()
while "bob" in s:
    bobCount += 1
    s = s[s.find("bob", lastFoundAt)+2:]

print("Number of times bob occurs is: " + str(bobCount))
