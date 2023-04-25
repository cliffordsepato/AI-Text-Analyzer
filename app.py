import streamlit as st
import openai
from streamlit.components.v1 import html
from dotenv import load_dotenv
import os

# environment variable
load_dotenv()

# Set up OpenAI API credentials
openai.api_key = os.getenv('API_KEY') or st.secrets['API_KEY']

html_temp = """
                <div style="background-color:{};padding:1px">
                
                </div>
                """


# Define the layout of the app
st.set_page_config(page_title="Social Filter APP")
st.title("Social Filter APP :speech_balloon:")
st.header("Check Your Text for Inappropriate Language")
st.subheader("Enter your text below:")
st.markdown("""[(see examples)](https://github.com/cliffordsepato/Social-Filter-APP/blob/main/examples.md)""")
user_text = st.text_area("Text input") 
submit_button = st.button("Check Text")

with st.sidebar:
    st.markdown("""
    # About 🤖 
    Social Filter is powered by OpenAI's GPT-3 [Davinci model](https://platform.openai.com/docs/models/overview) and is designed to detect inappropriate language, including hate speech, offensive language, and other forms of online abuse.
    """)
    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    # How it works?🤔
📝 Simply enter your text in the input field provided.
🔍 Click on the `Check Text` button and wait a few seconds for the analysis to complete.
👀 Check the results to see if any inappropriate content was detected. It's that easy! 

    """)

    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""

⚠️ **DISCLAIMER:** The analysis provided by this AI tool is based on the model's training data and may not accurately identify all forms of inappropriate content.

🛑 As with any machine learning model, the results may be biased or inaccurate in certain cases, and should be taken with a grain of salt.

📌 It's important to note that the analysis does not consider the context or intent of the text. As a result, some innocuous statements may be flagged as inappropriate. 

👉 Use the results as a helpful guide, but always exercise your own judgment and discretion when assessing text for inappropriate content.

    """)

    st.markdown(html_temp.format("rgba(55, 53, 47, 0.16)"),unsafe_allow_html=True)
    st.markdown("""
    Made by [Clifford Sepato](https://twitter.com/csepato)
    """,
    unsafe_allow_html=True,
    )
# Create a link to your Buy Me a Coffee page
coffee_link = "https://www.buymeacoffee.com/dxc2023"

# Add the button to the sidebar
st.sidebar.write(
    f'<a href="{coffee_link}" target="_blank"><img src="https://cdn.buymeacoffee.com/buttons/v2/default-yellow.png" alt="Buy Me A Coffee" style="height:60px;width:217px;" ></a>',
    unsafe_allow_html=True,
)

# Define a callback function for the submit button
if submit_button:
    # Show a spinner while the analysis is being performed
    with st.spinner(text='Analyzing...'):
    # Send the user's text to the OpenAI API for analysis
        analysis = openai.Completion.create(
        engine="text-davinci-002",
        prompt=f"""I want you to act as an online content moderator for users 
        to check their own text for inappropriate language such as misogynistic 
        humor, insults, jokes that makes reference to family members,sexism, racism, 
        bigorty, hurtful comments, hate speech, offensive language, discrimination 
        and other forms of online abuse, before posting on social media platforms, 
        forums and other online communities. You will be provided with text and 
        your task is to check the users text for any instances of inappropriate language.
        If you determine that a piece of text has inappropriate language,give reasons for why the text contains innappriateand language 
        and provide guidance and context to the user in order for them to correct the inappropriate language and behavior. 
        If there is no innapropriate language found in the text, simply respond with the following:
        "This text does not contain any inappropriate language". 
        You may use the following guidelines in addition to other information you may have 
        as a expert in online content moderation: 
        1.Respect others: Do not use language or actions that are offensive, disrespectful, 
        or hurtful to others. This includes avoiding derogatory comments about race, ethnicity, 
        gender, sexuality, religion, nationality, disability, or any other personal characteristic. 
        2.No harassment or bullying, Do not engage in any form of online harassment, bullying, 
        or stalking. This includes targeting individuals with unwanted messages or actions, 
        or engaging in any behavior that creates a hostile or intimidating online environment.
        Phrases like "I'm nor racist but.." often precedes a racist argument and provides a veneer of political correctness.
        3.No hate speech,Do not use hate speech, which refers to language or actions that promote violence, 
        discrimination, or prejudice against a particular group of people. This includes any content that is racist, 
        sexist, homophobic, transphobic, or otherwise discriminatory.
        4.Do not share jokes that belittles,stereotypes or malign an individual or social group 
        including jokes that employ sexist, homophobic, transphobic or racist humor. 
        The following is also prohibited, Jokes that insult women, devalue women, 
        cement women in a gender role, reduce them and thier actions to exaggerations of existing sexist stereotypes,
        reducing women only to thier bodies, reffering to them as an object or piece of property,
        potraying them solely from a male perspective with no agency or identity, inciting voilence against women 
        to further prop up toxic masculinity and aggression. 
        Please check the following text for any inappropriate language: \n{user_text}\n""",
        #prompt=user_text,
        max_tokens=1024,
        temperature=0.7
    )
    
    # Extract the analysis results and display them to the user
    st.subheader("Results:")
    #st.write(analysis.choices[0].text)

       # Extract the analysis results and display them to the user
    results = analysis.choices[0].text
    if "This text does not contain any inappropriate language" in results:
        st.success("This text does not contain any inappropriate language.")
    else:
        st.warning(results)
        #st.write(results)
