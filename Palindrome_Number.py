def isPalindrome(x: int):
    a = str(x)
    if a == a[::-1]:
        return True
    return False

if __name__ == "__main__":
    
    x = int(input("Enter the number  :"))
    result = isPalindrome(x)
    print(result)
