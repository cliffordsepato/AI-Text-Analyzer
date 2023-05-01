# Social Filter App 💬
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://social-filter.streamlit.app)

This streamlit app is powered by OpenAI's GPT-3 Davinci model and is designed to detect inappropriate language, including hate speech, offensive language, and other forms of online abuse. The app aims to promote safe and respectful online communication, while also empowering users to take responsibility for the content they post online.

[![Streamlit Demo app #1](https://img.youtube.com/vi/u9BRI4LgMM0/0.jpg)](https://youtu.be/u9BRI4LgMM0)


# Installation 💥

To run this application, you need to have Python 3.7+ installed on your machine. Once you have Python installed, you can clone this repository and install the required packages by running:

- Clone the repository:
`git clone https://github.com/cliffordsepato/Social-Filter-APP.git`
- Navigate to the project directory:`cd <your-repo>`
- Install the required dependencies:
`pip install -r requirements.txt`

### Additional steps

1. Open a text editor or code editor on your local machine.

2. Create a new file and save it as ".env" in your project directory.

3. Add the following line to the file, replacing "your_api_key_here" with your actual API key:`OPENAI_API_KEY=your_api_key_here`

4. Save the file.

Once you have created the .env file, you can load the API key into your app by importing the os module and using the os.getenv() function to read the value of the OPENAI_API_KEY environment variable. Here is an example:


```
import os
import openai

# load environment variable
load_dotenv()

# Load the API key from the environment variable
openai.api_key = os.getenv("OPENAI_API_KEY")
```

# Usage ✨

To start the application, run the following command:

`streamlit run app.py`

# Features 🚀
The application offers the following features:

* Powered by Artificial Intelligence(AI)
* Detects hate speech, offensive language, and other forms of online abuse.
* Provides feedback and suggestions: If the app detects any problematic language, it provides clear and specific feedback to the user. 
* Robust examples: The app includes both appropriate and inappropriate language examples, allowing users to test the app with a variety of different inputs and contexts.
* Easy to use: The app has a simple and intuitive user interface that makes it easy for users to check their text for inappropriate language.

# Contributing 🤝
Contributions are always welcome! If you want to contribute to this project, please follow these steps:

* Fork this repository.
* Create a new branch with your feature or bug fix.
* Commit your changes and push them to your fork.
* Submit a pull request.


# Author 📝

Please feel free to contact us with any issues, comments, or questions.

#### Clifford Sepato [![Twitter URL](https://img.shields.io/twitter/url/https/twitter.com/bukotsunikki.svg?style=social&label=Follow%20%40csepato)](https://twitter.com/csepato)

- Email: <codingwithcliff@gmail.com>
- LinkedIn: https://linkedin.com/in/cliffordsepato

# How to support this project ❤️

You can support the project by buying me a coffee ☕️.

<a href="https://www.buymeacoffee.com/dxc2023" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>

If you find this project helpful, please consider giving it a star⭐ on GitHub and sharing it with others who might benefit from it. 
  
Your support helps keep this project alive and enables me to continue improving it. 

Thank you!😊

# License

The Social Filter app is released under the MIT License.
