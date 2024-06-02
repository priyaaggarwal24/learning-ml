# python -m venv openai-env
# source openai-env/bin/activate

from openai import OpenAI
client = OpenAI()

response = client.images.generate(
    prompt="A mobile phone backcover with outer space view of our solar system",
    n=1,
    size='256x256',
    model='dall-e-2'
)

print(response)
# ImagesResponse(created=1717332274, data=[Image(b64_json=None, revised_prompt=None, url='https://oaidalleapiprodscus.blob.core.windows.net/private/org-ygPjLISINHQTkg48lizrIATB/user-Iwk6OX5U4aFuiWj5h8nsaFry/img-HZzP3SJAnvIbC0jZPwS2SrmA.png?st=2024-06-02T11%3A44%3A34Z&se=2024-06-02T13%3A44%3A34Z&sp=r&sv=2023-11-03&sr=b&rscd=inline&rsct=image/png&skoid=6aaadede-4fb3-4698-a8f6-684d7786b067&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2024-06-01T23%3A59%3A17Z&ske=2024-06-02T23%3A59%3A17Z&sks=b&skv=2023-11-03&sig=GnmqCXQRgfAy26kkbN6kWPFL5pZoIqq0es5mU0HCwfs%3D')])