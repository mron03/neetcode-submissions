BFS Method



During BFS, at each iteration, our queue should contain all the nodes of the  current level of the tree in order. 
So we know that the rightmost node of the queue is the right side viewed node of the tree on that level. 
But before popping that answer and saving it in the result. We need to collect the next queue of the next level. 
After that, we can pop the right-most of the current queue and save it in the result list.
Then assign the previously collected queue as the current queue for the next iteration.
