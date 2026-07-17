from abc import ABC, abstractmethod


class SocialMediaConnector(ABC):
    
    @abstractmethod
    def make_post(post):
        pass
    
class XConnector(SocialMediaConnector):

    def make_post(post):
        pass
    
class BskyConnector(SocialMediaConnector):

    def make_post(post):
        pass