import json
from . import api
from flask import request, g, jsonify, Response, current_app


@api.route('/api/uptime', methods=['GET'])
def get_uptime():
    uptime = dict(status="Up", downTime="9 days", responseTime="500 ms")
    return jsonify(uptime)

@api.route('/api/revenue', methods=['GET'])
def get_revenue():
    revenue = dict(text="Revenue Last 24 hours", value=4532, prefix="£")
    item = [revenue]
    return jsonify(item=item)

@api.route('/api/latency', methods=['GET'])
def get_latency():
    min = dict(value=100, text="Min Latency (ms)")
    max = dict(value=500, text="Max Latency (ms)")
    latency= dict(item=325, min=min, max=max)
    return jsonify(latency)


