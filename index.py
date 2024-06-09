from flask import Flask, render_template, request, jsonify
from flask_mail import Mail, Message
import random
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Rowdy_Code'  # Change this to a random string
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'rowdy.man900@gmail.com'  # Enter your Gmail email here
app.config['MAIL_PASSWORD'] = 'dfdy uxen smxh cejc'  # Enter your Gmail password here

mail = Mail(app)

def generate_otp():
    digits = string.digits
    otp = ''.join(random.choice(digits) for i in range(6))
    return otp

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_otp', methods=['POST'])
def send_otp():
    email = request.form['email']
    otp = generate_otp()

    msg = Message('OTP Verification', sender='rowdy.man900@gmail.com', recipients=[email])
    msg.body = f'Your OTP for verification is: {otp}'

    try:
        mail.send(msg)
        return jsonify({'status': 'success', 'otp': otp})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
