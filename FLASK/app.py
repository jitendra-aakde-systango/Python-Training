from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

# Route to render the form
@app.route('/')
def welcome():
    return render_template('submit.html')
@app.route('/')
def result():
    return render_template('result.html')

@app.route('/success/<int:score>')
def success(score):
    return f"Student passed with marks: {score}"

@app.route('/fail/<int:score>')
def fail(score):
    return f"Student failed with marks: {score}"

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    if request.method == "POST":
        m1 = float(request.form['m1'])
        m2 = float(request.form['m2'])
        m3 = float(request.form['m3'])

        total_score = (m1 + m2 + m3) / 3  # Average score
        res=''
        if total_score < 50:
            res="fail"
        else:
            res='pass'

        exp={'score':int(total_score), 'status':res}
    return render_template('result.html', result=exp)
if __name__ == "__main__":
    app.run(debug=True)
