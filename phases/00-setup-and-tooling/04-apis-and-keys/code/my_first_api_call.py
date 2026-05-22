from anthropic import Anthropic
import os, json, urllib.request

client = Anthropic()

def calculate_cost(usage, model="claude-sonnet-4-20250514"):
    """
    Calculates the input and output api cost based on usage and displays it.
    """
    prices = {
        "claude-sonnet-4-20250514": {"input": 3.00, "output": 15.00},
    }
    p = prices.get(model, prices[model])
    input_cost = (usage.input_tokens / 1_000_000) * p["input"]
    output_cost = (usage.output_tokens / 1_000_000) * p["output"]
    total = input_cost + output_cost

    print(f"Input tokens:  {usage.input_tokens:,}  → ${input_cost:.6f}")
    print(f"Output tokens: {usage.output_tokens:,} → ${output_cost:.6f}")
    print(f"Total cost:    ${total:.6f}")

def call_with_sdk():
    try:
        import anthropic
    except ImportError:
        print("Install the SDK: pip install anthropic")
        return 
    
    client = anthropic.Anthropic()
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=256,
        messages=[
            {"role": "user", "content": "What is a neural network in one sentence?"}
        ]
    )
    print(f"SDK Response: {response.content[0].text}")
    print(f"Tokens used: {response.usage.input_tokens} in, {response.usage.output_tokens} out ")
    # Calculate the cost and display it
    calculate_cost(response.usage)

def call_with_http():
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "Content-type": "application/json",
        "x-api-key": api_key,
        "anthropic-version": "2023-06-01"
    }
    body = json.dumps({
        "model": "claude-sonnet-4-20250514",
        "max_tokens": 256,
        "messages": [{"role": "user", "content": "What is a neural network in one sentence?"}],
    }).encode()

    req = urllib.request.Request(url, data=body, headers=headers, method="POST")
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f"Raw HTTP response: {result['content'][0]['text']}")
        print(f"Tokens used: {result['usage']['input_tokens']} in, {result['usage']['output_tokens']} out")



if __name__ == "__main__":
    print("=== API Calls ===\n")
    print("1. Using the SDK:")
    call_with_sdk()
    print("\n2. Using raw HTTP:")
    call_with_http()
