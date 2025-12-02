---
title: Building a web browser agent with Generative APIs, Holo2 and Selenium
description: Follow our step by step guide to build a web browser agent with Holo2, Selenium and Scaleway Generative APIs
tags: inference API selenium browser holo2 agent vision ai
dates:
  validation: 2025-11-28
  posted: 2025-11-28
  validation_frequency: 12
products:
  - generative-apis
difficulty: beginner
usecase:
  - build-and-run-ai
ecosystem:
  - scaleway-only
---
import Requirements from '@macros/iam/requirements.mdx'

# Building a web browser agent with Generative APIs, Holo2 and Selenium

This tutorial will guide you through creating a web agent that can interact with websites using LLM vision and browser automation. You will build on Scaleway's Generative APIs to create a system that can "see" web pages and take actions based on visual understanding. This approach is particularly useful for building more flexible pipelines compared to HTML DOM parsing, and requires less maintenance over time when website HTML code changes.

## Why Holo2 model ?

[Holo2 model](https://huggingface.co/Hcompany/Holo2-30B-A3B) is a Vision Language Model optimized to understand Graphical User Interface (GUI) such as web pages or mobile applications, and perform actions on them. Compared to traditional HTML DOM parsing, using a vision model helps building more flexible pipelines that requires less maintenance over time when website code and structure changes.

## What you will learn
- How to take screenshot and perform actions using ***Selenium***
- How to analyze images and process actions output using ***Holo2 vision model***

<Requirements />

- A Scaleway account logged into the [console](https://console.scaleway.com)
- [Owner](/iam/concepts/#owner) status or [IAM permissions](/iam/concepts/#permission) allowing you to perform actions in the intended Organization
- A valid [API key](/iam/how-to/create-api-keys/)
- Access to the [Generative APIs service](/generative-apis/quickstart/)
- [Python 3.11+](https://www.python.org/downloads/) installed on your local computer
- [Chrome](https://www.google.com/intl/fr/chrome/gsem/download) or [Firefox](https://www.firefox.com/fr/) browser installed on your local computer

## Install required packages

Run the following command to install the required packages:
```bash
pip install openai selenium
```

- `openai` enables to query Holo2 model through Generative APIs
- `selenium` enables interaction with browser

## Import dependencies

Create a new `holo2-agent.py` file with the following content:

```python
#holo2-agent.py
from openai import OpenAI
from selenium import webdriver
from selenium.webdriver.common.actions.action_builder import ActionBuilder
import base64
import os
import json
import time
```

## Define tasks to perform and website to browse

Define what tasks you want your agent to perform and on which website:

```python
#holo2-agent.py
TASKS = ["Accept cookies", "Click on changelog", "Select newly added feature"]
WEBSITE_URL = "https://www.scaleway.com/en/docs/"
```
For this example we will make the agent go to Scaleway Documentation Website, and look for recently added features.

## Create the model output structure

By default, Holo2 outputs text data. However, it can be guided to output coordinates in a structured way using `JSON`.

```python
#holo2-agent.py
output_structure = {
    'x': {
        'description': 'The x coordinate, normalized between 0 and 1000.',
        'type': 'integer'
    },
    'y': {
        'description': 'The y coordinate, normalized between 0 and 1000.',
        'type': 'integer'
    }
}
```

This structure ensures coordinates are valid within the expected range (0-1000 that is normalized and independant from exact browser window size).

## Connect to Scaleway's Generative API

Set up the OpenAI client to connect to Scaleway's API:

```python
#holo2-agent.py
client = OpenAI(
    base_url="https://api.scaleway.ai/v1",
    api_key=os.getenv("SCW_SECRET_KEY")  # Store your IAM API KEY in this environment variable or replace directly with your IAM API key
)
```

## Identify where to click on an image

Create a function that will send a task an interface screenshot to the AI model and output an (x,y) coordinates on the screen. The coordinates corresponds to the location the agent needs to click to perform the task:

```python
#holo2-agent.py
def get_next_action(task):
    # Read and encode the current screenshot
    with open("current_screen.png", "rb") as file:
        image_content = file.read()
        base64_img = base64.b64encode(image_content).decode("utf-8")

    # Send the image and task to the vision model
    response = client.chat.completions.create(
        model="holo2-30b-a3b",
        messages=[
            { 
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_img}",
                        },
                    },
                    {
                        "type": "text",
                        "text": f"""Localize an element on the GUI image according to the provided target and output a click position.
                        * You must output a valid JSON following the format: {json.dumps(output_structure)}
                        Your target is: {task}"""
                    }
                ]
            }
        ],
        max_tokens=10000,
        temperature=0.8,
        top_p=0.95
    )

    # Parse the response
    next_action = json.loads(response.choices[0].message.content)
    return next_action
```

## Automate browser actions

Use Selenium to:
- Take a screenshot of the current page
- Click on the right location to perform the task. 

Click coordinates are retrieved from Holo2 using `get_next_action` function. These coordinates are adjusted to exact browser coordinates using `window.innerWidth` and `window.innerHeight` browser properties.

```python
#holo2-agent.py
driver = webdriver.Chrome() # Use webdriver.Firefox() for Firefox

try:
    # Navigate to the target website
    driver.get(WEBSITE_URL)
    time.sleep(3)  # Wait for the page to load
    
    # Process each task in sequence
    for task in TASKS:
        # Take a screenshot of the current page
        driver.save_screenshot('current_screen.png')
        
        # Get the current page dimensions
        page_width = driver.execute_script("return window.innerWidth;")
        page_height = driver.execute_script("return window.innerHeight;")

        # Get click position from the AI model
        next_action = get_next_action(task)
        
        # Convert normalized coordinates to actual screen coordinates
        click_x = (next_action['x'] / 1000) * page_width
        click_y = (next_action['y'] / 1000) * page_height

        # Create and perform the click action
        action = ActionBuilder(driver)
        action.pointer_action.move_to_location(click_x, click_y)
        action.pointer_action.click()
        action.perform()
        
        print(f"Performing task: {task}. Clicked at coordinates: X={click_x}, Y={click_y}")
        time.sleep(3)  # Wait to see the result
        
finally:
    # Always close the browser
    driver.quit()
```

## Run the agent

Execute the agent with:
```bash
SCW_SECRET_KEY="your_scaleway_secret_key" \
python holo2-agent.py
```

You should see your browser open and perform the given actions until the latest added features are displayed.

Congratulations! You have built a web browser agent navigating through website only based on text written tasks.

## Going further

- Add different tasks and see the agent adapt to them
- Add other actions types such as scrolling through the page or typing text.
- Use [Pydantic](https://docs.pydantic.dev/latest/) to define output structure and check its validity
- Extract information from the browsed page
- Use the agent with "thick" client applications, such as desktop or mobile applications (without selenium)
