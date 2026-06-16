r'''
Problem StatementGiven two strings, s and goal, return true if and only if s can become goal after some number of shifts on s.
A shift on s consists of moving the leftmost character to the rightmost position.
Example 1: s = "abcde", goal = "cdeab" \(\rightarrow \) Output: true
Example 2: s = "abcde", goal = "abced" \(\rightarrow \) Output: false
Constraints1 <= s.length, goal.length <= 100s and goal consist of lowercase English letters. 
'''
le = input("Enter the length of input string: ")
le = int(le)
s = []
for i in range(le):
    char = input("Enter a character and hit enter to use it: ")
    s.insert(i, char)
print(f"Final string entered: {s}")
goal = []
for i in range(le):
        g = input("Enter goal string, hit enter after each string :")
        goal.insert(i, g)
print(f"Final goal string: {goal}")
double = []
double = s + s
print (f"Doubling the strings :{double}")
cur_slice = []
for i in range(le):
      cur_slice = double[i:i+le]
      if cur_slice == goal:
           print(f"Final rotation: {cur_slice}")
      else: print("Rotation not possible."); break

            



