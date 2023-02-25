import openai
import requests
from fastapi import FastAPI, Path
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

@app.get(r'/openai/{prompt}')
def code_review(prompt: str = Path(None, description='Pass the item_id of the item you want to view') ):
    API_KEY = ''

    openai.api_key = API_KEY
    model = 'text-davinci-003'

    response = openai.Completion.create(
        prompt=prompt,
        model=model
    )

    return response.choices[0].text



class Prompt(BaseModel):
    text: str



@app.post("/items/")
async def create_item(prompt: Prompt):

    # return item.name
    API_KEY = ''

    openai.api_key = API_KEY
    model = 'text-davinci-003'

    response = openai.Completion.create(
        prompt=prompt.text,
        model = 'text-davinci-003'
    )

    return response.choices[0].text

code_review('How big is the moon?')
# test = requests.post('http://127.0.0.1:8000/items/', json={"text":"how are you today?"})


