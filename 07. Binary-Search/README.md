# 🔍 Binary Search

## 📘 What is Binary Search?

Binary Search is a searching algorithm used to find a target element in a **sorted array**.

It works by:
- Repeatedly dividing the search space into half
- Comparing the middle element with the target
- Eliminating half of the elements in every step

---

## ❓ Why Use Binary Search?

Binary Search is extremely fast compared to Linear Search.

---

## ⚡ Time Complexity Comparison

| Algorithm | Time Complexity |
|-----------|----------------|
| Linear Search | O(n) |
| Binary Search | O(log n) |

---

## 🚀 Why is O(log n) Powerful?

Binary Search cuts the search space into half every iteration.

Example:

```txt
1000 elements
→ 500
→ 250
→ 125
→ 62
→ 31
→ ...
```

Even for billions of elements, Binary Search performs very efficiently.

---

### 📊 Growth Rate Comparison

> ![(Ologn - Comparison)]:
>
> (./ologn.png)


This image shows why algorithms like:
- `O(log n)`
- `O(n)`

are much faster than:
- `O(n²)`
- `O(2ⁿ)`

for large inputs.

---

## 🧠 Key Requirement for Binary Search

The data MUST be:

✅ Sorted

Examples:
- Ascending order
- Descending order
- Alphabetically sorted

---

### ❌ Binary Search Cannot Be Applied On

- Unsorted arrays
- Randomly arranged data

---

## 📌 Binary Search Steps

---

### ✅ Step 1

Set the search space.

Usually:

```txt
left = 0
right = array.length - 1
```

---

### ✅ Step 2

Find the middle element.

```txt
mid = (left + right) / 2
```

---

### ✅ Step 3

Compare target with middle element.

---

#### Case 1

```txt
target == middle
```

Return the index.

---

#### Case 2

```txt
target < middle
```

Discard:
- Middle element
- All elements on the right

Search in left half.

---

#### Case 3

```txt
target > middle
```

Discard:
- Middle element
- All elements on the left

Search in right half.

---

### ✅ Step 4

If no elements are left:

```txt
return -1
```

---

## 🔄 Binary Search Visualization

Example:

```txt
Array = [1, 3, 5, 7, 9, 11, 13]

Target = 9
```

---

### Iteration 1

```txt
Middle = 7
```

Target > 7

Search right half.

---

### Iteration 2

```txt
Middle = 11
```

Target < 11

Search left half.

---

### Iteration 3

```txt
Middle = 9
```

Target found.

---

## 💻 Binary Search Implementation

---

### JavaScript

```js
function binarySearch(arr, target) {

    let left = 0;
    let right = arr.length - 1;

    while(left <= right) {

        let mid = Math.floor((left + right) / 2);

        if(arr[mid] === target) {
            return mid;
        }

        else if(target < arr[mid]) {
            right = mid - 1;
        }

        else {
            left = mid + 1;
        }
    }

    return -1;
}
```

---

### Python

```py
def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif target < arr[mid]:
            right = mid - 1

        else:
            left = mid + 1

    return -1
```

---

## 📈 Time and Space Complexity

| Operation | Complexity |
|-----------|------------|
| Time Complexity | O(log n) |
| Space Complexity | O(1) |

---

## 🛠️ Easy Tricks to Identify Binary Search Problems

Use Binary Search when:

✅ Data is sorted

---

✅ The problem asks:
- Search efficiently
- Find position/index
- Find first/last occurrence
- Search in huge data

---

✅ The problem contains:
- Monotonic property
- Increasing/decreasing order

---

✅ The brute-force solution is:
- O(n)
- Too slow for large inputs

---

## 📚 Most Common Binary Search Scenarios

| Scenario | Description |
|----------|-------------|
| Search Element | Find target index |
| First Occurrence | Find first appearance |
| Last Occurrence | Find last appearance |
| Lower Bound | Smallest valid index |
| Upper Bound | Largest valid index |
| Search Insert Position | Find insertion index |
| Peak Element | Find local maxima |

---

## 🔄 Recursive Binary Search

Binary Search can also be implemented recursively.

---

### JavaScript

```js
function binarySearch(arr, left, right, target) {

    if(left > right) {
        return -1;
    }

    let mid = Math.floor((left + right) / 2);

    if(arr[mid] === target) {
        return mid;
    }

    else if(target < arr[mid]) {
        return binarySearch(arr, left, mid - 1, target);
    }

    else {
        return binarySearch(arr, mid + 1, right, target);
    }
}
```

---

### Python

```py
def binary_search(arr, left, right, target):

    if left > right:
        return -1

    mid = (left + right) // 2

    if arr[mid] == target:
        return mid

    elif target < arr[mid]:
        return binary_search(arr, left, mid - 1, target)

    else:
        return binary_search(arr, mid + 1, right, target)
```

---

## 🌍 Real World Applications of Binary Search

Binary Search is used in:
- Search engines
- Databases
- Dictionaries
- Phone contacts
- Library systems
- Competitive programming
- Infinite search spaces

---

## 💡 Most Common Interview Questions

### Easy Level

- LeetCode 704 → Binary Search
- LeetCode 35 → Search Insert Position
- LeetCode 69 → Sqrt(x)
- LeetCode 278 → First Bad Version

---

### Medium Level

- LeetCode 33 → Search in Rotated Sorted Array
- LeetCode 34 → Find First and Last Position
- LeetCode 74 → Search a 2D Matrix
- LeetCode 162 → Find Peak Element

---

### Advanced Level

- LeetCode 4 → Median of Two Sorted Arrays
- LeetCode 410 → Split Array Largest Sum
- LeetCode 875 → Koko Eating Bananas

---

## 🧠 Interview Notes

- Binary Search only works on sorted data.
- Always calculate:
  
```txt
mid = left + (right - left) / 2
```

to avoid overflow in some languages.

- Binary Search is one of the most important interview algorithms.
- Many advanced problems use Binary Search indirectly.

---

## ⚠️ Common Beginner Mistakes

- Applying Binary Search on unsorted arrays
- Incorrect loop condition
- Infinite loops
- Wrong pointer updates
- Forgetting edge cases
- Returning wrong index

---

## 🚀 Quick Revision Tips

| Concept | Key Idea |
|---------|----------|
| Requirement | Sorted Data |
| Complexity | O(log n) |
| Search Space | Divide into halves |
| Pointer Names | left, right, mid |

---

## 📌 Summary

In this section, we covered:

- Binary Search Basics
- Why Binary Search is Fast
- Binary Search Steps
- Iterative Binary Search
- Recursive Binary Search
- Time Complexity
- Binary Search Patterns
- Common Interview Problems
- Real World Applications

Binary Search is one of the most important searching algorithms and is heavily used in:
- DSA Interviews
- Competitive Programming
- Optimization Problems
- Search Problems