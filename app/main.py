from flask import Flask, redirect,render_template,request

app=Flask(__name__)
data_rows = []  # 전체 데이터-각 원소는 Name,Student Number,...로 구성된 딕셔너리로, 행

@app.route('/')
def main():
    return render_template('main.html')

@app.route('/result',methods=['POST','GET'])
def result():
    referring_url = request.referrer  # request가 어디서 들어왔는지에 따라 다르다.
    print("referring_url=",referring_url)
    filename='/'+referring_url.split('/')[-1]  # /뒷부분이 filename이기에 /filename형식 갖추게 한 것
    

            
    if filename == '/':
        data=dict()
        data['name'] = request.form.get('name')
        data['studentnumber'] = request.form.get('StudentNumber')
        data['major'] = request.form.get('Major')
        email_id = request.form.get('email_id')
        email_addr = request.form.get('email_addr')
        data['email'] = email_id + "@" + email_addr
        data['gender'] = request.form.get('gender')
        data['languages'] = str(request.form.getlist('languages'))[1:-1]#양쪽 끝의 '[',']' 제거
        data['languages']=data['languages'].replace("'",'')#'제거하도록 수정
        
        print("data=",data)
        data_rows.append(data)

        # 딕셔너리 학번순으로 나열
        sorted_rows=[]
        order=[]
        for row in data_rows:
            order.append(row['studentnumber'][:4])
            sorted_rows.append(" ")

        s_order = sorted(order)
        for num,i in enumerate(order):
            i_order = s_order.index(i)
            if sorted_rows[i_order] ==" ":
                sorted_rows[i_order] = data_rows[num] 
            else:
                sorted_rows[i_order+1] = data_rows[num] 

        

        return render_template('result.html',rows=sorted_rows) 
    else:  # delete row시 redirect될 때 사용됨.
        return render_template('result.html', rows=data_rows)   # else일 경우 sorted_rows는 선언되지 않았음



@app.route("/delete", methods=['POST'])
def delete():
    rows_to_delete = request.form.getlist('rows[]')
    global data_rows
    new_data_rows = []
    for i in range(len(data_rows)):
        if str(i) not in rows_to_delete:
            new_data_rows.append(data_rows[i])
    data_rows = new_data_rows
    return redirect('/result')

@app.route('/reset')
def reset():
    data_rows.clear()
    return redirect('/')

if __name__=='__main__':
    app.run(debug=True)