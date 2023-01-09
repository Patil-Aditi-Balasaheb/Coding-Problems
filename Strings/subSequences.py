######################################
# Print all subsequences of a string #
######################################

# Recursive Approach - Pick and Don’t Pick Concept
# Explanation - https://youtu.be/EJwCUCjb9HM

ans = []    # for storing the subsequences

def printSubsequences(input, output):
    if len(input) == 0:
        # appending only non-empty subsequences
        if output:
            ans.append(output)
        return
    
    # when we do not include the first character of input in the output
    printSubsequences(input[1:], output)

    # when we include the first character of input in the output
    printSubsequences(input[1:], output + input[0])


def subsequences(string):
    ans.clear()
    printSubsequences(string, "")
    return ans


def main():
    t = int(input())
    strings = input().strip().split()
    for string in strings:
        print(*sorted(subsequences(string)))


if __name__ == "__main__":
    main()


'''
Sample Input 1:
1 
abc
Sample Output 1:
a ab abc ac b bc c
Explanation Of Sample Input 1:
All possible subsequences of abc are :  
“a” , “b” , “c” , “ab” , “bc” , “ac”, “abc”


Sample Input 2:
4
bbb p hq ghu
Sample Output 2:
b b b bb bb bb bbb
p 
h hq q 
g gh ghu gu h hu u 
'''