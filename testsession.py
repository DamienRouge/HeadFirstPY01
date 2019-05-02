from flask import Flask, session
from checker import check_logged_in

app_TestSession = Flask(__name__)
#session['logged_in']=False
app_TestSession.secret_key = "mysecretkeyismysecretkey"

@app_TestSession.route('/')
def entry_page()->str:
    return "This is the entry page"

@app_TestSession.route('/page1')
@check_logged_in
def page1()->str:
    return "This is page1"

@app_TestSession.route('/page2')
@check_logged_in
def page2()->str:
    return "this is page2"

@app_TestSession.route('/page3')
@check_logged_in
def page3()->str:
    return "this is page3"

@app_TestSession.route('/login')
def do_Login()->str:
    session['logged_in']=True
    return "You are logged in."

@app_TestSession.route('/logout')
@check_logged_in
def do_logout():
    session.pop('logged_in')
    return 'something' #You will still have to retun something
    #as logged_in may actually exist
    #then we need to pull the actual do_logout function.
    #if not, then we just need to return it does not exist

    #return "you have now logged out"
    # if 'logged_in' in session:
    #     session.pop('logged_in')
    #     return "you have now logged out"
    # return 'you are current not logged in'

# @app_TestSession.route('/status')
# def check_status()->str:
#     if 'logged_in' in session:
#         return "You current status is logged in"
#     return "You have not yet logged in"


if __name__ == "__main__":
    app_TestSession.run(debug = True)
