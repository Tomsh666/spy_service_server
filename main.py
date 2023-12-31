from flask import Flask, request

app = Flask(__name__)

@app.route('/sms_data', methods=['GET'])
def sms_data():
    sender = request.args.get('sender')
    message_body = request.args.get('message_body')
    date = request.args.get('date')
    print(sender, message_body, date)
    return 'success'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
