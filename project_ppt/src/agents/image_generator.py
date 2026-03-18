import os
import requests
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

class ImageGenerator:
    def __init__(self, output_dir="output_images/"):
        self.output_dir = output_dir
        os.makedirs(self.output_dir, exist_ok=True)

    def generate_image(self, prompt, filename=None):
        """
        Generates an image based on the given prompt using OpenAI's API.
        If filename is not provided, it will use the prompt to create a filename.
        """
        url = "https://api.openai.com/v1/images/generations"
        headers = {
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        }
        data = {
            "prompt": prompt,
            "n": 1,
            "size": "512x512"
        }
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        image_url = response.json()["data"][0]["url"]

        # Create a safe filename from the prompt if not provided
        if not filename:
            safe_prompt = "".join(c if c.isalnum() else "_" for c in prompt)[:50]
            filename = f"{safe_prompt}.png"

        file_path = os.path.join(self.output_dir, filename)
        img_data = requests.get(image_url).content
        with open(file_path, "wb") as handler:
            handler.write(img_data)
        return file_path

    def generate_images_from_prompts(self, prompts):
        """
        Accepts a list of prompts and generates images for each.
        Returns a dict mapping prompts to file paths.
        """
        results = {}
        for prompt in prompts:
            file_path = self.generate_image(prompt)
            results[prompt] = file_path
        return results

if __name__ == "__main__":
    generator = ImageGenerator()
    # Example: Extract prompts from a user document (simulate with a list)
    user_prompts = [
        "A futuristic city skyline at sunset",
        "A cat riding a skateboard",
        "A serene mountain landscape with a lake"
    ]
    results = generator.generate_images_from_prompts(user_prompts)
    for prompt, path in results.items():
        print(f"Prompt: {prompt}\nImage saved to: {path}\n")