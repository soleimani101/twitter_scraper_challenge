# Define the prompt for the GPT model
import openai
openai.api_key = "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"
# Define a function to generate text based on user input
def generate_text(input_text):
    # Add the user input to the prompt
    # Call the OpenAI API to generate text
    response = openai.Completion.create(
  model="text-davinci-003",
  prompt="tell me if this is a negative sentence\nanswer + if porsitive and answer - if negative \n\{0}\n".format(input_text),
  temperature=0.7,
  max_tokens=256,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
    )

    # Extract the generated text from the API response
    generated_text = response.choices[0].text.strip()
    return generated_text

# Example usage
# input_text = "alifarhat79 Maybe that’s what’s meant the Beyond part"
# generated_text = generate_text(input_text)
