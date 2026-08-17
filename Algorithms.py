def manual_lowercase(text:str) -> str:
    result = ""
    for char in text:
        ascii_value = ord(char)
        if 65 <= ascii_value <= 90:
            char = chr(ascii_value + 32)
        result += char
    return result
## the largest integer less than or equal to the number
def floor(n:float) -> int:
    truncated = int(n) 
    if truncated == n:
        return n
    if n < 0:
        return truncated - 1
    return truncated



def check_if_symmetric(s:str) -> bool:
    s = manual_lowercase(s)
    left = 0
    right = len(s) - 1
    while left  < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

def convert_to_number(s:str)-> list[int]:
    s = manual_lowercase(s)
    alp = " abcdefghijklmnopqrstuvwxyz"
    results = []
    for char in s:
        value = alp.index(f"{char}")
        results.append(value)
    return results

def convert_to_letters(s:str) -> str:
    alp = " abcdefghijklmnopqrstuvwxyz"
    result = ""
    for num in s:
        char = alp[num]
        result += char
    return result
def get_intersection(arr1:list[int],arr2:list[int]) -> list[int]:
    result = []
    for val in arr1:
         if val not in result:
            if val in arr2:
              result.append(val)
    return result
def get_union(arr1:list[int],arr2:list[int]) -> list[int]:
    result = []
    for val in arr1:
        if val not in result:
            result.append(val)
    for val in arr2:
        if val not in  result:
            result.append(val)
    return result
def count_characters(s:str) -> dict[str:int] :
    s = manual_lowercase(s)
    count = {}
    for val in s:
        count[val] = count.get(val,0) + 1
    return count
def is_prime(N:int) -> bool:
    if N <= 1:
        return False
    limit = N // 2
    for i  in range(2,limit + 1):
        if N % i == 0:
            return False
    return True


    





