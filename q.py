from collections import deque
from db import TimelineFeed, FollowRelationship


all_tweets = deque()


def consume_q(all_tweets: deque = all_tweets):
    # 지속적으로 큐는 트윗이 있으면, 해당하는 유저 타임라인에 컨슈밍
    if all_tweets:
        tweet = all_tweets.popleft()
        all_followees = list(FollowRelationship.filter(follower_id=tweet.writer_id))
        for followee in all_followees:
            timeline = TimelineFeed.get(user_id=followee.followee_id)
            timeline.tweets.append(tweet)
            timeline.save()