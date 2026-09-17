from flask import Flask

application = Flask(__name__)

@application.route("/")
def index():
    return "Hello from 5bf61784 Elastic Beanstalk CI-CD"
