from abc import ABC, abstractmethod
import PIL
from google import genai


class FoundationModel(ABC):
    
    def __init__(self, system_instructions: str):
        self.system_instructions = system_instructions

    @abstractmethod
    def generate_text(self, prompt: str, image: PIL.Image) -> str:
        pass

class APIModel(FoundationModel):

    def __init__(self, gemini_api_key):
        super().__init__(self)
        self.client = genai.Client(
            api_key = gemini_api_key
        )

    def generate_text(self, prompt, image):
        interaction = self.client.interactions.create(
            model="gemini-3.5-flash",
            input="Explain how AI works in a few words"
        )
        print(interaction.output_text)

class LocalModel(FoundationModel):

    def __init__(self):
        super().__init__(self)

    def generate_text(self, prompt, image):
        pass