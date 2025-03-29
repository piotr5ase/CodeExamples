# dane z excela i tworzy strone internetowa
# https://patents.google.com/patent/US20090089394A1/en
# casualowe łamanie patentów
import pandas as pd
import flask

app = flask.Flask(__name__)

@app.route('/file', methods=['GET'])
def hello():
    args = flask.request.args
    filename = args.get('filename')
    try:
        filename = filename + ".xlsx"
    except TypeError:#idiotoodpornosc
        return "<meta http-equiv='refresh' content='0; url=http://127.0.0.1:5000/' />"
    site = "<html><head><title>" + filename + "</title><meta charset='utf-8'></head><body>"
    end = "</body></html>"
    try:
        df = pd.read_excel(filename)
        df = df.to_html(na_rep="",index=False,header=True)

        site = site + df + end
    except FileNotFoundError:

        site = site +"Nie znaleziono pliku" + end
    return site

@app.route("/")
def index():
    stri = "<title>Wybierz plik</title><form method='get' action='file'><input type='text' name='filename' id='filename'><input type='submit'></form>"
    return stri

# main driver function
if __name__ == '__main__':
    app.run()