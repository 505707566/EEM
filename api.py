import atexit
import json
import os
import requests
from msal import PublicClientApplication, SerializableTokenCache

class LLMClient:
    _ENDPOINT = "https://fe-26.qas.bing.net/completions"
    _SCOPES = ["api://68df66a4-cad9-4bfd-872b-c6ddde00d6b2/access"]

    def __init__(self):
        self._cache = SerializableTokenCache()
        atexit.register(
            lambda: open(".llmapi.bin", "w").write(self._cache.serialize())
            if self._cache.has_state_changed
            else None
        )

        self._app = PublicClientApplication(
            "68df66a4-cad9-4bfd-872b-c6ddde00d6b2",
            authority="https://login.microsoftonline.com/72f988bf-86f1-41af-91ab-2d7cd011db47",
            token_cache=self._cache,
        )
        if os.path.exists(".llmapi.bin"):
            self._cache.deserialize(open(".llmapi.bin", "r").read())

    def send_request(self, model_name, request):
        token = self._get_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
            "X-ModelType": model_name,
        }
        body = str.encode(json.dumps(request))
        try:
            response = requests.post(LLMClient._ENDPOINT, data=body, headers=headers)
            return response.json()
        except:
            return {}

    def send_stream_request(self, model_name, request):
        token = self._get_token()
        headers = {
            "Content-Type": "application/json",
            "Authorization": "Bearer " + token,
            "X-ModelType": model_name,
        }
        body = str.encode(json.dumps(request))
        response = requests.post(
            LLMClient._ENDPOINT, data=body, headers=headers, stream=True
        )
        for line in response.iter_lines():
            text = line.decode("utf-8")
            if text.startswith("data: "):
                text = text[6:]
                if text == "[DONE]":
                    break
                else:
                    yield json.loads(text)

    def _get_token(self):
        accounts = self._app.get_accounts()
        result = None

        if accounts:
            chosen = accounts[0]
            result = self._app.acquire_token_silent(LLMClient._SCOPES, account=chosen)

        if not result:
            flow = self._app.initiate_device_flow(scopes=LLMClient._SCOPES)

            if "user_code" not in flow:
                raise ValueError(
                    "Fail to create device flow. Err: %s" % json.dumps(flow, indent=4)
                )

            print(flow["message"])
            result = self._app.acquire_token_by_device_flow(flow)

        return result["access_token"]

if __name__ == "__main__":
    #client = LLMClient()
    #token = client._get_token()
    #print("Access Token:", token)
    llm_client = LLMClient()
 
    request_data = {
            "prompt":"Seattle is",
            "max_tokens":50,
            "temperature":1,
            "top_p":1,
            "n":5,
            "stream":False,
            "logprobs":None,
            "stop":"\n"
    }
    
    response = llm_client.send_request('dev-text-davinci-003', request_data)
    print(response)