from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/getURL', methods=['POST'])
def getURL():
    url = request.form['url']
    
    # Perform your Phishing Website Detection logic
    # Example implementation:
    if 'phishing' in url.lower():
        error = 'Phishing'
    else:
        error = 'Legitimate'
    
    return render_template('home.html', url=url, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)