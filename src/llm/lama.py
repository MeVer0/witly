import base64

import requests
import json

from base_llm import BaseLLM
import src.dto as dto


class LlamaLLM(BaseLLM):
    def __init__(self):
        super().__init__()
        self.api_url = 'http://localhost:11434/api'

    async def ask_with_api(
            self,
            prompt: str,
            suffix: str | None = None,
            images: list[base64] | None = None,
            format: str | None = None,
            options: str | None = None,
            system: str | None = None,
            template: str | None = None,
            context: str | None = None,
            stream: str | None = None,
            raw: str | None = None,
            keep_alive: str | None = None,

    ) -> dto.LlamaResponse:

        url = self.api_url + '/generate'



def ask():

    url = 'http://localhost:11434/api/generate'

    body = {
        "model": "llama3.1",
        "prompt": "почему трава зеленая?",
        "stream": False
    }
    headers = {
        'Content-Type': 'application/json'
    }
    r = requests.post(url, headers=headers, data=json.dumps(body))
    print(r.text)


if __name__ == '__main__':
    ask()
