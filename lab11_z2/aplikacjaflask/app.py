from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    dane = {'tytul': 'Strona główna'}
    return render_template('index.html', tytul=dane['tytul'])

@app.route('/about/<name>')
def user(name):
    dane = {'tytul': 'O mnie'}
    return render_template('omnie.html',name=name, tytul=dane['tytul'])

@app.route('/about')
def usr():
    dane = {'tytul': 'O mnie'}
    return render_template('omnie.html', name="brak", tytul=dane['tytul'])

@app.route('/info')
def info():
    dane = {'tytul': 'Informacje'}
    return render_template('informacje.html', tytul=dane['tytul'])

if __name__ == "__main__":
 app.run()


