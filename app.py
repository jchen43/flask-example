from flask import Flask
from config import HOST, PORT

app = Flask(__name__)

@app.route("/")
def hello():
    x = 5
    return "hihi testing"


if __name__ == "__main__":
    print("***** STARTING APP ******")
    print("HOST PORT", HOST, PORT)
    app.run(debug=True, host=HOST,port=PORT)
