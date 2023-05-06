# Intuition
The intuitive (and expensive) approach was to use a nexted for loop. The outer loop would iterate over all of s while the inner one iterated over k making the runtime O(s*k), not ideal.

# Approach
What I ended up doing to save time was to instead create a queue of size k, I filled this queue while iterating through s and I kept track of whether a vowel was added or not, I also kept track of whether a vowel was removed.  

# Complexity
- Time complexity:
There are some operations (checking, manipulating the queue etc) which have a constand runtime. pushing and popping from the queue would be O(1)*s meaning the overall time is O(3s) which then becomes: O(s) 

- Space complexity:
O(k)

# Code
```
import queue

class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        maxSubStr = 0
        count = 0
        q = queue.SimpleQueue()

        for i in s:
            if q.qsize() < k:
                q.put(i)
                if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                    count += 1 
                if maxSubStr < count:
                    maxSubStr = count
            else:
                pop = q.get()
                if pop == 'a' or pop == 'e' or pop == 'i' or pop == 'o' or pop == 'u':
                    count -= 1
                q.put(i)
                if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
                    count += 1 
                if maxSubStr < count:
                    maxSubStr = count      
        return maxSubStr
```