from flask import Flask, render_template, request
import os
import cx_Oracle


db_user = os.environ.get('DBAAS_USER_NAME', 'system')
db_password = os.environ.get('DBAAS_USER_PASSWORD', 'ur_password')
db_connect = os.environ.get('DBAAS_DEFAULT_CONNECT_DESCRIPTOR', "localhost:1521/orcl")
service_port = port=os.environ.get('PORT', '8080')



app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']
        connection = cx_Oracle.connect(db_user, db_password, db_connect)
        cur = connection.cursor()
        cur.execute('INSERT INTO MyUsers (firstName,lastName) VALUES (\'' + str(firstName) + '\',\'' + str(lastName)+'\')')
        connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)

