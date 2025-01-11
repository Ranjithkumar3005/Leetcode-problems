import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.users = {}  # key: userID. val: [following, tweets]
        self.time = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId] = [[], []]
        self.users[userId][1].append([self.time, tweetId])

        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        if userId not in self.users:
            return []
        maxheap = []
        for tweet in self.users[userId][1]:
            maxheap.append([-tweet[0], tweet[1]])

        for followed in self.users[userId][0]:
            if followed in self.users:
                for tweet in self.users[followed][1]:
                    maxheap.append([-tweet[0], tweet[1]])

        heapq.heapify(maxheap)
        count, ret, past = 0, [], set()
        while maxheap and count < 10:
            item = heapq.heappop(maxheap)[1]
            if item not in past:
                ret.append(item)
                past.add(item)
                count += 1
        return ret

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId] = [[], []]
        self.users[followerId][0].append(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users or followeeId not in self.users:
            return
        try:
            self.users[followerId][0].remove(followeeId)
        except:
            return


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
