    def convertToAbbreviation(word):
        if len(word) <= 10:
            return word
        else:
            return word[0] + str(len(word) - 2) + word[-1]
     
    n = int(input())
     
    for _ in range(n):
        word = input().strip()
        print(convertToAbbreviation(word))