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

@api.route('/api/get_locations', methods=['GET'])
def get_locations():
    london = dict(city_name="London", country_code="UK")
    glasgow = dict(city_name="Glasgow", country_code="UK")
    sydney = dict(city_name="Sydney", country_code="AU")
    new_york = dict(city_name="New York", country_code="US")
    cape_town = dict(city_name="Cape Town", country_code="ZA")

    point1 = dict(london, size=10)
    point2 = dict(sydney, size=5)

    point_list = [point1, point2]
    points = dict(point=point_list)


    return jsonify(points=points)


