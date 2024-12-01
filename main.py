import streamlit as st
import replicate
import os

st.button("Reset", type="primary")
if st.button("Say hello"):
    st.write("Why hello there")
else:
    st.write("Goodbye")

def img():
    os.environ["REPLICATE_API_TOKEN"] = "r8_cuawH1rZjE9VXfnhJbHX8pvcup3Gz8G1xNr3R"

    input = {}

    output = replicate.run(
        "recraft-ai/recraft-v3",
        input={
            "size": "1365x1024",
            "style": "any",
            "prompt": "photo, girl, blue eyes, realistic"
        }
    )

