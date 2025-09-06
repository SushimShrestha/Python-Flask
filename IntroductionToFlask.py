from flask import Flask

app= Flask(__name__)
@app.route("/")
def first_flask():
    return "this is my first flask program."
app.run(debug=True)