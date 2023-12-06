from flask import Flask, render_template,  request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/resume', methods=['GET', 'POST'])
def resume():
    if request.method == 'POST':
        objective = request.form['objective']
        academic=[]
        i=0
        while True:
            try:
                course = request.form['course['+str(i)+']']
                university = request.form['university['+str(i)+']']
                result = request.form['result['+str(i)+']']
                passout = request.form['passout['+str(i)+']']
                academic.append([course, university, result,  passout])
                i += 1
            except Exception as e:
                print(str(e))
                break    
        summury = [] 
        j=0
        while True:
            try:
                sm = request.form['summury['+str(j)+']']
                summury.append(sm)
                j += 1
            except Exception as e:
                print(str(e))
                break
        
        skill = request.form['skill']
        tool = request.form['tool']
        db = request.form['db']
        sos = request.form['sos']
        title = request.form['title']
        srvr = request.form['srvr']
        pos = request.form['pos']
        team = request.form['team']
        tech = request.form['tech']
        desp = request.form['desp']
       
        activities = [] 
        k=0
        while True:
            try:
                ac = request.form['activities['+str(k)+']']
                activities.append(ac)
                k += 1
            except Exception as e:
                print(str(e))
                break
        
        strength = [] 
        l=0
        while True:
            try:
                st = request.form['strength['+str(l)+']']
                strength.append(st)
                l += 1
            except Exception as e:
                print(str(e))
                break

        fname = request.form['fname']
        lname = request.form['lname']
        fullname = fname+' '+lname
        bday = request.form['bday']
        gender = request.form['gender']
        pnum = request.form['pnum']
        gid = request.form['gid']
        caddress = request.form['caddress']
        paddress = request.form['paddress']
        languages = request.form['languages']
        marital = request.form['marital']
        declaration = request.form['declaration']
        
        print(objective, declaration,marital,languages,paddress
        ,caddress,gid,pnum,gender,bday,fullname,lname,fname,strength,
        activities,desp,tech,team,pos,srvr,title,sos,db,tool,skill,summury,academic)


        return render_template('resume.html', objective=objective, declaration=declaration,marital=marital,languages=languages,paddress=paddress
        ,caddress=caddress,gid=gid,pnum=pnum,gender=gender,bday=bday,fullname=fullname,lname=lname,fname=fname,strength=strength,
        activities=activities,desp=desp,tech=tech,team=team,pos=pos,srvr=srvr,title=title,sos=sos,db=db,tool=tool,skill=skill,summury=summury,academic=academic )
    
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)