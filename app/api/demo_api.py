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
    min = dict(value=100, text="(ms)")
    max = dict(value=500, text="(ms)")
    latency = dict(item=325, min=min, max=max)
    return jsonify(latency)


@api.route('/api/get_locations', methods=['GET'])
def get_locations():
    london = dict(city_name="London", country_code="GB")
    glasgow = dict(city_name="Glasgow", country_code="GB")
    sydney = dict(city_name="Sydney", country_code="AU")
    new_york = dict(city_name="New York", country_code="US")
    cape_town = dict(city_name="Cape Town", country_code="ZA")

    point1 = dict(city=london, size=10)
    point2 = dict(city=sydney, size=5)
    point3 = dict(city=glasgow, size=5)
    point4 = dict(city=new_york, size=10)
    point5 = dict(city=cape_town, size=10)

    point_list = [point1, point2, point3, point4, point5]
    points = dict(point=point_list)

    return jsonify(points=points)


