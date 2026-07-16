from abc import ABC, abstractmethod


class SocialMediaConnector(ABC):
    
    @abstractmethod
    def post(message):
        pass
    
class XConnector(SocialMediaConnector):

    def post(message):
        pass
    
class BskyConnector(SocialMediaConnector):

    def post(message):
        pass