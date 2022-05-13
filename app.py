

import model1
from flask import Flask , render_template, url_for,request

app=Flask(__name__)

@app.route('/', methods=['POST','GET'])
def index():
    paragraph=""
    count=0
    if request.method=='POST':
        paragraph= request.form['inputpara']
        count=model1.wordCount(paragraph)
        x=model1.sentCount(paragraph)
        para=open("paragraph.txt",'w')
        para.write(paragraph)
        para.close()
        summary=model1.generate_summary("paragraph.txt",min(int(0.5*x),4))
        

        
        return render_template('index.html', para=summary,count=count)

    else:

        return  render_template('index.html', para=paragraph,count=count)

if __name__=='__main__':
    app.run(debug=True)