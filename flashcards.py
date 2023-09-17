# Import necessary libraries
import streamlit as st
import os
from langchain import PromptTemplate
from langchain.llms import OpenAI
from trubrics.integrations.streamlit import FeedbackCollector

template = """
    The following text requires analysis for the purpose of creating flashcards. Your tasks are:
    - Summarize the main concepts and ideas from the text.
    - Identify and extract potential flashcard candidates based on the following rules:

        1. Distinct definitions or explanations of terms.
           Example Flashcard:
           Q: What is photosynthesis?
           A: Photosynthesis is the process by which green plants and some other organisms use sunlight to synthesize foods with the help of chlorophyll pigments.
           Creative Variant 1: Think of photosynthesis as a "solar-powered food factory" inside plants.
           Creative Variant 2: Imagine plants sunbathing to make their food. That's photosynthesis!

        2. Important dates, events, or milestones.
           Example Flashcard:
           Q: When did the First World War begin?
           A: The First World War began on July 28, 1914.
           Creative Variant 1: Picture it: 1914, a world on the brink, and on July 28, the fuse is lit for WWI.
           Creative Variant 2: Remember WWI's start as a summer event: July 28, 1914.

        3. Key principles or theories.
           Example Flashcard:
           Q: What is Newton's First Law of Motion?
           A: Newton's First Law states that an object will remain at rest or in uniform motion in a straight line unless acted upon by an external force.
           Creative Variant 1: Think of Newton's First Law as the "laziness law": objects like to keep doing what they're doing.
           Creative Variant 2: Picture a sleeping cat. It won't move unless you nudge it. That's Newton's First Law!

        4. Lists or sequences that need memorization.
           Example Flashcard:
           Q: List the first three planets in our solar system.
           A: Mercury, Venus, Earth.
           Creative Variant 1: Remember the order with "My Very Eager..." for Mercury, Venus, Earth.
           Creative Variant 2: Picture a lineup: Mercury first, then Venus shining bright, followed by our home, Earth.

        5. Comparisons or contrasts between concepts.
           Example Flashcard:
           Q: How do mitosis and meiosis differ?
           A: Mitosis results in two identical daughter cells, whereas meiosis results in four genetically different cells.
           Creative Variant 1: Mitosis is like cloning. Meiosis is like shuffling a deck of genes.
           Creative Variant 2: Think of mitosis as "twinning" and meiosis as "mixing it up."

        6. Any formulas, equations, or rules.
           Example Flashcard:
           Q: What is the formula for the area of a circle?
           A: The formula is A = πr^2, where r is the radius of the circle.
           Creative Variant 1: Picture a circle. Its area is all about its radius, squared, dancing with π.
           Creative Variant 2: Remember: π loves to square dance with the circle's radius for the area!

    Please ensure that the suggestions are concise, clear, and easily understandable.

    Provided Text:
    {user_text}

    YOUR FLASHCARD SUGGESTIONS:
"""


prompt = PromptTemplate(
    input_variables=["user_text"],
    template=template,
)

def load_LLM(openai_api_key):
    """Logic for loading the chain"""
    llm = OpenAI(temperature=0.3, openai_api_key=openai_api_key)
    return llm

# Load API key from environment variable
openai_api_key = os.environ.get("OPENAI_API_KEY")
if not openai_api_key:
    st.error("OpenAI API key not found in environment variables!")

# Set page configuration
st.set_page_config(
    page_title="Flashcard Generator",
    page_icon=":rocket:",
    layout="wide",
)

st.markdown("""
## Flashcard Generator with GPT

Welcome to the Flashcard Generator! This tool is designed to help you extract and create flashcards from any document or text you provide. Here's how to use it:

1. **Paste Your Document**: In the textbox provided, paste the content from which you'd like to generate flashcards. The current limit is 5000 characters.
2. **Generate Flashcards**: After pasting your text, click on the "Generate Flashcards" button. The app will analyze your content and suggest potential flashcards based on the main concepts, definitions, and other important information.
3. **Review & Edit**: The generated flashcards will be displayed below. Review them and make any necessary edits to ensure they fit your needs.
4. **Feedback is Gold**: Your feedback is invaluable to us. By providing feedback, you help us improve and keep this app running. So, if you find this tool helpful or have suggestions for improvement, please let us know!

Thank you for using the Flashcard Generator. Happy studying!
""")
            


# Textbox for users to input their document content with a character limit
user_text = st.text_area("Paste your document content here:", max_chars=7000)

# Button to trigger the GPT analysis
if st.button("Generate Flashcards"):

    # Load the LLM with the provided API key and temperature
    llm = load_LLM(openai_api_key)
    
    # Use the LLM to improve the email
    prompt_with_email = prompt.format(user_text=user_text)
    response = llm(prompt_with_email)
    st.write(response)

# Trubrics Feedback Collector
collector = FeedbackCollector(
    project="flashcards",
    email=os.environ.get("TRUBRICS_EMAIL"),
    password=os.environ.get("TRUBRICS_PASSWORD"),
)

collector.st_feedback(
    component="rating",
    feedback_type="faces",
    model="gpt-3.5-turbo",
    prompt_id=None,  # see prompts to log prompts and model generations
    open_feedback_label='[Optional] Provide additional feedback'
)


# Display the text description
st.write("If you like my work, consider supporting me:")

# Embed the custom "Buy Me A Coffee" button
st.markdown("""
    <a href="https://www.buymeacoffee.com/sherlockanddan" target="_blank">
        <img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;">
    </a>
""", unsafe_allow_html=True)
