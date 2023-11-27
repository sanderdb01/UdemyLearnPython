from flask import Flask, render_template, request
import backend


app = Flask(__name__)

# main part of the program
# decorator expression. Connects the function route() to the home() function
# executes the home() function when the user visits the url "/", which is the main page. If they had (for example) an about page, then 
# it would be "/about"
@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("index.html")
    if request.method == "POST":
        text = request.form.get('textbox')
        return render_template("index.html", 
                               output = backend.meters_feet(float(text)),
                               user_text = text)

# if this script/py file is imported, then the __name__ would be the name on the actual file. However, if you are actually running the script, then the __name__ 
# would be __main__. So, the code below is to say that if we are directly running app.py, then call app.run(), but if you are imported by a different script, 
# then dont run this code.
if __name__ == "__main__":
    app.run()