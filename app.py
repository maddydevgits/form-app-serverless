from flask import Flask,render_template,redirect,request,Response
import requests
from flask_cors import CORS
import json
from apis import *

app=Flask(__name__)
CORS(app)

@app.route('/')
def indexPage():
    return render_template('index.html')

@app.route('/registerForm',methods=['POST','GET'])
def registerForm():
    name=request.form['name']
    rollno=request.form['rollno']
    resumelink=request.form['resumelink']
    email=request.form['email']
    phoneno=request.form['phoneno']
    currentsem=request.form['currentsem']
    aggregate=request.form['aggregate']
    department=request.form['department']
    print(name,rollno,resumelink,email,phoneno,currentsem,aggregate,department)
    data={}
    data['name']=name
    data['rollno']=rollno
    data['resumelink']=resumelink
    data['email']=email
    data['phoneno']=phoneno
    data['currentsem']=currentsem
    data['aggregate']=aggregate
    data['department']=department
    result=requests.post(postApi,json=data)
    print(result.text)
    return redirect('/')

@app.route('/result',methods=['POST','GET'])
def resultPage():
    k=requests.get(getApi)
    data=json.loads(k.text)
    print(data)
    data=data['data']['Items']
    k=[]
    for i in range(len(data)):
        dummy=[]
        dummy.append(data[i]['department'])
        dummy.append(data[i]['rollno'])
        dummy.append(data[i]['resumelink'])
        dummy.append(data[i]['aggregate'])
        dummy.append(data[i]['email'])
        dummy.append(data[i]['phoneno'])
        dummy.append(data[i]['name'])
        dummy.append(data[i]['currentsem'])
        k.append(dummy)
    print(k)
    l=len(k)

    return render_template('result.html',dashboard_data=k,len=l)
if __name__=="__main__":
    app.run(debug=True,host='0.0.0.0',port=5001)