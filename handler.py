from db import Tweet, TimelineFeed
from uuid import UUID
from q import all_tweets


def write_tweet(user_id: UUID, contents: str):
    tweet = Tweet(
        writer_id=user_id,
        contents=contents,
    )
    # 생성 된 트윗은 Q에 전송
    all_tweets.append(tweet)


def get_timeline(user_id: UUID):
    # 타임라인에서 모든 트윗을 가져온다.
    timeline = TimelineFeed.get(user_id=user_id)
    return timeline.tweets