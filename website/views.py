from itertools import count
from turtle import end_fill
from unicodedata import decimal
from flask import Blueprint, render_template, request, flash, jsonify, redirect,url_for
from flask_login import login_required, current_user
from .models import Note, User, Mthlysalaryrecord
from sqlalchemy import sql, true
from . import db
import json
import math
import sqlite3
from datetime import datetime,date
from calendar import monthrange

views = Blueprint('views', __name__)
auth = Blueprint('auth', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/view_record', methods=['GET', 'POST'])
@login_required
def view_record():

    dbprojectlist = []
    currentproject = []
    totalrow=[]
    totalcost = 0
    
    dbprojectlist = readdbProjectList()
    
    if request.method == 'POST':

        # this page will only display salary record for 1 previous mth for each project
        # therefore 1st thing is to get to know whats the previous mth inorder to filter
        
        previousmth = readPreviousSalaryMth()                
        projectname = request.form.get('searchprojectdropdown')   
        if projectname == "Select project title here":
            flash('Select a project to search', category='error') 

        totalrow = readWorkerRec(previousmth,projectname)
             
        for i in totalrow:
            totalcost = totalcost + i[3]
         
    return render_template("view_record.html", user=current_user,currentproject=currentproject,totalrow=totalrow,dbprojectlist=dbprojectlist,totalcost=totalcost)
   # return render_template("view_record.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()

    return jsonify({})

@views.route('/input_salary', methods=['GET', 'POST'])
def input_salary():
    
    #start - this part is to get workers name,salary date, project title from db and put into each html dropdown box
    dbworkernamelist = []
    dbworkernamelist = readdbWorkerName()

    dbprojectlist = []
    dbprojectlist = readdbProjectList()

    salarydateforcurrentyearonly =[]
    salarydateforcurrentyearonly = readSalaryYear()
    #end - this part is to get workers name,salary date, project title from db and put into each html dropdown box

    if request.method == 'POST':
        
        wname = request.form.get('wname')        
        salarydate = request.form.get('salarydate')        
        projectlocation = request.form.get('projectlocation')

        #start - validation to create new record. if record exist, will not add to new
        dbrecordcount = checkIfRecordExist(wname,salarydate,projectlocation)
        
        if(dbrecordcount==0):
            #end - validation to create new record. if record exist, will not add to new
            if request.form.get('d1') == "":
                d1 = 0
            else :
                d1 = int(request.form.get('d1'))
            
            if request.form.get('d2') == "":
                d2 = 0
            else :
                d2 = int(request.form.get('d2'))
                                   
            if request.form.get('d3') == "":
                d3 = 0
            else :
                d3 = int(request.form.get('d3'))

            if request.form.get('d4') == "":
                d4 = 0
            else :
                d4 = int(request.form.get('d4'))
            
            if request.form.get('d5') == "":
                d5 = 0
            else :
                d5 = int(request.form.get('d5'))
            
            if request.form.get('d6') == "":
                d6 = 0
            else :
                d6 = int(request.form.get('d6'))
            
            if request.form.get('d7') == "":
                d7 = 0
            else :
                d7 = int(request.form.get('d7'))
            
            if request.form.get('d8') == "":
                d8 = 0
            else :
                d8 = int(request.form.get('d8'))

            if request.form.get('d9') == "":
                d9 = 0
            else :
                d9 = int(request.form.get('d9'))
            
            if request.form.get('d10') == "":
                d10 = 0
            else :
                d10 = int(request.form.get('d10'))
            
            if request.form.get('d11') == "":
                d11 = 0
            else :
                d11 = int(request.form.get('d11'))
            
            if request.form.get('d12') == "":
                d12 = 0
            else :
                d12 = int(request.form.get('d12'))
                                   
            if request.form.get('d13') == "":
                d13 = 0
            else :
                d13 = int(request.form.get('d13'))

            if request.form.get('d14') == "":
                d14 = 0
            else :
                d14 = int(request.form.get('d14'))
            
            if request.form.get('d15') == "":
                d15 = 0
            else :
                d15 = int(request.form.get('d15'))
            
            if request.form.get('d16') == "":
                d16 = 0
            else :
                d16 = int(request.form.get('d16'))
            
            if request.form.get('d17') == "":
                d17 = 0
            else :
                d17 = int(request.form.get('d17'))
            
            if request.form.get('d18') == "":
                d18 = 0
            else :
                d18 = int(request.form.get('d18'))

            if request.form.get('d19') == "":
                d19 = 0
            else :
                d19 = int(request.form.get('d19'))
            
            if request.form.get('d20') == "":
                d20 = 0
            else :
                d20 = int(request.form.get('d20'))

            if request.form.get('d21') == "":
                d21 = 0
            else :
                d21 = int(request.form.get('d21'))
            
            if request.form.get('d22') == "":
                d22 = 0
            else :
                d22 = int(request.form.get('d22'))
                                   
            if request.form.get('d23') == "":
                d23 = 0
            else :
                d23 = int(request.form.get('d23'))

            if request.form.get('d24') == "":
                d24 = 0
            else :
                d24 = int(request.form.get('d24'))
            
            if request.form.get('d25') == "":
                d25 = 0
            else :
                d25 = int(request.form.get('d25'))
            
            if request.form.get('d26') == "":
                d26 = 0
            else :
                d26 = int(request.form.get('d26'))
            
            if request.form.get('d27') == "":
                d27 = 0
            else :
                d27 = int(request.form.get('d27'))
            
            if request.form.get('d28') == "":
                d28 = 0
            else :
                d28 = int(request.form.get('d28'))

            if request.form.get('d29') == "":
                d29 = 0
            else :
                d29 = int(request.form.get('d29'))
            
            if request.form.get('d30') == "":
                d30 = 0
            else :
                d30 = int(request.form.get('d30'))
            
            if request.form.get('d31') == "":
                d31 = 0
            else :
                d31 = int(request.form.get('d31'))

            
            #start - to validate d29,d30,d31 whethere exist on current month
            todays_date = date.today()  
            currentyear = todays_date.year  
            currentmonth = todays_date.month  
            #currentmonth = 2                       
            currentmonthtotaldays = monthrange(currentyear, currentmonth)[1]
            
            if 31 > currentmonthtotaldays:
                d31 = 0
            if 30 > currentmonthtotaldays:
                d30 = 0
            if 29 > currentmonthtotaldays:
                d29 = 0
            #end - to validate d29,d30,d31 whethere exist on current month       

            dayrate = request.form.get('dayrate')

            if dayrate =="":
                dayrate = 0
            totalhr = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12+d13+d14+d15+d16+d17+d18+d19+d20+d21+d22+d23+d24+d25+d26+d27+d28+d29+d30+d31
            hrrate = float(dayrate)/8
            totalcost = math.floor(int(totalhr) * float(hrrate))
            print("totalhr =" + str(totalhr))
            print("hrrate =" + str(hrrate))
            print("totalcost =" + str(totalcost))
            print("salarydate = " + str(salarydate))
            print("wname = " + str(wname))
            print("projectlocation =" +str(projectlocation))           
            
            new_salaryrecord= Mthlysalaryrecord(wname=wname.upper(), salarydate=salarydate, projectlocation=projectlocation.upper(), d1=d1,d2=d2,d3=d3,d4=d4,d5=d5,d6=d6,d7=d7,d8=d8,d9=d9,
            d10=d10,d11=d11,d12=d12,d13=d13,d14=d14,d15=d15,d16=d16,d17=d17,d18=d18,d19=d19,d20=d20,d21=d21,d22=d22,d23=d23,d24=d24,d25=d25,d26=d26,
            d27=d27,d28=d28,d29=d29,d30=d30,d31=d31,dayrate=dayrate,totalhr=totalhr,hrrate=hrrate,totalcost=totalcost)
            db.session.add(new_salaryrecord)
            db.session.commit()           
            flash('Salary Record ' + str(salarydate) + ' created! Worker Name =' + str(wname), category='success')
        else :
            flash('Record already existed!', category='error')   
    return render_template("input_salary.html", user=current_user,dbworkernamelist = dbworkernamelist,dbprojectlist=dbprojectlist,salarydateforcurrentyearonly=salarydateforcurrentyearonly)
 

@views.route('/search_salary', methods=['GET', 'POST'])
def search_salary():
    row = []

    #start - this part is to get workers name,salary date, project title from db and put into each html dropdown box
    dbworkernamelist = []
    dbworkernamelist = readdbWorkerName()

    dbprojectlist = []
    dbprojectlist = readdbProjectList()

    salarydateforcurrentyearonly =[]
    salarydateforcurrentyearonly = readSalaryYear()
    #end - this part is to get workers name,salary date, project title from db and put into each html dropdown box
    
    if request.method == 'POST':
        #is POST method is from search form, togglecontrol will be searchcontrol.
        togglecontrol = request.form.get('searchControl') 
        print("togglecontrol is "  + str(togglecontrol))
        #if togglecontrol is none, saving record
        if togglecontrol is None:

            pkkey = request.form.get('pk')            
            if request.form.get('d1') == "":
                d1 = 0
            else :
                d1 = int(request.form.get('d1'))
            
            if request.form.get('d2') == "":
                d2 = 0
            else :
                d2 = int(request.form.get('d2'))
                                   
            if request.form.get('d3') == "":
                d3 = 0
            else :
                d3 = int(request.form.get('d3'))

            if request.form.get('d4') == "":
                d4 = 0
            else :
                d4 = int(request.form.get('d4'))
            
            if request.form.get('d5') == "":
                d5 = 0
            else :
                d5 = int(request.form.get('d5'))
            
            if request.form.get('d6') == "":
                d6 = 0
            else :
                d6 = int(request.form.get('d6'))
            
            if request.form.get('d7') == "":
                d7 = 0
            else :
                d7 = int(request.form.get('d7'))
            
            if request.form.get('d8') == "":
                d8 = 0
            else :
                d8 = int(request.form.get('d8'))

            if request.form.get('d9') == "":
                d9 = 0
            else :
                d9 = int(request.form.get('d9'))
            
            if request.form.get('d10') == "":
                d10 = 0
            else :
                d10 = int(request.form.get('d10'))
            
            if request.form.get('d11') == "":
                d11 = 0
            else :
                d11 = int(request.form.get('d11'))
            
            if request.form.get('d12') == "":
                d12 = 0
            else :
                d12 = int(request.form.get('d12'))
                                   
            if request.form.get('d13') == "":
                d13 = 0
            else :
                d13 = int(request.form.get('d13'))

            if request.form.get('d14') == "":
                d14 = 0
            else :
                d14 = int(request.form.get('d14'))
            
            if request.form.get('d15') == "":
                d15 = 0
            else :
                d15 = int(request.form.get('d15'))
            
            if request.form.get('d16') == "":
                d16 = 0
            else :
                d16 = int(request.form.get('d16'))
            
            if request.form.get('d17') == "":
                d17 = 0
            else :
                d17 = int(request.form.get('d17'))
            
            if request.form.get('d18') == "":
                d18 = 0
            else :
                d18 = int(request.form.get('d18'))

            if request.form.get('d19') == "":
                d19 = 0
            else :
                d19 = int(request.form.get('d19'))
            
            if request.form.get('d20') == "":
                d20 = 0
            else :
                d20 = int(request.form.get('d20'))

            if request.form.get('d21') == "":
                d21 = 0
            else :
                d21 = int(request.form.get('d21'))
            
            if request.form.get('d22') == "":
                d22 = 0
            else :
                d22 = int(request.form.get('d22'))
                                   
            if request.form.get('d23') == "":
                d23 = 0
            else :
                d23 = int(request.form.get('d23'))

            if request.form.get('d24') == "":
                d24 = 0
            else :
                d24 = int(request.form.get('d24'))
            
            if request.form.get('d25') == "":
                d25 = 0
            else :
                d25 = int(request.form.get('d25'))
            
            if request.form.get('d26') == "":
                d26 = 0
            else :
                d26 = int(request.form.get('d26'))
            
            if request.form.get('d27') == "":
                d27 = 0
            else :
                d27 = int(request.form.get('d27'))
            
            if request.form.get('d28') == "":
                d28 = 0
            else :
                d28 = int(request.form.get('d28'))

            if request.form.get('d29') == "":
                d29 = 0
            else :
                d29 = int(request.form.get('d29'))
            
            if request.form.get('d30') == "":
                d30 = 0
            else :
                d30 = int(request.form.get('d30'))
            
            if request.form.get('d31') == "":
                d31 = 0
            else :
                d31 = int(request.form.get('d31'))

            dayrate = request.form.get('dayrate')
            #start - to retrive salary date and split into 2 string, mth and year for processing to validate d29,d30,d31 whethere exist on current month
            editsalarydate = request.form.get('editsalarydate')
            mthyrsplit = str(editsalarydate).split('-')

            currentyear = mthyrsplit[1]  
            currentmonth = mthyrsplit[0] 
            #currentmonth = 2                       
            currentmonthtotaldays = monthrange(int(currentyear), int(currentmonth))[1]
            
            if 31 > currentmonthtotaldays:
                d31 = 0
            if 30 > currentmonthtotaldays:
                d30 = 0
            if 29 > currentmonthtotaldays:
                d29 = 0
            #end - to retrive salary date and split into 2 string, mth and year for processing to validate d29,d30,d31 whethere exist on current month
            

            if dayrate =="":
                dayrate = 0
            totalhr = d1+d2+d3+d4+d5+d6+d7+d8+d9+d10+d11+d12+d13+d14+d15+d16+d17+d18+d19+d20+d21+d22+d23+d24+d25+d26+d27+d28+d29+d30+d31
            hrrate = float(dayrate)/8
            totalcost = math.floor(int(totalhr) * float(hrrate))
            datecreated = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            
            con = sqlite3.connect("website/database.db")    
            cur = con.cursor()
            sqlquery = "UPDATE Mthlysalaryrecord SET d1 = " + str(d1) + ",d2 = "+ str(d2) +",d3 = "+ str(d3) +",d4 = "+ str(d4)+",d5 = "+ str(d5)+",d6 = "+ str(d6)+",d7 = "+ str(d7)+",d8 = "+ str(d8)+",d9 = "+ str(d9)+",d10 = "+ str(d10)+",d11 = "+ str(d11)+",d12 = "+ str(d12)+",d13 = "+ str(d13)+",d14 = "+ str(d14)+",d15 = "+ str(d15)+",d16 = "+ str(d16)+",d17 = "+ str(d17)+ ",d18 = "+ str(d18)+",d19 = "+ str(d19)+",d20 = "+ str(d20)+",d21 = "+ str(d21)+ ",d22 = "+ str(d22)+",d23 = "+ str(d23)+",d24 = "+ str(d24) +",d25 = "+ str(d25)+",d26 = "+ str(d26)+ ",d27 = "+ str(d27)+ ",d28 = "+ str(d28)+ ",d29 = "+ str(d29)+ ",d30 = "+ str(d30)+ ",d31 = "+ str(d31)+",totalhr =" +str(totalhr)+",dayrate =" +str(dayrate)+",hrrate =" + str(hrrate)+",totalcost =" + str(totalcost)+ ",datecreated = '" + str(datecreated) + "' WHERE id = " + str(pkkey) + ";" 
            print(sqlquery)
            sqlrow = cur.execute(sqlquery)
            con.commit()
            con.close()

            #display search record again after updated table    
            wname = request.form.get('editwname')        
            salarydate = request.form.get('editsalarydate')        
            projectlocation = request.form.get('editprojectlocation')
            print("wname=" + str(wname))
            print("salarydate=" + str(salarydate))
            print("projectlocation=" + str(projectlocation))
            
            if (len(wname) !=0) and (len(salarydate) !=0) and (len(projectlocation) !=0) :
                row = readMthlysalaryrecord(wname,salarydate,projectlocation)
                flash("Edited Record Saved!")

        #is togglecontrol is searchcontrol, perform search only
        else :

            wname = request.form.get('searchwname')        
            salarydate = request.form.get('searchsalarydate')        
            projectlocation = request.form.get('searchprojectlocation')
            
            print("wname =" + str(wname))
            print("salarydate =" + str(salarydate))
            print("projectlocation =" + str(projectlocation))
            if (len(wname) !=0) and (len(salarydate) !=0) and (len(projectlocation) !=0) :                
                row = readMthlysalaryrecord(wname,salarydate,projectlocation)
                if len(row) == 0 :
                    flash("Record not found/Duplicated Records found!",category='error')
                else :
                    flash("Record found!")
            else :
                flash("Record not found! Please try again!",category='error')
        
    return render_template("search_salary.html",user=current_user, row=row,dbworkernamelist=dbworkernamelist,dbprojectlist=dbprojectlist,salarydateforcurrentyearonly=salarydateforcurrentyearonly)           
            
    

def readMthlysalaryrecord(wname,salarydate,projectlocation):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("website/database.db")    
    cur = con.cursor()
    row = []
    querycount = []
    # The result of a "cursor.execute" can be iterated over by row
    sqlquery = "SELECT * FROM Mthlysalaryrecord where wname='" +str(wname) + "' and salarydate='" + str(salarydate) + "' and projectlocation='" + str(projectlocation) + "';"
    sqlqyertcountcheck = "SELECT COUNT(*) FROM Mthlysalaryrecord where wname='" +str(wname) + "' and salarydate='" + str(salarydate) + "' and projectlocation='" + str(projectlocation) + "';"
   
    for querycount in cur.execute(sqlqyertcountcheck):
        print(querycount[0])
    
    if int(querycount[0])== 0:
        row = []
    else:
        for row in cur.execute(sqlquery):
            print(row)
    
    # Be sure to close the connection
    con.close()
    return row

def readdbWorkerName():
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("website/database.db")    
    cur = con.cursor()
    row = []
    querycount = []
    totalrow = []
    # The result of a "cursor.execute" can be iterated over by row
    sqlquery = "SELECT distinct wname FROM Mthlysalaryrecord ORDER BY wname ASC;"
    sqlqyertcountcheck = "SELECT COUNT(wname) FROM Mthlysalaryrecord;"
   
    for querycount in cur.execute(sqlqyertcountcheck):
        print("readdbWorkerName DB Query count found = " + str(querycount[0]))
    
    if int(querycount[0])== 0:
        row = []        
    else:
        for row in cur.execute(sqlquery):            
            totalrow.append(row[0])        

    # Be sure to close the connection
    con.close()
    return totalrow

def readdbProjectList():
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("website/database.db")    
    cur = con.cursor()
    row = []
    querycount = []
    totalrow = []
    # The result of a "cursor.execute" can be iterated over by row
    sqlquery = "SELECT distinct projectlocation FROM Mthlysalaryrecord ORDER BY projectlocation ASC;"
    sqlqyertcountcheck = "SELECT COUNT(projectlocation) FROM Mthlysalaryrecord;"
   
    for querycount in cur.execute(sqlqyertcountcheck):
        print("readdbProjectList DB Query count found = " + str(querycount[0]))
    
    if int(querycount[0])== 0:
        row = []
        
    else:
        for row in cur.execute(sqlquery):
           totalrow.append(row[0])        

    # Be sure to close the connection
    con.close()
    return totalrow

def readSalaryYear():
    #this function is to set available mth and year from last year dec until current mth yr
    totalrow = []
    todays_date = date.today()
    currentyear = todays_date.year  
    currentmonth = todays_date.month  
    #currentmonth = 12
    
    #start - this line is to add 1 month of previous year if it is january
    totalrow.append(str("12") + "-" + str(currentyear-1))
    #end - this line is to add 1 month of previous year if it is january

    mth = 1
    while mth <= currentmonth:
        totalrow.append(str(mth) + "-" + str(currentyear))
        mth +=1
    
    return totalrow

def readSalaryList():
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("website/database.db")    
    cur = con.cursor()
    row = []
    querycount = []
    totalrow = []
    # The result of a "cursor.execute" can be iterated over by row
    sqlquery = "SELECT distinct projectlocation FROM Mthlysalaryrecord ORDER BY projectlocation ASC;"
    sqlqyertcountcheck = "SELECT COUNT(projectlocation) FROM Mthlysalaryrecord;"
   
    for querycount in cur.execute(sqlqyertcountcheck):
        print("readdbProjectList DB Query count found = " + str(querycount[0]))
    
    if int(querycount[0])== 0:
        row = []
        
    else:
        for row in cur.execute(sqlquery):
           totalrow.append(row[0])        

    # Be sure to close the connection
    con.close()
    return totalrow

def readPreviousSalaryMth():
    #this function is to set available mth to only previous mth and current mth
    totalrow = ""    
    todays_date = date.today()
    currentmonth = todays_date.month 
    currentyear = todays_date.year
    
    if currentmonth == 1:
        previousmonth = 12
        previousyear = currentyear - 1
    else:
        previousmonth = currentmonth - 1
        previousyear = currentyear
        
    totalrow = (str(previousmonth) + "-" + str(previousyear))
    return totalrow
    
def readDistinctProject(previousmth):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("website/database.db")    
    cur = con.cursor()
    row = []
    totalrow = []
    # The result of a "cursor.execute" can be iterated over by row
    sqlquery = "SELECT distinct projectlocation FROM Mthlysalaryrecord WHERE salarydate =\'" + str(previousmth) + "\' ORDER BY projectlocation;"
      
    for row in cur.execute(sqlquery):
        totalrow.append(row[0])        

    # Be sure to close the connection
    con.close()
    return totalrow

def readWorkerRec(previousmth,projecttitle):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("website/database.db")    
    cur = con.cursor()
    row = []
    
    totalrow = []
    # The result of a "cursor.execute" can be iterated over by row
    sqlquery = "SELECT projectlocation,salarydate,wname,totalcost from Mthlysalaryrecord where salarydate =\'" + str(previousmth) + "\' and projectlocation = \'" + str(projecttitle) + "' ORDER BY wname;"
      
    for row in cur.execute(sqlquery):
        totalrow.append(row)        

    # Be sure to close the connection
    con.close()
    return totalrow

def checkIfRecordExist(wname,salarydate,projectlocation):
    # Create a SQL connection to our SQLite database
    con = sqlite3.connect("website/database.db")    
    cur = con.cursor()
    totalrow = 1 
    # The result of a "cursor.execute" can be iterated over by row
    sqlquery = "SELECT COUNT(*) from Mthlysalaryrecord where wname= \'" + str(wname) + "\'and salarydate =\'" + str(salarydate) + "\' and projectlocation = \'" + str(projectlocation) + "';"
      
    for querycount in cur.execute(sqlquery):
        print("querycount = " + str(querycount[0]))
    
    if int(querycount[0])== 0:
        totalrow=0

    # Be sure to close the connection
    con.close()
    return totalrow
    