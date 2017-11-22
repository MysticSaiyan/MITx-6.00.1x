s = "bobisachildbobbobbobbobbobbobbobbobbob"

bobCount = 0

for i in range(0, len(s)):
    if s[i:i+3] == "bob":
        bobCount += 1
print("Number of times bob occurs is: " + str(bobCount))