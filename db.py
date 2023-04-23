from pydantic import BaseModel, Field
from datetime import datetime
from uuid import uuid4, UUID


class User(BaseModel):
    id: UUID = Field(default_factory=uuid4())
    screen_name: str
            


class Tweet(BaseModel):
    id: UUID = Field(default_factory=uuid4())
    timestamp: datetime = Field(default_factory=datetime.now())
    writer_id: UUID
    contents: str
    

class FollowRelationship(BaseModel):
    follower_id: UUID
    followee_id: UUID


class TimelineFeed(BaseModel):
    user_id: UUID
    tweets: list[UUID | None] = list