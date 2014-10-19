from flask import g
from flask import Flask
from flask import render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def table():
     
    return '''
<!DOTYPE html>
<html>
<head>
    <title> WEBPAGE </title>
</head>
<body>
<a href="http://127.0.0.1:5000/edit">insert content</a>
<a href="http://127.0.0.1:5000/view">view table</a>
</body>
</html>
'''
@app.route('/view')
def view():
	db=sqlite3.connect('table.db')
	cursor = db.execute("SELECT * FROM box")
	rows=[]
	for row in cursor:
   		rows.append(row)

	print "Operation done successfully";
	db.close()
	return '''
<!DOCTYPE html>
<html>
<body>

<table style="width:100%">
  <tr>
    <td>'''rows[0][1]'''</td>
    <td>'''rows[0][1]'''</td>		
    <td>'''rows[0][2]'''</td>
  </tr>
  <tr>
    <td>'''rows[1][0]'''</td>
    <td>'''rows[1][1]'''</td>		
    <td>'''rows[1][2]'''</td>
  </tr>
</table>

</body>
</html>

	
	
  


if __name__=='__main__':
   app.run(debug=True)
