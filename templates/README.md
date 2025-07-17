# Coding Pattern Templates for Interviews

---

## 1. Two Pointers / Sliding Window

### When to Use
- Problems involving **arrays or strings**.
- Finding a **contiguous subarray or substring** that meets a condition (e.g., longest, shortest, specific sum).
- Signal Keywords: "subarray," "substring," "contiguous," "longest," "shortest," "minimum," "maximum" (when applied to a range).
- Use this when you need to find an optimal range within a 1D array or string. For example, "find the longest substring with no repeating characters" or "find the minimum size subarray that sums to a target."
### Code Template
```python
def sliding_window_template(arr):
    left = 0
    result = 0
    # ... any other state for the current window ...

    for right in range(len(arr)):
        # Expand the window by adding arr[right]

        # While the window is invalid, shrink it from the left
        while not is_window_valid():
            # Remove arr[left] from the window state
            left += 1

        # Update the result, e.g., with the window size
        # result = max(result, right - left + 1)

    return result
```
### How to Apply
1. Initialize a `left` pointer to `0` and a `result` variable.
2. Use a `for` loop with a `right` pointer to expand the window.
3. Inside the loop, use a `while` loop to shrink the window from the `left` until it becomes valid.
4. Update your `result` with the properties of the current valid window.

## 2. Hash Map (Dictionary)
### When to Use
- Problems involving counting frequencies, finding duplicates, or needing fast O(1) lookups. 
- The key to many "find a pair" problems like Two Sum.
- Signal Keywords: "count," "frequency," "duplicate," "group," "anagram," "pair."
- Use this when you need to count how often things appear, group items by a property, or quickly look up if you've seen something before. For example, "find a pair that sums to a target" or "group the anagrams."
```python # Template for "find a pair" problems
def hash_map_template(arr, target):
    lookup = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in lookup:
            return [lookup[complement], i]
        lookup[num] = i
```
### How to Apply
1. Initialize an empty dictionary `lookup = {}`.
2. Loop through your input data.
3. In each iteration, either check for an existing entry that solves your problem (like `complement in lookup`) or store the current item's information (`lookup[num] = i`).

## 3. Tree/Graph Traversal: BFS
### When to Use
- Finding the shortest path in an unweighted graph or tree.
- Any problem involving exploring by levels, layers, or rings.
- Signal Keywords: "shortest path," "minimum steps," "nearest," "level," "layer."
- Use this for finding the shortest path in an unweighted graph or grid. Any problem that mentions processing nodes "level-by-level" is a perfect candidate for BFS.
```Python
import collections
def bfs_template(start_node):
    queue = collections.deque([start_node])
    visited = {start_node}
    while queue:
        node = queue.popleft() #
        # Process node here
        for neighbor in get_neighbors(node):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
```
### How to Apply
- Initialize a `deque` (queue) with the starting node.
- Initialize a `visited` set to avoid infinite loops (if graph is cyclic; e.g. binary tree don't need)
- Loop while the `queue` is not empty.
- Inside the loop, `popleft()` to get the next node, process it, and add all its unvisited neighbors to both the `queue` and the `visited` set.

## 4. Tree/Graph Traversal: DFS
### When to Use
- Checking for connectivity.
- Finding if any path exists between two nodes.
- Exploring all possible configurations or paths (e.g., all root-to-leaf paths).
- Signal Keywords: "path exists," "connectivity," "connected components," "cycle," "all paths."
- Use this when you need to explore a graph or tree exhaustively. It's not about the shortest path, but about whether a path exists at all or about visiting every single node in a component. For example, "count the number of connected components" (like in Number of Islands).
```Python
def dfs_template(start_node):
    visited = set()
    def solve(node):
        if not node or node in visited:
            return
            
        visited.add(node)
        # Process node here (pre-order)
        
        for neighbor in get_neighbors(node):
            solve(neighbor)
        
        # Process node here (post-order)

    solve(start_node)
 ```
### How to Apply
1. Create a `visited` set to track visited nodes.
2. Define a recursive helper function, `solve(node)`.
3. The first lines of `solve(node)` should be your base case (e.g., what to do if the node is null or already visited).
4. Mark the current node as visited.
5. Make a recursive call, `solve(neighbor)`, for each of the node's neighbors.

## 5. Heap (Priority Queue)
### When to Use
- Any problem asking for the "Top K," "Smallest K," or "Largest K" elements. 
- Finding the median in a stream or merging multiple sorted lists.
- Signal Keywords: "top K," "smallest K," "largest K," "most frequent K," "median," "merge."
- Use this whenever the problem asks you to find the top, smallest, or most frequent K items from a collection. It's also the go-to for merging multiple sorted lists or maintaining a running median.
```Python
import heapq
# Finds the K largest elements
def heap_template(arr, k):
    min_heap = []
    for num in arr:
        heapq.heappush(min_heap, num)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return min_heap
```
### How to Apply
1. Remember that Python's `heapq` is a min-heap.
2. To find the K largest items, maintain a min-heap of size K.
3. Loop through the input. `heappush` each item onto the heap.
4. If the heap's size exceeds `k`, `heappop` the smallest item.
5. After the loop, the heap will contain the `k` largest elements.

## 6. Binary Search
### When to Use
- Use binary search when you can quickly discard half of the search space based on a single check.
- The Obvious Signal: The problem gives you a sorted array.
- The Advanced Signal ("Binary Search on the Answer"): The problem asks you to find the minimum or maximum value that satisfies a certain condition. You can "guess" an answer, and if your guess is too high or too low, you can safely eliminate all other higher or lower guesses.

```Python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        # Calculate mid this way to prevent potential overflow in other languages
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid # Target found
        elif arr[mid] < target:
            # Target is in the right half
            left = mid + 1
        else:
            # Target is in the left half
            right = mid - 1
            
    return -1 # Target not found
```
### How to Apply
1. Identify Your Search Space: Determine the `left` (minimum possible value) and `right` (maximum possible value) bounds of what you're searching for.
2. Define Your Condition: What are you checking at the `mid` point? 
   - Simple Case: Is `array[mid]` equal to, less than, or greater than your target?
   - Advanced Case: Can you achieve the goal with a value of `mid`? (e.g., "is it possible to finish in `mid` hours?").
3. Implement the Loop: Write the `while left <= right:` loop.
4. Shrink the Space: Based on your condition at `mid`, discard half of the search space by moving either `left` or `right`.
   - If `mid` is too small, you need a larger value, so set `left = mid + 1`. 
   - If `mid` is too large, you need a smaller value, so set `right = mid - 1`.