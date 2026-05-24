# 👉👈 Two Pointers Pattern

## 📘 What is Two Pointers?

Two Pointers is a problem-solving technique where two pointers are used to traverse through a data structure like:
- Arrays
- Strings
- Linked Lists

This pattern helps reduce:
- Nested loops
- Unnecessary traversals
- Time Complexity

---

## ❓ Why Use Two Pointers?

Many brute-force solutions use nested loops.

Example:

```txt
O(n²)
```

Using Two Pointers, many of these problems can be optimized to:

```txt
O(n)
```

This makes the algorithm:
- Faster
- More efficient
- More interview-friendly

---

## 🧠 Basic Idea Behind Two Pointers

The idea is to place:
- Two indexes/pointers
- At specific positions
- And move them based on conditions

The pointers can:
- Move towards each other
- Move in the same direction
- Move at different speeds

---

## 🔍 Brute Force Example

### Check if an Array is Sorted

### JavaScript

```js
function isSortedArray(arr) {
    for(let i = 0; i < arr.length - 1; i++) {
        for(let j = i + 1; j < arr.length; j++) {
            if(arr[i] > arr[j]) {
                return false;
            }
        }
    }

    return true;
}
```

---

### ⏱️ Time Complexity

```txt
O(n²)
```

Because nested loops are used.

---

## ⚡ Optimized Using Two Pointers

### JavaScript

```js
function isArraySorted(arr) {

    let pointer1 = 0;
    let pointer2 = 1;

    while(pointer2 < arr.length) {

        if(arr[pointer1] > arr[pointer2]) {
            return false;
        }

        pointer1++;
        pointer2++;
    }

    return true;
}
```

---

### Python

```py
def is_array_sorted(arr):

    pointer1 = 0
    pointer2 = 1

    while pointer2 < len(arr):

        if arr[pointer1] > arr[pointer2]:
            return False

        pointer1 += 1
        pointer2 += 1

    return True
```

---

### ⏱️ Time Complexity

```txt
O(n)
```

Only one traversal is used.

---

## 📌 What is a Template?

A Template is a predefined coding pattern used for solving a particular type of problem.

Templates help us:
- Solve problems faster
- Avoid starting from scratch
- Recognize common patterns
- Perform better in interviews

---

## 🧩 General Two Pointer Template

### JavaScript

```js
function twoPointers(arr) {

    let left = 0;
    let right = arr.length - 1;

    while(left < right) {

        if(condition) {
            // process logic
        }

        // update pointers
    }
}
```

---

### Python

```py
def two_pointers(arr):

    left = 0
    right = len(arr) - 1

    while left < right:

        if condition:
            # process logic

        # update pointers
```

---

## 🔄 Types of Two Pointer Movement

---

### 1️⃣ Opposite Direction Pointers

Pointers move towards each other.

### Commonly Used In:
- Palindrome checking
- Reversing arrays
- Two sum in sorted array

---

### Example

```txt
left → ← right
```

---

## 2️⃣ Same Direction Pointers

Pointers move together in the same direction.

### Commonly Used In:
- Sorted array checking
- Sliding window
- Removing duplicates

---

### Example

```txt
left → → right
```

---

## 3️⃣ Slow and Fast Pointers

One pointer moves slower than the other.

### Commonly Used In:
- Linked List cycle detection
- Middle element finding
- Floyd’s Cycle Detection

---

### Example

```txt
slow → 
fast → →
```

---

## 🛠️ Easy Tricks to Identify Two Pointer Problems

Use Two Pointers when:

✅ The problem involves:
- Arrays
- Strings
- Sorted data

---

✅ The problem asks:
- Find pair
- Find triplet
- Check palindrome
- Reverse data
- Remove duplicates
- Compare elements

---

✅ The brute-force solution uses:
- Nested loops
- Repeated traversal

---

## 📚 Most Common Two Pointer Scenarios

| Scenario | Pointer Movement |
|----------|----------------|
| Palindrome | Opposite Direction |
| Reverse Array | Opposite Direction |
| Two Sum Sorted | Opposite Direction |
| Remove Duplicates | Same Direction |
| Sliding Window | Same Direction |
| Linked List Cycle | Slow & Fast |

---

## 🔤 Palindrome Example

### JavaScript

```js
function isPalindrome(str) {

    let left = 0;
    let right = str.length - 1;

    while(left < right) {

        if(str[left] !== str[right]) {
            return false;
        }

        left++;
        right--;
    }

    return true;
}
```

---

### Python

```py
def is_palindrome(str):

    left = 0
    right = len(str) - 1

    while left < right:

        if str[left] != str[right]:
            return False

        left += 1
        right -= 1

    return True
```

---

## 📈 Time Complexity Advantage

| Approach | Complexity |
|----------|------------|
| Brute Force | O(n²) |
| Two Pointers | O(n) |

---

## 💡 Most Common Interview Problems

### Beginner Level

- LeetCode 9 → Palindrome Number
- LeetCode 125 → Valid Palindrome
- Reverse Array
- LeetCode 344 → Reverse String
- LeetCode 541 → Reverse String II
- LeetCode 167 → Two Sum II - Input Array Is Sorted
- LeetCode 283 → Move Zeroes

---

### Medium Level

- LeetCode 26 → Remove Duplicates from Sorted Array
- LeetCode 88 → Merge Sorted Array
- LeetCode 680 → Valid Palindrome II
- LeetCode 977 → Squares of a Sorted Array
- LeetCode 75 → Sort Colors

---

### Advanced Level

- LeetCode 3 → Longest Substring Without Repeating Characters
- LeetCode 76 → Minimum Window Substring
- LeetCode 11 → Container With Most Water
- LeetCode 42 → Trapping Rain Water
- LeetCode 15 → 3Sum
- LeetCode 18 → 4Sum

---

## 🧠 Interview Notes

- Two Pointers is one of the most important DSA patterns.
- It is mainly used to reduce nested loops.
- Many `O(n²)` problems can be optimized to `O(n)`.
- Works extremely well with sorted arrays and strings.
- Pointer movement depends completely on conditions.

---

## ⚠️ Common Beginner Mistakes

- Incorrect pointer updates
- Infinite loops
- Wrong stopping condition
- Confusing pointer directions
- Accessing invalid indexes

---

## 🚀 Quick Revision Tips

| Pattern | Use Case |
|---------|----------|
| Opposite Direction | Palindrome, Reverse |
| Same Direction | Sliding Window |
| Slow & Fast | Linked Lists |

---

## 📌 Summary

In this section, we covered:

- What is Two Pointers
- Why use Two Pointers
- Two Pointer Templates
- Opposite Direction Pointers
- Same Direction Pointers
- Slow & Fast Pointers
- Palindrome Example
- Time Complexity Optimization
- Common Interview Problems

Two Pointers is one of the most important optimization techniques in DSA and is heavily used in coding interviews.