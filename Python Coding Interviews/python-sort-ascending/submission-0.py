from typing import List


def sort_words(words: List[str]) -> List[str]:
    if len(words) <= 1:
        return words
    else:
        midpoint = len(words)//2
        arrayA = words[0:midpoint]
        arrayB = words[midpoint:(len(words))]
        arrayA = sort_words(arrayA)
        arrayB = sort_words(arrayB)
        return merge_words(arrayA, arrayB)        
    pass

def sort_numbers(numbers: List[int]) -> List[int]:
    if len(numbers) <= 1:
        return numbers
    else:
        midpoint = len(numbers)//2
        arrayA = numbers[0:midpoint]
        arrayB = numbers[midpoint:(len(numbers))]
        arrayA = sort_numbers(arrayA)
        arrayB = sort_numbers(arrayB)
    return merge_numbers(arrayA, arrayB)
    pass

def sort_decimals(numbers: List[float]) -> List[float]:
    if len(numbers) <= 1:
        return numbers
    else:
        midpoint = len(numbers)//2
        arrayA = numbers[0:midpoint]
        arrayB = numbers[midpoint:(len(numbers))]
        arrayA = sort_decimals(arrayA)
        arrayB = sort_decimals(arrayB)
    return merge_decimals(arrayA, arrayB)
    pass

def merge_words(arrayA: List[str], arrayB: List[str]) -> List[str]:
    i = 0
    j = 0
    retArray = []
    while (i < len(arrayA)) and (j < len(arrayB)):
        if (arrayA[i] < arrayB[j]):
            retArray.append(arrayA[i])
            i += 1
        else:
            retArray.append(arrayB[j])
            j += 1

    while (i < len(arrayA)):
        retArray.append(arrayA[i])
        i += 1

    while (j < len(arrayB)):
        retArray.append(arrayB[j])
        j += 1

    return retArray
    pass

def merge_numbers(arrayA: List[int], arrayB: List[int]) -> List[int]:
    i = 0
    j = 0
    retArray = []
    while (i < len(arrayA)) and (j < len(arrayB)):
        if (arrayA[i] < arrayB[j]):
            retArray.append(arrayA[i])
            i += 1
        else:
            retArray.append(arrayB[j])
            j += 1
        
    while (i < len(arrayA)):
        retArray.append(arrayA[i])
        i += 1

    while (j < len(arrayB)):
        retArray.append(arrayB[j])
        j += 1

    return retArray
    pass

def merge_decimals(arrayA: List[float], arrayB: List[float]) -> List[float]:
    i = 0
    j = 0
    retArray = []
    while (i < len(arrayA)) and (j < len(arrayB)):
        if (arrayA[i] < arrayB[j]):
            retArray.append(arrayA[i])
            i += 1
        else:
            retArray.append(arrayB[j])
            j += 1

    while (i < len(arrayA)):
        retArray.append(arrayA[i])
        i += 1

    while (j < len(arrayB)):
        retArray.append(arrayB[j])
        j += 1

    return retArray
    pass




# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, 5, 3, 2, 4, 11, 19, 9, 2, 5, 6, 7, 4, 2, 6]))

print(sort_decimals([3.14, 2.82, 6.433, 7.9, 21.555, 21.554]))
