import json
from . import api
from flask import request, g, jsonify, Response, current_app


@api.route('/api/uptime', methods=['GET'])
def get_uptime():
    uptime = dict(status="Up", downTime="9 days", responseTime="500 ms")
    return jsonify(uptime)


