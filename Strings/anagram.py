# Question: Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Way 1: Sorting (Conceptually Simplest - Time: O(N log N), Space: O(N))
def is_anagram_sort(s, t):
    s = s.lower()
    t = t.lower()
    return sorted(s) == sorted(t)

print(is_anagram_sort("anagram", "nagaram"))


# Way 2: Dictionary / Hash Map (Optimal - Time: O(N), Space: O(1) auxiliary)
def is_anagram_dict(s, t):
    s = s.lower()
    t = t.lower()
    
    if len(s) != len(t):
        return False
        
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
        
    for char in t:
        if char not in count or count[char] == 0:
            return False
        count[char] -= 1
        
    return True

print(is_anagram_dict("anagram", "nagaram"))


# Way 3: Pythonic Counter (Time: O(N), Space: O(1) auxiliary)
from collections import Counter

def is_anagram_counter(s, t):
    s = s.lower()
    t = t.lower()
    return Counter(s) == Counter(t)

print(is_anagram_counter("anagram", "nagaram"))

# Way 4: Direct iteration using sorted() (simplest direct way)
s = "anagram"
t = "nagaram"

is_anagram = sorted(s.lower()) == sorted(t.lower())
print(is_anagram)

# Way 5: Direct iteration using a Dictionary (Time: O(N), Space: O(1) auxiliary)
s = "anagram"
t = "nagaram"

s = s.lower()
t = t.lower()

is_anagram_dict = True
if len(s) != len(t):
    is_anagram_dict = False
else:
    count = {}
    for char in s:
        count[char] = count.get(char, 0) + 1
    for char in t:
        if char not in count or count[char] == 0:
            is_anagram_dict = False
            break
        count[char] -= 1

print(is_anagram_dict)
