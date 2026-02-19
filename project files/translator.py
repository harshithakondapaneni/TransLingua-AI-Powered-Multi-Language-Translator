import streamlit as st
from google import genai

# Initialize Gemini Client
client = genai.Client(api_key="Api Key")

st.set_page_config(page_title="TransLingua - AI Translator", page_icon="🌍")

st.title("🌍 TransLingua - AI Powered Universal Translator")
st.write("Translate text between any languages")

# User Input
text = st.text_area("📝 Enter text to translate:")

target_language = st.text_input("🌍 Enter target language (e.g., Hindi, Spanish, Japanese, Arabic...)")

if st.button("🚀 Translate"):
    if text.strip() and target_language.strip():
        try:
            prompt = f"""
            1. Detect the language of the following text.
            2. Translate it into {target_language}.
            3. Return the response in this clean format:

            Detected Language:
            <language name>

            Translation:
            <translated text>

            Text:
            {text}
            """

            response = client.models.generate_content(
                model="gemini-2.5-flash",   # use your working model name
                contents=prompt
            )

            # Clean UI Output
            st.success("✅ Translation Completed")
            st.markdown(response.text)

        except Exception as e:
            st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter both text and target language.")