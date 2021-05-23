from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def main():
    return render_template('index.html')

@app.route('/about/<name>')
def user(name):
    return render_template('omnie.html', name=name)

@app.route('/about')
def usr():
    return render_template('omnie.html', name="brak")

@app.route('/info')
def info():
    return render_template('informacje.html')



if __name__ == "__main__":
 app.run()


