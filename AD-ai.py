import openai
  
openai.api_key = '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'


def get_completion(prompt, model="gpt-3.5-turbo"):

    messages = [{"role": "system", "content": prompt}]

    response = openai.ChatCompletion.create(

    model=model,

    messages=messages,

    temperature=0,

    )

    return response.choices[0].message["content"]

product = input("Enter Product : ")
country = input("Enter Country : ")
words = str(input("Enter word limit : "))
prompt = f"Create {country} based ad banner for {product} with proper formatting as text in {words} words"
print(prompt)
response = get_completion(prompt)

path = f"/Users/mohamedmafaz/Desktop/AD_{country}.txt"
with open(path , 'w') as f:
    f.write(response)

print(f"Generated and saved at {path}")