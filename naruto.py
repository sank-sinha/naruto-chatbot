import openai
import streamlit as st
import random
from streamlit_chat import message

# Set OpenAI API key
openai.api_key = "YOUR_OPENAI_API_KEY"

naruto_characters = {
    "Naruto Uzumaki": {"bio": "Believes in never giving up, the power of friendship, and turning pain into strength.", "image": "https://i.imgur.com/Naruto.jpg"},
    "Sasuke Uchiha": {"bio": "Driven by revenge and justice, but ultimately seeks redemption and purpose.", "image": "https://i.imgur.com/Sasuke.jpg"},
    "Itachi Uchiha": {"bio": "Sacrifices personal happiness for the greater good, embodying deep wisdom and suffering.", "image": "https://i.imgur.com/Itachi.jpg"},
    "Kakashi Hatake": {"bio": "Teaches the value of teamwork, learning from the past, and staying calm under pressure.", "image": "https://i.imgur.com/Kakashi.jpg"},
    "Jiraiya": {"bio": "A wise and pervy sage who believes that love and passing down knowledge define one’s legacy.", "image": "https://i.imgur.com/Jiraiya.jpg"},
    "Shikamaru Nara": {"bio": "A genius strategist who values intellect over strength but learns responsibility over time.", "image": "https://i.imgur.com/Shikamaru.jpg"},
    "Madara Uchiha": {"bio": "Sees peace as an illusion and believes in power as the ultimate tool of control.", "image": "https://i.imgur.com/Madara.jpg"},
    "Obito Uchiha": {"bio": "Represents lost idealism, the struggle between love and hatred, and redemption.", "image": "https://i.imgur.com/Obito.jpg"}
}

# Multiple-choice questions
questions = [
    {"question": "What drives you the most?", "options": ["Love", "Power", "Justice", "Wisdom"]},
    {"question": "Which ninja skill would you want?", "options": ["Shadow Clone Jutsu", "Sharingan", "Rasengan", "Susanoo"]},
    {"question": "What’s your greatest strength?", "options": ["Loyalty", "Strategy", "Resilience", "Ambition"]}
]

# Streamlit UI Configuration
st.set_page_config(page_title="Kreo x Naruto | Which character are you?", page_icon="🍥", layout="centered")
st.title("🍥 Kreo x Naruto | Which character are you? 🌀")
st.write("Answer three questions, and I'll tell you which Naruto character matches your personality! 🤔🔥")

# Ask three multiple-choice questions
answers = []
for idx, q in enumerate(questions):
    st.subheader(q["question"])
    user_choice = st.radio("Select one:", q["options"], key=f"q{idx}")
    answers.append(user_choice)

# Submit button to reveal results
if st.button("Reveal My Ninja Identity 🥷"):
    if all(answers):
        assigned_character = random.choice(list(naruto_characters.keys()))
        character_bio = naruto_characters[assigned_character]["bio"]
        character_image = naruto_characters[assigned_character]["image"]
        
        st.subheader(f"🥷 You are most like {assigned_character}! 🌀")
        st.image(character_image, caption=assigned_character, use_column_width=True)
        st.write(f"{character_bio}")
        
        # Fun animated response
        st.markdown(
            f"""
            <div style="text-align: center; font-size: 24px; color: orange; font-weight: bold;">
                <p>🔥 Your ninja spirit burns strong! 🔥</p>
                <p>Embrace your path, {assigned_character}!</p>
            </div>
            """, unsafe_allow_html=True
        )
        
        # Social media challenge
        st.write("📸 Take a screenshot and share it on your Instagram stories with **#KreoxNaruto** and tag **@kreosphere** to win the Giveaway!")

# Funky CSS Animations
st.markdown(
    """
    <style>
        @keyframes glow {
            0% { text-shadow: 0 0 5px yellow; }
            50% { text-shadow: 0 0 20px orange; }
            100% { text-shadow: 0 0 5px yellow; }
        }
        .stTitle { animation: glow 2s infinite alternate; }
    </style>
    """,
    unsafe_allow_html=True
)

# Background animation (experimental)
st.markdown(
    """
    <style>
    body {
        background: linear-gradient(45deg, #ff6a00, #ee0979);
        background-size: 400% 400%;
        animation: gradientBG 10s ease infinite;
    }
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("💨 Run through the Hidden Leaf Village and embrace your ninja destiny! 🏯")
