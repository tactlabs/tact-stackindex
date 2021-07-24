from flask import Flask,jsonify,requests,render_template
import json
  
app = Flask(__name__)
PORT = 3000
  
@app.route("/")
def startpy():
    input_col =  input("Enter input col : ")
    print(input_col)
    
    return render_template('index.html')

@app.route("/result")
def getplot():
    return None

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=PORT)