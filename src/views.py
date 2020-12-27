from flask import jsonify, request
from src import app
from src.mutation_schema import MutationSchema
from src.request_schema import RequestSchema
from src.utils import validate_json, index_to_es, mutation_pattern_to_query, request_pattern_to_query, send_query


# ----------------- Send from Maleware-Analyser ---------------- #

@app.route('/send_pattern', methods=['POST'])
def recipient_of_pattern():
    json_data = request.json

    if "mutationMonitoring" in json_data:
        if validate_json(json_data["mutationMonitoring"], MutationSchema):
            if index_to_es(json_data["mutationMonitoring"], "mutationMonitoring"):
                return jsonify({"status": "succeeded"}), 200
            return jsonify({"status": "failed"}), 500
        else:
            return jsonify({"error": "Invalid Mutation Monitoring pattern"}), 400

    elif "monitoringRequests" in json_data:
        if validate_json(json_data["monitoringRequests"], RequestSchema):
            if index_to_es(json_data["monitoringRequests"], "monitoringRequests"):
                return jsonify({"status": "succeeded"}), 200
            return jsonify({"status": "failed"}), 500
        else:
            return jsonify({"error": "Invalid Monitoring Request pattern"}), 400


# ---------------------- Send from Dobiel ---------------------- #

@app.route('/send_request', methods=['POST'])
def recipient_of_request():
    json_data = request.json
    is_valid = validate_json(json_data, RequestSchema)

    if is_valid:
        return jsonify({"status": "succeeded"}), 200
    else:
        return jsonify({"error": "Given mutation has invalid syntax"}), 400


@app.route('/send_mutation', methods=['POST'])
def recipient_of_mutation():
    json_data = request.json
    is_valid = validate_json(json_data, MutationSchema)

    if is_valid:
        # if "type" in json_data:
        #     if "childNodeMutation" in json_data["type"]:
        #         if "addedNode" in json_data["type"]["childNodeMutation"]:
        #             if "nodeName" in json_data["type"]["childNodeMutation"]["addedNode"]:
        #                 if json_data["type"]["childNodeMutation"]["addedNode"]["nodeName"] == "iframe":
        #                     print("----> ", __import__("json").dumps(mutation_pattern_to_query(json_data)))
        #                     send_query(mutation_pattern_to_query(json_data), "mutationMonitoring")
        s, r = send_query(mutation_pattern_to_query(json_data), "mutationMonitoring")
        if s:
            return jsonify(r), 200
        else:
            return jsonify({"status": "failed"}), 500
    else:
        return jsonify({"error": "Given mutation has invalid syntax"}), 400
