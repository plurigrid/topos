import os
import openai
from PIL import Image
import io
import base64

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

def analyze_screenshot(image_path):
    base64_image = encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What's in this image? Please describe it in detail."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = openai.ChatCompletion.create(**payload)
    return response.choices[0].message['content']

def analyze_screenshots_in_directory(directory):
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                print(f"Analyzing {file_path}...")
                analysis = analyze_screenshot(file_path)
                print(f"Analysis: {analysis}\n")

if __name__ == "__main__":
    desktop_path = "/Users/barton/Desktop"
    analyze_screenshots_in_directory(desktop_path)
import os
import asyncio
import openai
from PIL import Image
import io
import base64

async def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')

async def analyze_screenshot(image_path):
    base64_image = await encode_image(image_path)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
    }

    payload = {
        "model": "gpt-4-vision-preview",
        "messages": [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "What's in this image? Please describe it in detail."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]
            }
        ],
        "max_tokens": 300
    }

    response = await openai.ChatCompletion.acreate(**payload)
    return response.choices[0].message['content']

async def analyze_screenshots_in_directory(directory):
    tasks = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
                file_path = os.path.join(root, file)
                tasks.append(asyncio.create_task(analyze_single_screenshot(file_path)))
    await asyncio.gather(*tasks)

async def analyze_single_screenshot(file_path):
    print(f"Analyzing {file_path}...")
    analysis = await analyze_screenshot(file_path)
    print(f"Analysis of {file_path}:\n{analysis}\n")

async def eventually_consistent_loop():
    desktop_path = "/Users/barton/Desktop"
    while True:
        await analyze_screenshots_in_directory(desktop_path)
        await asyncio.sleep(60)  # Wait for 60 seconds before the next iteration

if __name__ == "__main__":
    asyncio.run(eventually_consistent_loop())
