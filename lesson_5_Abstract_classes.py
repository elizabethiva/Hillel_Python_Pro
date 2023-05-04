import time
from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class SocialChannel(ABC):
    type_of_channel: str
    number_of_followers: int

    @abstractmethod
    def post_a_message(self, channel, message_to_post):
        """Post to the channel"""


@dataclass
class Post:
    message: str
    timestamp: int


class Twitter(SocialChannel):
    def __init__(self, number_of_followers: int):
        self.type_of_channel = Twitter.__name__
        self.number_of_followers = number_of_followers

    def post_a_message(self, message_to_post):
        print(f"The post was published on {self.type_of_channel}: '{message_to_post}'")


class Youtube(SocialChannel):
    def __init__(self, number_of_followers: int):
        self.type_of_channel = Youtube.__name__
        self.number_of_followers = number_of_followers

    def post_a_message(self, message_to_post):
        print(f"The post was published on {self.type_of_channel}: '{message_to_post}'")


class Facebook(SocialChannel):
    def __init__(self, number_of_followers: int):
        self.type_of_channel = Facebook.__name__
        self.number_of_followers = number_of_followers

    def post_a_message(self, message_to_post):
        print(f"The post was published on {self.type_of_channel}: '{message_to_post}'")


def process_schedule(posts: list, social_channels: list):
    """This function sorts the posts in ascending order of timestamp and calls the function post_a_message at the specified time."""
    sorted_posts_list = sorted(posts, key=lambda post: post.timestamp)
    for post in sorted_posts_list:
        for channel in social_channels:
            while True:
                if post.timestamp <= time.time():
                    channel.post_a_message(post.message)
                    break


def main():
    list_of_posts = [
        Post(message="Hi guys!", timestamp=1683210096.424286),
        Post(message="Subscribe!", timestamp=1683210097.424286),
        Post(message="Bye!", timestamp=1683210099.424286),
    ]
    list_of_social_channels = [
        Twitter(number_of_followers=1000),
        Youtube(number_of_followers=100),
        Facebook(number_of_followers=10),
    ]

    process_schedule(list_of_posts, list_of_social_channels)


if __name__ == "__main__":
    main()