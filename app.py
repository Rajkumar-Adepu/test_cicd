from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
   return "Jai Shree Ram"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=8080)
#save this file as app.py