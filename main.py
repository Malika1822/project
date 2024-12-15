from g4f.client import Client
client = Client()
while True:
    user_input =input("You: ")
    if user_input.lower()== "exit":
        print("Goodbye!")
        break
    try:
        response = client.chat.completions.create(
            model= "gpt-4o-mini",
            messages=[{"role": "user", "content":user_input}]

        )
        print("AI:", response.choices[0].message.content)
    except Exception as e:
        print("An error occured:", e)