import flask

@app.route('/api/get_messages', methods = ['POST'])
def get_messages():
    json = request.get_json()
    if json['user'] == "larry":
        return jsonify({'messages':['test1', 'test2']})
    return jsonify({'error':'no user found'})