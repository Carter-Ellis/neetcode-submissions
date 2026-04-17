#
#
#
#   postTweet() - tweetId from userId 
#
#   getNewsFeed() - feed posts must be from themself or user they follow
#
#   follow() - followerId follows followeeId
#
#   unfollow() - followerId unfollows followeeId
#
#   Notes:
#       - Each tweetId is unique
#
#
#
#
#

class User:
    def __init__(self, userId):
        self.userId = userId
        self.following = set() # userId
        self.tweets = [] # tweetId

    def follow(self, followeeId):
        self.following.add(followeeId)

    def unfollow(self, followeeId):
        self.following.discard(followeeId)


class Twitter:

    _timestamp = 0

    def __init__(self):        
        self.users = {} # userId : User()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.checkUser(userId)
        self.users[userId].tweets.append((Twitter._timestamp, tweetId))
        Twitter._timestamp += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        user = self.users[userId]
        maxHeap = [(-x, y) for x, y in user.tweets]

        for followee in user.following:
            for tweet in self.users[followee].tweets:
                maxHeap.append((-tweet[0], tweet[1]))
        heapq.heapify(maxHeap)

        maxTweets = 10
        i = 0
        feed = []

        while maxHeap and i < maxTweets:
            feed.append(heapq.heappop(maxHeap)[1])
            i += 1
        return feed

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.checkUser(followerId)
        self.users[followerId].follow(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        self.checkUser(followerId)
        self.users[followerId].unfollow(followeeId)
    
    def checkUser(self, userId):
        if userId not in self.users:
            self.users[userId] = User(userId)
        
