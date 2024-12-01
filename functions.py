import os
import replicate

def img(prompt):
    os.environ["REPLICATE_API_TOKEN"] = "r8_cuawH1rZjE9VXfnhJbHX8pvcup3Gz8G1xNr3R"

    output = replicate.run(
        "nvidia/sana:88312dcb9eaa543d7f8721e092053e8bb901a45a5d3c63c84e0a5aa7c247df33",
        input={
            "size": "1365x1024",
            "style": "any",
            "prompt": prompt
        }
    )
    with open("static/output.png", "wb") as file:
        file.write(output.read())