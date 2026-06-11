# 1755. Palindrome Reorder

def solve(s: str) -> str:
    
    d = {}
    for i in s:
        if i in d:
            d[i] +=1
        else:
            d[i] = 1

    isOddFreqFound = False
    oddFreqCharacter = ""
    for i in d:
        if d[i]%2 != 0:
            if isOddFreqFound:
                return "NO SOLUTION"
            isOddFreqFound = True
            oddFreqCharacter = i

    finalAnswer = []
    for i in d:
        finalAnswer.append(i*(d[i]//2))

    strFinalAnswer = "".join(finalAnswer)
    strFinalAnswer = strFinalAnswer + oddFreqCharacter + strFinalAnswer[::-1]

    return strFinalAnswer

def main():
    s = input()
    print(solve(s))

main()