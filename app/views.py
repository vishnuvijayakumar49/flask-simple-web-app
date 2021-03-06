from flask import render_template, flash, request,url_for,redirect,flash
from app import app
import sqlite3

@app.route('/')
def table():
     
    return render_template('table.html')

@app.route('/view',methods=['GET' ,'POST'])
def view():
   if request.method =='GET':
	db=sqlite3.connect('table.db')
	cursor = db.execute("SELECT * FROM box")
	rows=[]
	for row in cursor:
   		rows.append(row)
	
	db.close()
	return render_template('view.html',
                               rows=rows)
   else:
        if request.form['delete'] != '':
		db=sqlite3.connect('table.db')
		
		db.execute("DELETE FROM box \
			    WHERE PERSON =(?)",  ((request.form['delete'],)))
		db.commit()
		db.close()
		return redirect('/view')
	elif request.form['search'] !='':
		db=sqlite3.connect('table.db')
		
		a=db.execute("SELECT * FROM box WHERE PERSON=(?)",((request.form['search'],)))
		rows=[]
		for row in a:
			rows.append(row)
		db.close()
		return render_template('search.html',rows=rows)
	return redirect('/view')	



@app.route('/edit' , methods=['GET', 'POST'])
def edit():
	if request.method == 'POST':
        	db=sqlite3.connect('table.db')
		db.execute('''INSERT INTO box VALUES(?,?,?) ''',
		(request.form['no'], request.form['name'] ,request.form['age']));
		db.commit()
		db.close()
		return redirect('/view')
	return render_template('edit.html')


