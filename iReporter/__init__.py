from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'a25a89a56f653a13deb01aa2368cab8c'


from iReporter import routes