from jsonschema import validate, exceptions
from src import app


def validate_json(_json_data, _schema):
    try:
        validate(instance=_json_data, schema=_schema)
    except exceptions.ValidationError:
        return False
    return True


def index_to_es(pattern, document):
    es = app.config['ES_SERVER']

    if document == "mutationMonitoring":
        try:
            r = es.index(index="dobiel_mutation_monitoring", doc_type="_doc", body=pattern, request_timeout=20)
            if r["result"]:
                return True
        except Exception as e:
            print(str(e))

    elif document == "monitoringRequests":
        try:
            r = es.index(index="dobiel_monitoring_requests", doc_type="_doc", body=pattern, request_timeout=20)
            if r["result"]:
                return True
        except Exception as e:
            print(str(e))

    return False


def mutation_pattern_to_query(_pattern):
    query = {
        "_source": "description",
        "query": {
            "bool": {
                "must": list()
            }
        }
    }

    main = query["query"]["bool"]["must"]

    # ------------------------------------------------- 'target'
    if "target" in _pattern:
        if "nodeName" in _pattern["target"]:
            main.append(
                {
                    "match": {
                        "target.nodeName": "({}) OR (ALL)".format(_pattern["target"]["nodeName"]) if _pattern["target"]["nodeName"] != "" else "ALL"
                    }
                }
            )

        if "attributes" in _pattern["target"]:
            bool_should = {
                "bool": {
                    "should": [
                        {
                            "match": {"target.attributes.__check": False}
                        }
                    ]
                }
            }
            for k, _ in _pattern["target"]["attributes"].items():
                bool_should["bool"]["should"].append(
                    {
                        "match": {
                            "target.attributes.{}".format(k): _pattern["target"]["attributes"][k]
                        }
                    }
                )
            main.append(bool_should)

        if "style" in _pattern["target"]:
            bool_should = {
                "bool": {
                    "should": [
                        {
                            "match": {"target.style.__check": False}
                        }
                    ]
                }
            }
            for k, _ in _pattern["target"]["style"].items():
                bool_should["bool"]["should"].append(
                    {
                        "match": {
                            "target.style.{}".format(k): _pattern["target"]["style"][k]
                        }
                    }
                )
            main.append(bool_should)

    # ------------------------------------------------- 'type'
    if "type" in _pattern:
        if "attributeMutation" in _pattern["type"]:
            main.append(
                {
                    "match": {
                        "type.attributeMutation": _pattern["type"]["attributeMutation"]
                    }
                }
            )
        elif "characterMutation" in _pattern["type"]:
            main.append(
                {
                    "match": {
                        "type.characterMutation": _pattern["type"]["characterMutation"]
                    }
                }
            )
        elif "childNodeMutation" in _pattern["type"]:
            if "addedNode" in _pattern["type"]["childNodeMutation"]:
                if "nodeName" in _pattern["type"]["childNodeMutation"]["addedNode"]:
                    main.append(
                        {
                            "match": {
                                "type.childNodeMutation.addedNode.nodeName":
                                    "({}) OR (ALL)".format(_pattern["type"]["childNodeMutation"]["addedNode"]["nodeName"]) if _pattern["type"]["childNodeMutation"]["addedNode"]["nodeName"] != "" else "ALL"
                            }
                        }
                    )
                if "method" in _pattern["type"]["childNodeMutation"]["addedNode"]:
                    main.append(
                        {
                            "match": {
                                "type.childNodeMutation.addedNode.method":
                                    "({}) OR (ALL)".format(_pattern["type"]["childNodeMutation"]["addedNode"]["method"]) if _pattern["type"]["childNodeMutation"]["addedNode"]["method"] != "" else "ALL"
                            }
                        }
                    )
                if "hidden" in _pattern["type"]["childNodeMutation"]["addedNode"]:
                    main.append(
                        {
                            "match": {
                                "type.childNodeMutation.addedNode.hidden":
                                    _pattern["type"]["childNodeMutation"]["addedNode"]["hidden"]
                            }
                        }
                    )
                if "draggable" in _pattern["type"]["childNodeMutation"]["addedNode"]:
                    main.append(
                        {
                            "match": {
                                "type.childNodeMutation.addedNode.draggable":
                                    _pattern["type"]["childNodeMutation"]["addedNode"]["draggable"]
                            }
                        }
                    )
                if "attributes" in _pattern["type"]["childNodeMutation"]["addedNode"]:
                    bool_should = {
                        "bool": {
                            "should": [
                                {
                                    "match": {"type.childNodeMutation.addedNode.attributes.__check": False}
                                }
                            ]
                        }
                    }
                    for k, _ in _pattern["type"]["childNodeMutation"]["addedNode"]["attributes"].items():
                        bool_should["bool"]["should"].append(
                            {
                                "match": {
                                    "type.childNodeMutation.addedNode.attributes.{}".format(k):
                                        _pattern["type"]["childNodeMutation"]["addedNode"]["attributes"][k]
                                }
                            }
                        )
                    main.append(bool_should)
                if "style" in _pattern["type"]["childNodeMutation"]["addedNode"]:
                    bool_should = {
                        "bool": {
                            "should": [
                                {
                                    "match": {"type.childNodeMutation.addedNode.style.__check": False}
                                }
                            ]
                        }
                    }
                    for k, _ in _pattern["type"]["childNodeMutation"]["addedNode"]["style"].items():
                        bool_should["bool"]["should"].append(
                            {
                                "match": {
                                    "type.childNodeMutation.addedNode.style.{}".format(k):
                                        _pattern["type"]["childNodeMutation"]["addedNode"]["style"][k]
                                }
                            }
                        )
                    main.append(bool_should)

            elif "removedNode" in _pattern["type"]["childNodeMutation"]:
                if "nodeName" in _pattern["type"]["childNodeMutation"]["removedNode"]:
                    main.append(
                        {
                            "match": {
                                "type.childNodeMutation.removedNode.nodeName":
                                    "({}) OR (ALL)".format(_pattern["type"]["childNodeMutation"]["removedNode"]["nodeName"]) if _pattern["type"]["childNodeMutation"]["removedNode"]["nodeName"] != "" else "ALL"
                            }
                        }
                    )
                if "method" in _pattern["type"]["childNodeMutation"]["removedNode"]:
                    main.append(
                        {
                            "match": {
                                "type.childNodeMutation.removedNode.method":
                                    "({}) OR (ALL)".format(_pattern["type"]["childNodeMutation"]["removedNode"]["method"]) if _pattern["type"]["childNodeMutation"]["removedNode"]["method"] != "" else "ALL"
                            }
                        }
                    )
                if "hidden" in _pattern["type"]["childNodeMutation"]["removedNode"]:
                    main.append(
                        {
                            "match": {
                                "type.childNodeMutation.removedNode.hidden":
                                    _pattern["type"]["childNodeMutation"]["removedNode"]["hidden"]
                            }
                        }
                    )
                if "draggable" in _pattern["type"]["childNodeMutation"]["removedNode"]:
                    main.append(
                        {
                            "match": {
                                "type.childNodeMutation.removedNode.draggable":
                                    _pattern["type"]["childNodeMutation"]["removedNode"]["draggable"]
                            }
                        }
                    )
                if "attributes" in _pattern["type"]["childNodeMutation"]["removedNode"]:
                    bool_should = {
                        "bool": {
                            "should": [
                                {
                                    "match": {"type.childNodeMutation.removedNode.attributes.__check": False}
                                }
                            ]
                        }
                    }
                    for k, _ in _pattern["type"]["childNodeMutation"]["removedNode"]["attributes"].items():
                        bool_should["bool"]["should"].append(
                            {
                                "match": {
                                    "type.childNodeMutation.removedNode.attributes.{}".format(k):
                                        _pattern["type"]["childNodeMutation"]["removedNode"]["attributes"][k]
                                }
                            }
                        )
                    main.append(bool_should)
                if "style" in _pattern["type"]["childNodeMutation"]["removedNode"]:
                    bool_should = {
                        "bool": {
                            "should": [
                                {
                                    "match": {"type.childNodeMutation.removedNode.style.__check": False}
                                }
                            ]
                        }
                    }
                    for k, _ in _pattern["type"]["childNodeMutation"]["removedNode"]["style"].items():
                        bool_should["bool"]["should"].append(
                            {
                                "match": {
                                    "type.childNodeMutation.removedNode.style.{}".format(k):
                                        _pattern["type"]["childNodeMutation"]["removedNode"]["style"][k]
                                }
                            }
                        )
                    main.append(bool_should)

    return query


def request_pattern_to_query(_pattern):
    query = {
        "_source": "description",
        "query": {
            "bool": {
                "must": list()
            }
        }
    }

    main = query["query"]["bool"]["must"]

    if "type" in _pattern:
        main.append(
            {
                "match": {
                    "type": "({}) OR (ALL)".format(_pattern["type"][0])
                }
            }
        )
    if "method" in _pattern:
        main.append(
            {
                "match": {
                    "method": "({}) OR (ALL)".format(_pattern["method"][0])
                }
            }
        )
    if "url" in _pattern:
        main.append(
            {
                "match": {
                    "url": "({}) OR (ALL)".format(_pattern["url"])
                }
            }
        )
    if "documentUrl" in _pattern:
        main.append(
            {
                "match": {
                    "documentUrl": "({}) OR (ALL)".format(_pattern["documentUrl"])
                }
            }
        )
    if "originUrl" in _pattern:
        main.append(
            {
                "match": {
                    "originUrl": "({}) OR (ALL)".format(_pattern["originUrl"])
                }
            }
        )
    if "document" in _pattern:
        main.append(
            {
                "match": {
                    "document": _pattern["document"]
                }
            }
        )
    if "origin" in _pattern:
        main.append(
            {
                "match": {
                    "origin": _pattern["origin"]
                }
            }
        )
    if "mainFrame" in _pattern:
        main.append(
            {
                "match": {
                    "mainFrame": _pattern["mainFrame"]
                }
            }
        )
    if "parentFrame" in _pattern:
        main.append(
            {
                "match": {
                    "parentFrame": _pattern["parentFrame"]
                }
            }
        )

    return query


def send_query(query, document):
    es = app.config['ES_SERVER']

    try:
        if document == "mutationMonitoring":
            r = es.search(index="dobiel_mutation_monitoring", body=query, request_timeout=20)
        elif document == "monitoringRequests":
            r = es.search(index="dobiel_monitoring_requests", body=query, request_timeout=20)
        else:
            return False, {"error": "'document' is invalid"}

    except Exception as e:
        # print(str(e))
        return False, {"mutation": "", "attack": list(), "error": str(e)}

    else:
        if r["hits"]["total"]["value"] == 0:
            return True, {"mutation": "safe", "attack": list(), "error": ""}
        else:
            result = {"mutation": "dangers", "attack": list(), "error": ""}
            for hits in r["hits"]["hits"]:
                result["attack"].append(hits["_source"]["description"])
            return True, result
