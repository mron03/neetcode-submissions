Breadth First Search Solution

We need to use a deque in order to keep track of the queue of each level of the tree. 

And at each iteration, we need to process all the nodes in the queue. And only after that, we can create a new queue of the children of the processed nodes.

So, there is a double loop. One for the global iteration of each level of the tree. And one for processing all nodes at each level.
