from flask import Flask, jsonify, abort, make_response, request, url_for
from slacker import Slacker
from datetime import datetime


# Sending a notification to Slack
def Push(message):
    # Replace with your Slack token
    slack_token = "xoxp-000000000000-000000000000-000000000000-00000000000000000000000000000000"
    slack_channel = "#vrops"
    slack_msg = message
    slack = Slacker(slack_token)
    
    # Send Push Notification
    slack.chat.post_message(slack_channel, slack_msg, 'slackbot') 
    return jsonify({'Status':'Push Notification sent'}), 201


app = Flask(__name__)

@app.route('/<RequestID>', methods=['POST'])
def create_reading3(RequestID):
    if not request.json or 'Done' in request.json == True:
        abort(400) 
        
    reading=request.json
    
    for key in reading.keys():
        print('key: {}\n###\n{}'.format(key, reading[key]))

    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    message = dt_string + '\n' + str(reading['type']) + ':\nObject Type : ' \
    + str(reading['resourceKind']) + '\n' + str(reading['resourceName']) \
    + '\n' + str(reading['alertName'])+ '\nAlert Status : ' \
    + str(reading['status']) + '\n' + 20*'#' + '\n'
    
    Push(message)
    
    pass
            
    return jsonify(reading, 201)
    
        
@app.route('/<RequestID>', methods=['PUT'])
def create_reading4(RequestID):
    if not request.json or 'Done' in request.json == True:
        abort(400)
        
    reading=request.json
    
    for key in reading.keys():
        print('key: {}\n###\n{}'.format(key, reading[key]))
        
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    message = dt_string + '\n' + str(reading['type']) + ':\nObject Type : ' \
    + str(reading['resourceKind']) + '\n' + str(reading['resourceName']) \
    + '\n' + str(reading['alertName'])+ '\nAlert Status : ' \
    + str(reading['status']) + '\n' + 20*'#' + '\n'
    
    Push(message)
    
    pass
            
    return jsonify(reading, 201)
         

@app.route('/test', methods=['POST'])

def create_reading1():
    if not request.json or 'Done' in request.json == True:
        abort(400) 
    reading=request.json
    print(type(reading))
    print(reading.keys())
    print(reading['impact'])
    
            
    return jsonify(reading, 201)
    
@app.route('/test', methods=['PUT'])
def create_reading2():
    if not request.json or 'Done' in request.json == True:
        abort(400)             
    return jsonify('PUT method is also working', 201)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def syntax(error):
    return make_response(jsonify({'error': 'The request could not be understood by the server due to malformed syntax.'}), 400)

@app.errorhandler(500)
def internal(error):
    return make_response(jsonify({'error': 'Internal Server Error'}), 500)  


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001   , debug=False)
