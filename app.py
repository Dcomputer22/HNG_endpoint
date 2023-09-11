from flask import Flask, jsonify, request
from datetime import datetime

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def my_endpoint():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.now().strftime('%A')
    utc_now = datetime.utcnow()
    utc_time = utc_now.strftime("%Y-%m-%dT%H:%M:%SZ")

    return jsonify({
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": "https://github.com/Dcomputer22/HNG_endpoint/blob/master/app.py",
        "github_repo_url": "https://github.com/Dcomputer22/HNG_endpoint",
        "status_code": 200
    })


if __name__ == 'main':
    app.run()

