# 📅 Day 38 - Search in a Row-Column Sorted Matrix
## 🔍 Problem Statement
Given a 2D matrix mat[][] of size n x m, where each row and each column is sorted in increasing order, and a number x, find whether x exists in the matrix.

## ✅ Solution Approach
We used an efficient search from top-right corner strategy:

## 🔧 Steps:
- Initialize position at top-right: i = 0, j = m - 1

- While within matrix bounds:

- If mat[i][j] == x: return 1 (found)

- If mat[i][j] > x: move left (j -= 1)

- If mat[i][j] < x: move down (i += 1)

- If loop ends without finding: return 0

## ⏱ Time Complexity:
O(n + m)
(At most we traverse each row or column once.)

## 📦 Space Complexity:
O(1)
(No extra space used.)

## 💡 Key Concepts Practiced:
- Matrix traversal

- Optimized 2D search

- Sorted 2D array strategy
