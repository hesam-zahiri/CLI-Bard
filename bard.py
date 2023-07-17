import openai

def main():
    api_key = input("Enter your API key: ")

    # Set API key
    openai.api_key = api_key

    # 
    prompt = input("Enter your quastion: ")

    # Take the desired entry
    response = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=100
    )

    # Show answer
    print(response.choices[0].text.strip())

if __name__ == '__main__':
    main()

