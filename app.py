from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home_page():
    #return render_template("index.html")
    food = ["Pizza", "Ice cream", "Chips"] 
    return render_template(
		"index.html",
		food=food)


if __name__ == '__main__':
   app.run(debug = True)
