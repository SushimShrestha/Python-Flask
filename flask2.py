from flask import Flask, render_template

app=Flask(__name__)
@app.route("/index")
def first_flask_webpage():
    name="flask"
    return render_template('index.html', variable= name)
app.run(debug=True)