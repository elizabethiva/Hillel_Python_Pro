import time
from abc import ABC, abstractmethod


class SocialChannel:
    def __init__(self, type_of_channel: str, number_of_followers: int):
        self.type_of_channel = type_of_channel
        self.number_of_followers = number_of_followers


class PostToChannel(ABC):
    @abstractmethod
    def post_to_channel(self):
        """Post to the channel"""

    @abstractmethod
    def process_schedule(self, timestamp):
        """This function should determine when the post will be published."""


class Post:
    def __init__(self, message: str, timestamp: float):
        self.message = message
        self.timestamp = timestamp


class Twitter(PostToChannel):
    def __init__(self, channel, message):
        self.channel = channel
        self.message = message

    def post_to_channel(self):
        print(f"The post was published on {self.channel}: '{self.message}'")

    def process_schedule(self, timestamp):
        while True:
            if timestamp <= time.time():
                self.post_to_channel()
                break


class Youtube(PostToChannel):
    def __init__(self, channel, message):
        self.channel = channel
        self.message = message

    def post_to_channel(self):
        print(f"The post was published on {self.channel}: '{self.message}'")

    def process_schedule(self, timestamp):
        while True:
            if timestamp <= time.time():
                self.post_to_channel()
                break


class Facebook(PostToChannel):
    def __init__(self, channel, message):
        self.channel = channel
        self.message = message

    def post_to_channel(self):
        print(f"The post was published on {self.channel}: '{self.message}'")

    def process_schedule(self, timestamp):
        while True:
            if timestamp <= time.time():
                self.post_to_channel()
                break


def post_a_message(channel: str, message: str, timestamp: int) -> None:
    if channel == "Twitter":
        social_network = Twitter(channel, message)
    if channel == "Youtube":
        social_network = Youtube(channel, message)
    if channel == "Facebook":
        social_network = Facebook(channel, message)

    social_network.process_schedule(timestamp)


def dispatcher(posts: list, channels: list):
    for post in posts:
        for channel in channels:
            post_a_message(channel.type_of_channel, post.message, post.timestamp)


def main():
    list_of_posts = [
        Post(message="Hi guys!", timestamp=1683031500.6331794),
        Post(message="Subscribe!", timestamp=1683031511.8375683),
        Post(message="Bye!", timestamp=1683031524.2123072),
    ]
    list_of_social_channels = [
        SocialChannel(type_of_channel="Twitter", number_of_followers=1),
        SocialChannel(type_of_channel="Youtube", number_of_followers=100),
        SocialChannel(type_of_channel="Facebook", number_of_followers=10),
    ]

    dispatcher(list_of_posts, list_of_social_channels)


if __name__ == "__main__":
    main()
