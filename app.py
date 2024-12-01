from flask import Flask
from flask import render_template, request
from functions import img



app = Flask(__name__, static_url_path='/static')

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("ai_generator.html", show_image=False)
    else:
        value_prompt = request.form.get("value_prompt")
        img(value_prompt)
        return render_template("ai_generator.html", show_image=True)


if __name__ == "__main__":
    app.run(debug=True)
