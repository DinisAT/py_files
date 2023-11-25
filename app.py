# import openai
# import streamlit as st

# # Set the OpenAI API key
# openai.api_key = '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'

# def run():
#     st.title("Ask Dinis")

#     # Get user input
#     string = st.text_input("Ask Dinis:")

#     # Get user preference for Direct or Abstract response
#     env = st.selectbox("You want my response to be more Direct or Abstract?", options=['Direct', 'Abstract'])

#     if st.button("Submit"):
#         # Generate response based on user input and preference
#         if env == 'Direct':
#             diet_response = openai.Completion.create(
#                 engine="text-davinci-003",
#                 prompt=str(string),
#                 max_tokens=100,
#                 temperature=0.8
#             )
#             output_text = diet_response.get('choices')[0].get('text')
#             st.write(output_text)

#             # Get additional information if requested by user
#             string_2 = st.text_input("Maybe you wanna specify your answer in a more specific way?")
#             if string_2:
#                 response = openai.Completion.create(
#                     engine="text-davinci-003",
#                     prompt=string_2,
#                     max_tokens=100,
#                     temperature=0.8
#                 )
#                 output_text_2 = response.get('choices')[0].get('text')
#                 st.write(output_text_2)

#         elif env == 'Abstract':
#             response = openai.Completion.create(
#                 engine="text-davinci-003",
#                 prompt=str(string),
#                 max_tokens=200,
#                 temperature=0.4,
#                 top_p=0.5,
#                 frequency_penalty=2
#             )
#             output_text = response.get('choices')[0].get('text')
#             st.write(output_text)

#             # Get additional information if requested by user
#             string_2 = st.text_input("Maybe you wanna specify your answer in a more specific way?")
#             if string_2:
#                 response = openai.Completion.create(
#                     engine="text-davinci-003",
#                     prompt=string_2,
#                     max_tokens=200,
#                     temperature=0.2,
#                     top_p=0.2,
#                     frequency_penalty=2
#                 )
#                 output_text_2 = response.get('choices')[0].get('text')
#                 st.write(output_text_2)
import openai
import streamlit as st

# Set the OpenAI API key
openai.api_key = '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'

# Add the JavaScript code to the Streamlit app
st.set_page_config(
    page_title="Ask Dinis",
    page_icon=":books:",
    layout="wide",
    initial_sidebar_state="expanded",
    # Add the JavaScript code to the Streamlit app
    # js="""
    # if ('userAgentData' in navigator) {
    #     // Use navigator.userAgentData
    # } else {
    #     // Use navigator.userAgent, navigator.appVersion, or navigator.platform
    # }
    # """
)

def run():
    st.title("Ask Dinis")

    # Get user input
    string = st.text_input("")

    # Get user preference for Direct or Abstract response
    env = st.selectbox("You want my response to be more Direct or Abstract?", options=['Direct', 'Abstract'])

    if st.button("Submit"):
        # Generate response based on user input and preference
        if env == 'Direct':
            diet_response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=str(string),
                max_tokens=100,
                temperature=1.
            )
            output_text = diet_response.get('choices')[0].get('text')
            st.write(output_text)
            # string = ""
            # st.text_input("", value=string, key=1)

            # Get additional information if requested by user
            # string_2 = st.text_input("Maybe you wanna specify your answer in a more specific way?", value=string, key=1)

            # if string_2:
            #     response = openai.Completion.create(
            #         engine="text-davinci-003",
            #         prompt=string_2,
            #         max_tokens=100,
            #         temperature=0.8
            #     )
            #     output_text_2 = response.get('choices')[0].get('text')
            #     st.write(output_text_2)

        elif env == 'Abstract':
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=str(string),
                max_tokens=300,
                temperature=0.2,
                top_p=0.3,
                # frequency_penalty=2
            )
            output_text = response.get('choices')[0].get('text')
            st.write(output_text)
            # string = ""
            # st.text_input("", value=string, key=1)

            # # Get additional information if requested by user
            # string_2 = st.text_input("Maybe you wanna specify your answer in a more specific way?")
            # if string_2:
            #     response = openai.Completion.create(
            #         engine="text-davinci-003",
            #         prompt=string_2,
            #         max_tokens=200,
            #         temperature=0.2,
            #         top_p=0.2,
            #         frequency_penalty=2
            #     )
            #     output_text_2 = response.get('choices')[0].get('text')
            #     st.write(output_text_2)
            # st.write(output_text)

if __name__ == '__main__':
    run()
