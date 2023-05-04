from flask import Flask, redirect,render_template,request

app=Flask(__name__)

@app.route('/',methods=['POST','GET'])

def main():
    return render_template('main.html')

if __name__=='__main__':
    app.run(debug=True)