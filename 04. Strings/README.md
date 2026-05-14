# 🔤 Strings

## 📘 What are Strings?

A String is a sequence (array) of characters.

Strings can contain:
- Alphabets
- Numbers
- Special characters
- Spaces

Examples:

```txt
"hello"
"DSA123"
"hello@123"
```

---

## ❓ Why are Strings Important?

Strings are one of the most commonly used data structures in programming.

They are heavily used in:
- Input processing
- Web Development
- Search Engines
- Data Validation
- Pattern Matching
- Competitive Programming
- Technical Interviews

---

## 🧠 Strings and Arrays

Strings have many similarities with arrays.

Common similarities:
- Indexing
- Traversal
- Searching
- Slicing
- Iteration

---

## 🔢 Indexing in Strings

Each character has an index position.

Example:

```txt
String = "HELLO"
```

| Index | Character |
|-------|-----------|
| 0, -5 | H |
| 1, -4 | E |
| 2, -3 | L |
| 3, -2 | L |
| 4, -1 | O |

---

## 🚶 Traversing a String

### JavaScript

```js
let str = "HELLO";

for(let i = 0; i < str.length; i++) {
    console.log(str[i]);
}
```

---

### Python

```py
str = "HELLO"

for i in range(len(str)):
    print(str[i])
```

---

## ✂️ Common String Methods

---

### 🔹 slice()

Extracts a portion of a string.

### JavaScript

```js
let str = "JavaScript";

console.log(str.slice(0, 4));
```

### Python

```py
str = "Python"

print(str[0:4])
```

---

### 🔹 indexOf() / find()

Returns the index of a character or substring.

### JavaScript

```js
let str = "hello";

console.log(str.indexOf("e"));
```

### Python

```py
str = "hello"

print(str.find("e"))
```

---

### 🔹 includes() / in

Checks whether a substring exists.

### JavaScript

```js
let str = "hello";

console.log(str.includes("ell"));
```

### Python

```py
str = "hello"

print("ell" in str)
```

---

### 🔹 split()

Splits a string into an array/list.

### JavaScript

```js
let str = "a,b,c";

console.log(str.split(","));
```

### Python

```py
str = "a,b,c"

print(str.split(","))
```

---

### 🔹 join()

Joins array/list elements into a string.

### JavaScript

```js
let arr = ["a", "b", "c"];

console.log(arr.join(""));
```

### Python

```py
arr = ["a", "b", "c"]

print("".join(arr))
```

---

## 📚 Common String Terminologies

---

### 🔹 Substring vs Subsequence

### ✅ Substring

A continuous part of a string.

Example:

```txt
String: "thequickbrownfox"

Substring: "quick"
```

Example: 

```txt
String: Hello 

Substrings: 

length 1 : h, e, l, l, o
length 2 : he, el, ll, lo
length 3 : hel, ell, llo
length 4 : hell, ello
length 5 : hello

Total no. of substrings = 15
```

### NOTE: Total no. of substrings = (n * (n+1)) / 2

---

### ✅ Subsequence

Characters selected without changing order, but not necessarily continuous.

Example:

```txt
String: "thequickbrownfox"

Subsequence: "qck"
```

---

### 🔹 Prefix vs Suffix

### ✅ Prefix

A substring occurring at the beginning of the string.

Example:

```txt
String: "coding"

Prefix: "cod"
```

---

### ✅ Suffix

A substring occurring at the end of the string.

Example:

```txt
String: "coding"

Suffix: "ing"
```

---

## 🔒 Mutable vs Immutable

---

### ✅ Mutable

Object values can be changed after creation.

Example:
- Arrays
- Lists

---

### ✅ Immutable

Object values cannot be changed after creation.

Strings are immutable in:
- JavaScript
- Python

---

### JavaScript Example

```js
let str = "hello";

str[0] = "H";

console.log(str);
```

Output:

```txt
hello
```

---

### Python Example

```py
str = "hello"

str[0] = "H"
```

Output:

```txt
TypeError
```

---

## ⚙️ Common String Operations

---

### 🔄 Reversing a String

### JavaScript

```js
let str = "hello";

let reversed = str.split("").reverse().join("");

console.log(reversed);
```

### Python

```py
str = "hello"

print(str[::-1])
```

---

### 🔍 Check if Strings are Identical

### JavaScript

```js
let str1 = "abc";
let str2 = "abc";

console.log(str1 === str2);
```

### Python

```py
str1 = "abc"
str2 = "abc"

print(str1 == str2)
```

---

### 🔤 Sorting Characters in a String

### JavaScript

```js
let str = "dcba";

let sorted = str.split("").sort().join("");

console.log(sorted);
```

### Python

```py
str = "dcba"

print("".join(sorted(str)))
```

---

### ➕ Concatenation

### JavaScript

```js
let str1 = "Hello";
let str2 = "World";

console.log(str1 + " " + str2);
```

### Python

```py
str1 = "Hello"
str2 = "World"

print(str1 + " " + str2)
```

---

### 🔢 Count Characters

### JavaScript

```js
let str = "hello";

console.log(str.length);
```

### Python

```py
str = "hello"

print(len(str))
```

---

### ❌ Removing Characters

### JavaScript

```js
let str = "hello";

console.log(str.replace("l", ""));
```

### Python

```py
str = "hello"

print(str.replace("l", ""))
```

---

### 🖨️ Printing All Substrings

### JavaScript

```js
let str = "abc";

for(let i = 0; i < str.length; i++) {
    let temp = "";

    for(let j = i; j < str.length; j++) {
        temp += str[j];
        console.log(temp);
    }
}
```

---

### Python

```py
str = "abc"

for i in range(len(str)):
    temp = ""

    for j in range(i, len(str)):
        temp += str[j]
        print(temp)
```

---

## 🛠️ Additional Useful String Methods

---

### JavaScript String Methods

| Method | Description |
|--------|-------------|
| `toUpperCase()` | Convert to uppercase |
| `toLowerCase()` | Convert to lowercase |
| `trim()` | Remove spaces |
| `charAt()` | Get character at index |
| `replace()` | Replace substring |
| `startsWith()` | Check prefix |
| `endsWith()` | Check suffix |

---

### Python String Methods

| Method | Description |
|--------|-------------|
| `upper()` | Convert to uppercase |
| `lower()` | Convert to lowercase |
| `strip()` | Remove spaces |
| `replace()` | Replace substring |
| `startswith()` | Check prefix |
| `endswith()` | Check suffix |
| `count()` | Count occurrences |

---

## 📈 Time Complexity of Common String Operations

| Operation | Complexity |
|-----------|------------|
| Access Character | O(1) |
| Traversal | O(n) |
| Search | O(n) |
| Concatenation | O(n) |
| Reverse | O(n) |
| Substring Extraction | O(n) |

---

## 💡 Most Common Interview Questions on Strings

### Beginner Level

- Reverse a string
- Check palindrome
- Count vowels and consonants
- Find frequency of characters
- Remove duplicate characters
- Find largest word in a sentence

---

### Intermediate Level

- Longest common prefix
- Valid anagram
- String compression
- Reverse words in a sentence
- First non-repeating character
- Check rotation of strings

---

### Advanced Level

- KMP Algorithm
- Rabin-Karp Algorithm
- Z Algorithm
- Longest Palindromic Substring
- Minimum Window Substring

---

## 🧠 Interview Notes

- Strings are heavily asked in coding interviews.
- Most string problems involve:
  - Traversal
  - Hashing
  - Two pointers
  - Sliding window
- Immutability is an important concept.
- Learn substring and subsequence differences clearly.

---

## ⚠️ Common Beginner Mistakes

- Confusing substring with subsequence
- Incorrect loop boundaries
- Forgetting strings are immutable
- Incorrect indexing
- Using expensive concatenation repeatedly inside loops

---

## 📌 Summary

In this section, we covered:

- Strings
- Indexing
- Traversal
- Common String Methods
- Substring vs Subsequence
- Prefix vs Suffix
- Mutable vs Immutable
- Common String Operations
- JavaScript String Methods
- Python String Methods
- Interview Questions on Strings

Strings form the foundation for many advanced topics like:
- Sliding Window
- Pattern Matching
- Dynamic Programming
- Hashing
- Recursion
- Backtracking