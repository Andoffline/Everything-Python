print('Palindrome word checker')
word=input('Enter a word:')
lword=word.lower()
start=0
end=len(word)-1

palindrome=True

while start<end:
    if lword[start]!=lword[end]:
        palindrome=False
        break
    start+=1
    end-=1

if palindrome:
    print(word,' is a palindrome word')
else:
    print(word,' is NOT a palindrome word')