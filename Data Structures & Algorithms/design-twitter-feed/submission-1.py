import time

class Twitter:

    def __init__(self):
        self.posts_map = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.posts_map[userId].append((time.time(), tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        posts = [post for post in self.posts_map[userId]]

        for followeeId in self.follow_map[userId]:
            posts.extend(self.posts_map[followeeId])

        heapq.heapify_max(posts)

        res = []
        for _ in range(min(len(posts), 10)):
            res.append(heapq.heappop_max(posts)[1])
        
        return res

        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
       

        
