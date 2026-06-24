import streamlit as st
import re
import random
from fractions import Fraction

# 1. App Styling & Layout Configuration
st.set_page_config(page_title=⚡ , "Homework Copilot AI Ultra", page_icon="rocket", layout="wide")


# 2. Daily Science Fact Database
science_facts = [
    "A single asteroid named 16 Psyche contains enough gold and platinum to make everyone on Earth a billionaire!",
    "Artificial Intelligence models can read human brain signals and turn them into text sentences with 90% accuracy.",
    "Scientists have successfully reversed cellular aging in mice, making old tissue function like young tissue again!",
    "One day on Venus is longer than a whole year on Venus because it spins so slowly on its axis."
]

# 3. Main Interface Header
st.title("⚡ Homework Copilot AI st.title("  Homework Copilot AI Utlra")
st.markdown("### *The Ultimate Autonomous Multi-Tool for 5th Grade Leaders & Future Tech Titans*")
st.markdown("---")

# 4. Security Passcode Authentication Gate
passcode = st.text_input("Enter Enterprise Security Passcode:", type="password")

if passcode == "Empire2026":
    st.success("🔓 ACCESS GRANTED: Global Command Center Online.")
    
    # 5. Interactive Gamified Sidebar
    st.sidebar.title("🏆 Founder Profile")
    st.sidebar.markdown("### **Rank: Global CEO** 👔")
    st.sidebar.metric(label="Current Level XP", value="2,450 XP", delta="+150 XP Today")
    st.sidebar.progress(75) # Visual loading bar for level progress
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### **Unlocked Assets:**")
    st.sidebar.success("🥇 Empire Pioneer Badge")
    st.sidebar.info("🤖 AI Mastermind Badge")
    st.sidebar.warning("🚀 Space Miner Title") col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("🛠️ Core Functional Engines")
        feature = st.selectbox("Select Your Autonomous Utility:", ["Math Explainer Pro", "Reading Log Auto-Summarizer", "Voice Note-Taker"])
        user_data = st.text_area("Input your text data here:", height=150)
        
        if st.button("Execute System Pipeline"):
            if not user_data.strip():
                st.error("Please insert text input data to process!")
            else:
                if feature == "Math Explainer Pro":
                    if "/" in user_data:
                        fraction_strings = re.findall(r'\d+/\d+', user_data)
                        if len(fraction_strings) >= 2:
                            frac1, frac2 = Fraction(fraction_strings[0]), Fraction(fraction_strings[1])
                            st.info(f"🧬 **AI Fractions Matrix:** Combined total value is **{frac1 + frac2}**.")
                        else:
                            st.warning("Please provide at least two fraction strings.")
                    else:
                        numbers = [int(num) for num in re.findall(r'\d+', user_data)]
                        if len(numbers) >= 2 and ("altogether" in user_data.lower() or "total" in user_data.lower()):
                            st.info(f"📐 **AI Calculation:** Operation: Addition. Structural sum total = **{sum(numbers)}**.")
                        else:
                            st.warning("AI Clue: Scanning... Remember to type keywords like 'total' or 'altogether'!")
                            else:
                            st.warning("AI Clue: Scanning... Remember to type keywords like 'total' or 'altogether'!")
                            
                elif feature == "Reading Log Auto-Summarizer":
                    st.info("📚 **AI Generation Matrix:**")
                    st.markdown(f"• **Executive Summary:** The core narrative focal point centers entirely around *'{user_data[:40]}...'*, highlighting critical character decisions.")
                    st.markdown("• **Key Takeaway:** Hard work, strategic planning, and leverage conquer all operational obstacles.")
                    
                elif feature == "Voice Note-Taker":
                    cleaned_text = user_data.replace("um", "").replace("like", "").replace("uh", "")
                    st.info("📝 **AI Generated Classroom Study Guide:**")with col2:
        st.subheader("💬 Smart AI Chat Simulator")
        chat_query = st.text_input("Ask anything (Science, Space, AI, History):", placeholder="Why is Mars red?")
        
        if st.button("Transmit to Chat AI"):
            if chat_query:
                st.markdown("**🤖 AI Response:**")
                st.success(f"Excellent question about '{chat_query}'! To analyze this intelligently: look at the underlying data structure. Everything in physics and logic follows patterns. Keep studying this domain to master its rules and build systems around it!")
            else:
                st.warning("Type a query question above to talk to the AI.")
                
        st.markdown("---")
        st.subheader("🌌 Daily Space & Frontier Fact")
        if st.button("Generate New Fact"):
            st.warning(random.choice(science_facts))
        else:
            st.warning(science_facts[0])
else:
    if passcode != "":
        st.error("❌ ACCESS DENIED: Security matrix lockdown active.")
                    st.markdown(f"• **Clean Transcript:** *'{cleaned_text.strip().capitalize()}'*")
                    st.markdown("• **Operational Rule:** Review this core concept before your afternoon quiz matrix.")
                    st.balloons()
                    
    with col2:
        st.subheader("💬 Smart AI Chat Simulator")
        chat_query = st.text_input("Ask anything (Science, Space, AI, History):", placeholder="Why is Mars red?")
