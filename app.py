import streamlit as st
import re

st.set_page_config(page_title="Password Strength Checker", page_icon="🔒")

st.title("🔒 Password Strength Checker")
st.markdown("""
## Welcome to the ultimate password strength checker! 🔥
Use this simple tool to check the strength of your password and get suggestions on how to make it stronger.
We will give you helpful tips to create a **Strong Password** 🔒
""")
password = st.text_input("Enter your password", type="password")
feedback = []
score = 0

if password:  # Check if the password is not empty
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("❌ Password should be at least 8 characters long.")

    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("❌ Password should contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):  # checks if password contains a digit
        score += 1
    else:
        feedback.append("❌ Password should contain at least one digit.")

    if re.search(r"\W", password):  # checks if password contains a special character
        score += 1
    else:
        feedback.append("❌ Password should contain at least one special character.")

    if score == 4:
        feedback.append("✅ Password Strength: strong!")
    elif score >= 2:
        feedback.append("⚠️ Password Strength: moderate.")
    else:
        feedback.append("❌ Password Strength: weak.")

    if feedback:
        st.markdown("### Suggestions for Strong Password:")
        for tip in feedback:
            st.write(tip)
else:
    st.info("Please enter a password to check its strength.")