class Twitter:

    def __init__(self):
        self.count = 0
        self.tweetmap = defaultdict(list)
        self.followmap = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetmap[userId].append([self.count,tweetId])
        self.count -=1

    def getNewsFeed(self, userId: int) -> List[int]:
        res= []
        minheap = []
        self.followmap[userId].add(userId)
        for followeeid in self.followmap[userId]:
            if followeeid in self.tweetmap:
                index = len(self.tweetmap[followeeid])-1
                count,tweetid = self.tweetmap[followeeid][index]
                minheap.append([count,tweetid,followeeid,index-1])
        heapq.heapify(minheap)
        while minheap and len(res)<10:
            count,tweetid,followeeid,index = heapq.heappop(minheap)
            res.append(tweetid)
            if index >=0:
                count,tweetid = self.tweetmap[followeeid][index]
                heapq.heappush(minheap,[count,tweetid,followeeid,index-1])
        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.followmap[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followmap[followerId]:
            self.followmap[followerId].remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)