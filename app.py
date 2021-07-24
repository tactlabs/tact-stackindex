<<<<<<< HEAD
from flask import Flask,jsonify,request,render_template
=======
from flask import Flask,jsonify,render_template,request
>>>>>>> 7c70141d11511649efc29deb6bdfc9969bee1f6b
import json
import stackindex
  
app = Flask(__name__)
PORT = 3000
  
@app.route("/",methods=['GET','POST'])
def startpy():
    input_col =  input("Enter input col : ")
    print(input_col)
    
    return render_template('index.html')

@app.route("/result",methods=['POST'])
def getplot():
    input_col = request.form.get('label')
    plot = stackindex.plotdata(input_col)

if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0",port=PORT)