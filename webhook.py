from flask import Flask, request

app=Flask(__name__)

@app.route("/", methods=["POST"])
def webhook():
    print(request.json)
    return "hola"

if __name__ =="__main__":
    app.run(host="0.0.0.0", port=4000)