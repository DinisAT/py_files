import openai
import os
from dotenv import load_dotenv

def answer_me():
    openai.api_key = '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'
    # relevant_words = ('food,diet,nutrition,healthy,calories,recipe,meal,vegetables,fruit,protein,carbohydrates,fat,vitamins,minerals,weight,eating,cooking,organic,gluten-free,vegan').split(",")

    a = 0
    while True:
        print('Ask Dinis:')
        string = input()
        if len(string) > 100:
            print("Eita animalllll... Please input no more than 100 characters.")
        else:
            break

    while True:
        print("You want my response to be more Direct or Abstract?: ")
        env = input()
        if env not in ['Direct', 'Abstract']:
            if a == 0:
                a += 1
                print("Deves ser burro, dasss.")

            elif a == 1:
                a += 1
                print("Outra vez animal??")

            elif a == 2:
                a += 1
                print("Foda-se, desisto... Só te chamo BURRO apartir de agora!!")

            elif a >= 3:
                print("Burro!! Type either 'chat' or 'code'.")

        if env == 'Direct':
            diet_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=str(string),
                max_tokens=100,
                temperature=0.8
                )
            output_text = diet_response.get('choices')[0].get('text')
            # conversation = conversation + output_text
            print(output_text)

            while True:
                print("Maybe you wanna specify your answer in a more specific way?:")
                string_2 = input()
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=string_2,
                    max_tokens=100,
                    temperature=0.8
                    )
                output_text_2 = response.get('choices')[0].get('text')
                # conversation = conversation + output_text_2
                print(output_text_2)
                continue
            # else:
            #     print("Sorry, I couldn't find any relevant question about food or diet.")
            #     print('Please ask again')

        elif env == 'Abstract':
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=str(string),
                max_tokens=200,
                temperature=0.4,
                top_p=0.5,
                frequency_penalty=2
            )
            print(response.get('choices')[0].get('text'))

            while True:
                print("Maybe you wanna specify your answer in a more specific way?:")
                string_2 = input()
                response = openai.Completion.create(
                    engine="text-davinci-003",
                    prompt=string_2,
                    max_tokens=200,
                    temperature=0.2,
                    top_p=0.2,
                    frequency_penalty=2
                    )
                output_text_2 = response.get('choices')[0].get('text')
                # conversation = conversation + output_text_2
                print(output_text_2)
                continue
        # else:
        #     print("Invalid option. Please choose chat or code.")
