from flask import Flask,render_template, request,redirect,escape
from search4v import search4vowels,search4letters
#from mysql import connector
from DBcm import UseDatabase


app = Flask(__name__)
app.config['dbconfig'] = {'host':'127.0.0.1','user':'vsearch','password':'vsearchpassword','database':'vsearchlogDB'}
'''@app.route('/')
def Hello()-> str:
    return 'Hello Web App World''' # We may now redirects with return of 302

'''def Hello()-> '302':
    @app.route('/')
    return redirect ('/entry')''' #Or, we can have two url relates to one function as below on entry.

def log_request(req:"flask request", res: str)->None:
    # with open('versearch.log','a') as logstream:
    #     print(req.form, req.remote_addr, req.user_agent,res, file = logstream,sep = '|')
    # dbconfig = {'host':'127.0.0.1','user':'vsearch','password':'vsearchpassword','database':'vsearchlogDB'}
    # import mysql.connector
    # conn = mysql.connector.connect(**dbconfig)
    # cursor = conn.cursor()
    # insert_stmt = """ INSERT INTO log (phrase,letters, ip,browser_string, results) VALUES (%s,%s,%s,%s,%s)"""
    # cursor.execute(insert_stmt,(req.form['phrase'],req.form['letters'],req.remote_addr, req.user_agent.browser,res))#.browser, new stuff
    # #we can only extract browser, no longer user_agent
    # conn.commit()
    # # select_stmt = """SELECT * FROM log"""
    # # cursor.execute(select_stmt)
    # # for row in cursor.fetchall():
    # #     print(row)
    # cursor.close()
    # conn.close()
    #req.form is apparently one of the parameter in the form of a dictrionary.
    with UseDatabase(app.config['dbconfig']) as cursor:
        insert_stmt = """ INSERT INTO log (phrase,letters, ip,browser_string, results) VALUES (%s,%s,%s,%s,%s)"""
        cursor.execute(insert_stmt,(req.form['phrase'],req.form['letters'],req.remote_addr, req.user_agent.browser,res))#.browser, new stuff






@app.route('/search4', methods = ['GET','POST'])
def do_search()->str:
    phrase=request.form['phrase'] # Request automatically inherit due to http or html
    letters=request.form['letters']
    #return ''.join(list(search4letters(phrase,letters)))
    result = ''.join(list(search4letters(phrase,letters)))
    title = "YO what's up, this is your results"
    log_request(request, result)
    return render_template('results.html', the_title = title, the_phrase = phrase, the_letters = letters, the_results = result)

@app.route('/')
@app.route('/entry')
def entry_page() ->'html':
    return render_template('entry.html', the_title = "Welcome 2 search4letters")

@app.route('/viewlog')
def view_log()-> 'html':
    lines = []
    with open('versearch.log') as logstream:
        for line in logstream:
            lines.append([])
            for item in line.split('|'):
                lines[-1].append(escape(item))
        titles = ('Form Data', 'Remote_addr','User_Agent','Result')
        return render_template('viewlog.html', the_title = 'View Log', the_row_titles = titles, the_data = lines)
        #return str(lines)
    #     lines=[]
    #     for line in logstream:
    #         lines.append((escape(line)).split('|'))
    # return str(lines)

if(__name__=='__main__'):
    app.run(debug = True)
