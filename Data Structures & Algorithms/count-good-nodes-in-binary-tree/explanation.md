This is DFS algorithm, because we need to look at all nodes and look at the path from root to that nodes.

To understand that node is good we need to keep track of the maximum node that was before. 

Keep in mind that values can be negative. Therefore passing 0 as initial maximum is wrong, since it will diminish the real maximum in case of negative nodes.
