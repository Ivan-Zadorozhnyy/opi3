from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for demonstration purposes
historical_data = {
    "2023-27-09-20:00": 34,
    "2023-27-09-21:00": 30,
}

user_data = {
    "A4DC2287-B03D-430C-92E8-02216D828709": {
        "2023-27-09-20:00": False,
        "nearestOnlineTime": "2023-28-09-15:00"
    }
}


@app.route('/api/stats/users', methods=['GET'])
def get_users_stats():
    date = request.args.get('date')
    return jsonify({"usersOnline": historical_data.get(date, None)})


@app.route('/api/stats/user', methods=['GET'])
def get_user_stats():
    date = request.args.get('date')
    user_id = request.args.get('userId')

    if user_id not in user_data:
        return jsonify({"error": "Invalid userId"}), 404

    user_info = user_data[user_id]
    was_online = user_info.get(date, None)
    nearest_online_time = None if was_online else user_info.get('nearestOnlineTime', None)

    return jsonify({
        "wasUserOnline": was_online,
        "nearestOnlineTime": nearest_online_time
    })


@app.route('/api/predictions/users', methods=['GET'])
def predict_users_online():
    # Placeholder for prediction logic
    return jsonify({"onlineUsers": 31})


@app.route('/api/predictions/user', methods=['GET'])
def predict_user_online():
    date = request.args.get('date')
    tolerance = float(request.args.get('tolerance'))
    user_id = request.args.get('userId')

    # Placeholder for prediction logic
    chance = 0.81
    will_be_online = chance > tolerance

    return jsonify({
        "willBeOnline": will_be_online,
        "onlineChance": chance
    })


if __name__ == '__main__':
    app.run(debug=True)
