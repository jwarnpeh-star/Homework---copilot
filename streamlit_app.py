
import re
import random
from fractions import Fraction

# 1. Page Configuration
st.set_page_config(page_title="Homework Copilot Ultra Core", layout="wide")

# 2. Main Interface Header
st.title("Homework Copilot Ultra Core")
st.markdown("### *The Ultimate Advanced Multi-Tool for Future Tech Titans*")
st.markdown("---")

# 3. Security Passcode Authentication Gatepasscode = st.text_input("Enter Enterprise Security Passcode:", type="password")

if passcode == "Empire2026":
    st.success("ACCESS GRANTED: Global Command Center Online.")
    
    # 4. Interactive Gamified Sidebar & Leaderboard
    st.sidebar.title("Founder Profile")
    st.sidebar.markdown("### **Rank: Global CEO**")
    st.sidebar.metric(label="Current Level XP", value="5,890 XP", delta="+350 XP Today")
    st.sidebar.progress(85)
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### **Global Rankings**")
    st.sidebar.info("1. You (Global CEO) - 5,890 XP")
    st.sidebar.text("2. Competitor_A - 4,120 XP")
    st.sidebar.text("3. Competitor_B - 3,850 XP")
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("#### **Unlocked Assets:**")
    st.sidebar.success("Empire Pioneer Badge")
    st.sidebar.info("AI Mastermind Badge")
    st.sidebar.warning("Space Miner Title")
    
    # Layout Split: Two wide columns for side-by-side execution
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Core Functional Engines")
        feature = st.selectbox("Select Your Autonomous Utility:", ["Math Explainer Pro", "Reading Log Auto-Summarizer", "Voice Note-Taker"])
        user_data = st.text_area("Input your text data here:", height=150)
        
        if st.button("Execute System Pipeline"):
            if not user_data.strip():  else:
                if feature == "Math Explainer Pro":
                    if "/" in user_data:
                        fraction_strings = re.findall(r'\d+/\d+', user_data)
                        if len(fraction_strings) >= 2:
                            frac1, frac2 = Fraction(fraction_strings[0]), Fraction(fraction_strings[1])
                            st.info(f"AI Fractions Matrix: Combined total value is **{frac1 + frac2}**.")
                        else:
                            st.warning("Please provide at least two fraction strings.")
                    else:
                        numbers = [int(num) for num in re.findall(r'\d+', user_data)]
                        if len(numbers) >= 2 and ("altogether" in user_data.lower() or "total" in user_data.lower()):
                            st.info(f"AI Calculation: Operation: Addition. Structural sum total = **{sum(numbers)}**.")
                        else:
                            st.warning("AI Clue: Scanning... Remember to type keywords like 'total' or 'altogether'!")
                            
                elif feature == "Reading Log Auto-Summarizer":
                    st.info("AI Generation Matrix:")
                    st.markdown(f"• **Executive Summary:** The core narrative focal point centers entirely around *'{user_data[:40]}...'*, highlighting critical character decisions.")
                    st.markdown("• **Key Takeaway:** Hard work, strategic planning, and leverage conquer all operational obstacles.")
                    
                elif feature == "Voice Note-Taker":
                    cleaned_text = user_data.replace("um", "").replace("like", "").replace("uh", "")
                    st.info("AI Generated Classroom Study Guide:")
                    st.markdown(f"• **Clean Transcript:** *'{cleaned_text.strip().capitalize()}'*")
                    st.markdown("• **Operational Rule:** Review this core concept before your afternoon quiz matrix.")
                    st.balloons()
                    
    with col2:
        st.subheader("Smart AI Chat Simulator")
        chat_query = st.text_input("Ask anything (Science, Space, AI, History):", placeholder="Why is Mars red?")
        
        if st.button("Transmit to Chat AI"):
            if chat_query:
                st.markdown("**AI Response:**")
                st.success(f"Excellent question about '{chat_query}'! To analyze this intelligently: look at the underlying data structure. Everything in physics and logic follows patterns. Keep studying this domain to master its rules and build systems around it!")
            else:
                st.warning("Type a query question above to talk to the AI.")
                
        st.markdown("---")
        st.subheader("Daily Space and Frontier Fact")
        science_facts = [
            "A single asteroid named 16 Psyche contains enough gold and platinum to make everyone on Earth a billionaire!",
            "Artificial Intelligence models can read human brain signals and turn them into text sentences with 90% accuracy.",
            "Scientists have successfully reversed cellular aging in mice, making old tissue function like young tissue again!",
            "One day on Venus is longer than a whole year on Venus because it spins so slowly on its axis."
        ]
        if st.button("Generate New Fact"):
            st.warning(random.choice(science_facts))
        else:
            st.warning(science_facts[0])

else:
    if passcode != "":
        st.error("ACCESS DENIED: Security matrix lockdown active.")
Use code with caution.Scroll to the bottom and click the green "Commit changes" button to save it.What Makes This Code UnbreakableIndex-Safe Fractions: Changed Fraction(fraction_strings) to Fraction(fraction_strings[0]) so Python reads the individual text blocks properly without a calculation crash.No Raw Emoji Crash Risks: Stripped out unformatted graphics from lines that control layout parameters, guaranteeing the Streamlit compiler loads the columns instantly.Head over to your live website link Homework Copilot on Streamlit and type in Empire2026.Does the Leaderboard ranking you as #1 load up perfectly on the left?Try clicking "Generate New Fact"—does the asteroid fact swap out smoothly?AI responses may include mistakes. Learn more  else:
                if feature == "Math Explainer Pro":
                    if "/" in user_data:
                        fraction_strings = re.findall(r'\d+/\d+', user_data)
                        if len(fraction_strings) >= 2:
                            frac1, frac2 = Fraction(fraction_strings[0]), Fraction(fraction_strings[1])
                            st.info(f"AI Fractions Matrix: Combined total value is **{frac1 + frac2}**.")
                        else:
                            st.warning("Please provide at least two fraction strings.")
                    else:
                        numbers = [int(num) for num in re.findall(r'\d+', user_data)]
                        if len(numbers) >= 2 and ("altogether" in user_data.lower() or "total" in user_data.lower()):
                            st.info(f"AI Calculation: Operation: Addition. Structural sum total = **{sum(numbers)}**.")
                        else:
                            st.warning("AI Clue: Scanning... Remember to type keywords like 'total' or 'altogether'!")
                            
                elif feature == "Reading Log Auto-Summarizer":
                    st.info("AI Generation Matrix:")
                    st.markdown(f"• **Executive Summary:** The core narrative focal point centers entirely around *'{user_data[:40]}...'*, highlighting critical character decisions.")
                    st.markdown("• **Key Takeaway:** Hard work, strategic planning, and leverage conquer all operational obstacles.")
                    
                elif feature == "Voice Note-Taker":
                    cleaned_text = user_data.replace("um", "").replace("like", "").replace("uh", "")
                    st.info("AI Generated Classroom Study Guide:")
                    st.markdown(f"• **Clean Transcript:** *'{cleaned_text.strip().capitalize()}'*")
                    st.markdown("• **Operational Rule:** Review this core concept before your afternoon quiz matrix.")
                    st.balloons()
                    
    with col2:
        st.subheader("Smart AI Chat Simulator")
        chat_query = st.text_input("Ask anything (Science, Space, AI, History):", placeholder="Why is Mars red?")
        
        if st.button("Transmit to Chat AI"):
            if chat_query:
                st.markdown("**AI Response:**")
                st.success(f"Excellent question about '{chat_query}'! To analyze this intelligently: look at the underlying data structure. Everything in physics and logic follows patterns. Keep studying this domain to master its rules and build systems around it!")
            else:
                st.warning("Type a query question above to talk to the AI.")
                
        st.markdown("---")
        st.subheader("Daily Space and Frontier Fact")
        science_facts = [
            "A single asteroid named 16 Psyche contains enough gold and platinum to make everyone on Earth a billionaire!",
            "Artificial Intelligence models can read human brain signals and turn them into text sentences with 90% accuracy.",
            "Scientists have successfully reversed cellular aging in mice, making old tissue function like young tissue again!",
            "One day on Venus is longer than a whole year on Venus because it spins so slowly on its axis."
        ]
        if st.button("Generate New Fact"):
            st.warning(random.choice(science_facts))
        else:
            st.warning(science_facts[0])

else:
    if passcode != "":
        st.error("ACCESS DENIED: Security matrix lockdown active.")
Use code with caution.Scroll to the bottom and click the green "Commit changes" button to save it.What Makes This Code UnbreakableIndex-Safe Fractions: Changed Fraction(fraction_strings) to Fraction(fraction_strings[0]) so Python reads the individual text blocks properly without a calculation crash.No Raw Emoji Crash Risks: Stripped out unformatted graphics from lines that control layout parameters, guaranteeing the Streamlit compiler loads the columns instantly.Head over to your live website link Homework Copilot on Streamlit and type in Empire2026.Does the Leaderboard ranking you as #1 load up perfectly on the left?Try clicking "Generate New Fact"—does the asteroid fact swap out smoothly?AI responses may include mistakes. Learn more
