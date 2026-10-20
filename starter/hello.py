import anthropic

client = anthropic.Anthropic()  # reads ANTHROPIC_API_KEY from the environment

response = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Say hello in one sentence."}],
)

for block in response.content:
    if block.type == "text":
        print(block.text)
