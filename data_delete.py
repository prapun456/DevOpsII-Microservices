from flask import Flask, request, jsonify
import datetime
# pip install Flask-JWT
# import jwt
import data_item as us

app = Flask(__name__)

# username = us.user_name()

# Find data in json

@app.route('/delete', methods=['DELETE'])
def delete():
    name = request.form.get('name')
    # return jsonify(user)
    _user = us.find_itemname(name)
    data = [x for x in _user if x["name"]==name]
    if data:
        us.item_delete(name)
        return jsonify({'message': 'Delete successfully.'}), 200
    else:
        return jsonify({'message': 'Cannot delete user.'}), 401



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003, debug=True) #127.0.0.1