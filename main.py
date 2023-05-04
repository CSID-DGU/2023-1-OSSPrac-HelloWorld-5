from flask import Flask, redirect,render_template,request

app=Flask(__name__)

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/result',methods=['POST','GET'])
def result():
    if request.method == 'POST':
        name = request.form.get('name')
        studentnumber = request.form.get('StudentNumber')
        major = request.form.get('Major')
        email_id = request.form.get('email_id')
        email_addr = request.form.get('email_addr')
        gender = request.form.get('gender')
        languages = request.form.getlist('languages')

        return render_template('result.html',name=name,studentnumber=studentnumber,major=major,email_id=email_id,email_addr=email_addr,gender=gender,languages=languages)

if __name__=='__main__':
    app.run(debug=True)