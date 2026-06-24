import streamlit as st
import re
from fractions import Fraction

# 1. Page Configuration & Header
st.set_page_config(page_title="Homework Copilot AI", page_icon="🚀")
st.title("🚀 Homework Copilot AI")
st.subheader("The ultimate platform for 5th grade conquerors")

# 2. Security Passcode Gate
passcode = st.text_input("Enter Secret App Passcode:", type="password")

if passcode == "Empire2026":
    st.success("🔓 ACCESS GRANTED: System Online.")
    
    # 3. Interactive Web Interface Dropdown
    feature = st.selectbox("Choose Your Tool:", ["Math Explainer", "Reading Log"])
    user_data = st.text_input("Paste your homework or book details here:")
    
    if st.button("Run AI Engine"):
        if feature == "Math Explainer":
            # Fraction check
            if "/" in user_data:
                fraction_strings = re.findall(r'\d+/\d+', user_data)
                if len(fraction_strings) >= 2:
                    frac1, frac2 = Fraction(fraction_strings), Fraction(fraction_strings)
                    st.info(f"AI Clue: Adding fractions! {frac1} + {frac2} = {frac1 + frac2}.")
                else:
                    st.warning("Please entnter at least two fractions.")
            else:
                # Whole numbers check
                numbers = [int(num) for num in re.findall(r'\d+', user_data)]
                if len(numbers) >= 2 and ("altogether" in user_data.lower() or "total" in user_data.lower()):
                    st.info(f"AI Clue: 'Altogether' detected. Add {numbers} and {numbers}. Answer is {numbers + numbers}.")
                else:
                    st.warning("AI Clue: Scanning input... Read your problem carefully for keywords!")
                    
        elif feature == "Reading Log":
            st.info(f"AI Log Core: Summarizing content based on target text -> '{user_data}'")
else:
    if passcode != "":
        st.error("❌ ACCESS DENIED: Invalid passcode matrix.")
