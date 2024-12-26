import openai

openai.api_key = "your-api-key"


def generate_text(prompt, model="gpt-4o", max_tokens=150):
    """
    Generates text based on the given prompt using OpenAI's ChatGPT models.

    Parameters:
        prompt (str): The input prompt for the model.
        model (str): The ChatGPT model to use. Default is "gpt-3.5-turbo".
        max_tokens (int): The maximum number of tokens to generate.

    Returns:
        str: The generated text.
    """
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        return f"Error: {e}"

# Example usage
if __name__ == "__main__":
    user_prompt = input("Enter a prompt: ")
    generated_text = generate_text(user_prompt)
    print("\nGenerated Text:\n", generated_text)
