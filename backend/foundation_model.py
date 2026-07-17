from abc import ABC, abstractmethod
import PIL

class FoundationModel(ABC):
    
    def __init__(self, system_instructions: str):
        self.system_instructions = system_instructions

    @abstractmethod
    def generate_text(self, prompt: str, image: PIL.Image) -> str:
        pass

class APIModel(FoundationModel):

    def __init__(self):
        super().__init__(self)

    def generate_text(self, prompt, image):
        pass

class LocalModel(FoundationModel):

    def __init__(self):
        super().__init__(self)

    def generate_text(self, prompt, image):
        pass