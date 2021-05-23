from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('kontent.html')

@app.route('/about/<name>')
def user(name):
    dane = {'tytul': 'O mnie','tresc':'about '+name}
    return render_template('kontent.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/about')
def usr():
    dane = {'tytul': 'O mnie','tresc':'about'}
    return render_template('kontent.html', tytul=dane['tytul'], tresc=dane['tresc'])

@app.route('/info')
def info():
    dane = {'tytul': 'Informacje'}
    posty = [
        {
            'author': {'username': 'Marcin'},
            'tresc': 'Pierwszy wpis!'
        },
        {
            'author': {'username': 'Ariel'},
            'tresc': 'Post ostatni :('
        }]
    return render_template('kontent.html', tytul=dane['tytul'], posty=posty)
if __name__ == "__main__":
 app.run()


