import time
from abc import ABC, abstractmethod


class SocialChannel:
    def __init__(self, type_of_channel: str, number_of_followers: int):
        self.type_of_channel = type_of_channel
        self.number_of_followers = number_of_followers


class Post:
    def __init__(self, message: str, timestamp: float):
        self.message = message
        self.timestamp = timestamp


class PostToChannel(ABC):
    @abstractmethod
    def post_to_channel(self):
        """Post to the channel"""


class Twitter(PostToChannel):
    def __init__(self, message, channel):
        self.message = message
        self.channel = channel

    def post_to_channel(self):
        print(f"The post was published on {self.channel}: {self.message}")


class Youtube(PostToChannel):
    def __init__(self, message, channel):
        self.message = message
        self.channel = channel

    def post_to_channel(self):
        print(f"The post was published on {self.channel}: {self.message}")


class Facebook(PostToChannel):
    def __init__(self, message, channel):
        self.message = message
        self.channel = channel

    def post_to_channel(self):
        print(f"The post was published on {self.channel}: {self.message}")


def post_a_message(channel: str, message: str) -> None:
    post_to_twitter = Twitter(channel, message)
    post_to_youtube = Youtube(channel, message)
    post_to_facebook = Facebook(channel, message)
    post_to_twitter.post_to_channel()
    post_to_youtube.post_to_channel()
    post_to_facebook.post_to_channel()


def process_schedule(posts: list, channels: list):
    temp = posts.copy()
    while len(temp):
        for post in temp:
            i = 0
            while i < len(channels):
                if time.time() >= post.timestamp:
                    post_a_message(channels[i].type_of_channel, post.message)
                    i += 1
                if i == len(channels) - 1:
                    temp.remove(post)


def main():
    list_of_posts = [
        Post(message='Hi guys!!', timestamp=1682866912.6884475),
        Post(message='Subscribe!', timestamp=1682860160.410366),
        Post(message='Bye!', timestamp=1682860100.410366)
    ]
    list_of_social_channels = [
        SocialChannel(type_of_channel="youtube", number_of_followers=100),
        SocialChannel(type_of_channel="facebook", number_of_followers=10),
        SocialChannel(type_of_channel="twitter", number_of_followers=1)
    ]

    process_schedule(list_of_posts, list_of_social_channels)


if __name__ == "__main__":
    main()
