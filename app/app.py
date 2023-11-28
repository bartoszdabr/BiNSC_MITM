from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        return f'{username} successfully logged'
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=80)
