import PIL


class SocialMediaPost:
    
    def __init__(self, text: str, images: list[PIL.Image]):
        self.text = text
        self.images = images

class SocialMediaPostCollection:

    def __init__(self, raw_texts_images):
        self.raw_texts_images = raw_texts_images

    def save(self):
        pass