from flask import Flask, redirect

app = Flask(__name__)

# Redirect route
@app.route('/')
def home():
    # Redirect to the desired URL
    return redirect('https://www.google.com', code=302)

if __name__ == '__main__':
    app.run(debug=True)
