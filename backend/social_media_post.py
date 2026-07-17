import PIL


class SocialMediaPost:
    
    def __init__(self, text: str, image: PIL.Image):
        self.text = text
        self.image = image

class SocialMediaPostCollection:

    def __init__(self, post_collection: list[SocialMediaPost]):
        self.post_connection = post_collection

    def save(self):
        pass