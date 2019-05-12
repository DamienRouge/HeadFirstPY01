from flask import Flask,render_template,request,redirect

webapp = Flask(__name__)

@webapp.route('/')
def entry_page() ->'html':
    return render_template('entry.html',the_title='test Azure')

if __name__ == "__main__":
    webapp.run(debug=True)