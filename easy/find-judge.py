from typing import List
from collections import defaultdict

"""
Conditions
----
- The town judge trusts nobody
- Everybody, except the town judge, trusts the town judge
- There's exactly one person that satisfies the above 2 conditions 👆 
Strategy
----
- in a network of nodes, we need to compare the number of incoming connections vs outgoing connections
- we need to keep this data of connections in some sort of hash-map or dict
- after computing the incoming and outgoing connections, we compare with the conditions stated above
- the node that satisfies those conditions is our town judge
- otherwise, simply return -1
"""
class Solution:
	def findJudge(self, n: int, trust: List[List[int]]) -> int:
		incoming = defaultdict(int)
		outgoing = defaultdict(int)

		for a, b in trust:
			outgoing[a] += 1 
			incoming[b] += 1

		for i in range(1, n + 1):
			if outgoing[i] == 0 and incoming[i] == n - 1:
				return i
		return -1

solution = Solution()
res = solution.findJudge(2, [[1,2]])

print(res)
assert res == 2, "Wrong Answer"

