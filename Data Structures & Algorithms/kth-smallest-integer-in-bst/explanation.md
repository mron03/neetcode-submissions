DFS

First we need to reach the smallest node. Which is just recurvely going to left node.

After that the recursion moves in order Left -> Node -> Right.  So we collect the nodes in ascending order. 

At the end just return the index of k in the list.



OR 

Instead of collecting nodes. Just count down from the leftest node K times. When K becomes 0, this is the node to return.
