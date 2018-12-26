# s = "azcbobobegghakl"
s = "abcbcd"

longestSubstring = ""
start = 0
tempSubstring = s[start]

while (start < len(s)-1):
    for j in range(start+1, len(s)):
        if s[j] >= tempSubstring[len(tempSubstring)-1]:
            tempSubstring = tempSubstring + s[j]
            start = j
        else:
            if len(tempSubstring) > len(longestSubstring):
                longestSubstring = tempSubstring
            start = j
            tempSubstring = s[start]
            break

print("Longest substring in alphabetical order is: " + longestSubstring)
