from flask import Flask, render_template, request, redirect,session
app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe'
# our index route will handle rendering our form
@app.route('/')
def index():
    if 'site_accessed' not in session:
        session['site_accessed'] =0
    else:
        session['site_accessed'] +=1
    if 'actual_visits' not in session:
        session['actual_visits'] =0
    else:
        session['actual_visits'] +=1

    return render_template("index.html")

@app.route('/destroy_session')
def destroy_sess():
    session.clear()
    return redirect('/')

@app.route('/add_two')
def add_two():
    session['site_accessed'] +=1
    return redirect('/')

@app.route('/increase_counter',methods = ['POST'])
def increase_counter():
    session['site_accessed'] +=int(request.form['incrament'])-1
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)