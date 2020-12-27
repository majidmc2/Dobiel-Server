mutation_mapping = {
    "mappings": {
        "properties": {
            "description": {"type": "text"},
            "target": {
                "properties": {
                    "nodeName": {"type": "text"},
                    "attributes": {"type": "nested"},
                    "style": {"type": "nested"},
                }
            },
            "type": {
                "properties": {
                    "attributeMutation": {"type": "text"},
                    "characterMutation": {"type": "boolean"},
                    "childNodeMutation": {
                        "properties": {
                            "addedNode": {
                                "properties": {
                                    "nodeName": {"type": "text"},
                                    "method": {"type": "text"},
                                    "hidden": {"type": "boolean"},
                                    "draggable": {"type": "boolean"},
                                    "attributes": {"type": "nested"},
                                    "style": {"type": "nested"},
                                }
                            },
                            "removedNode": {
                                "properties": {
                                    "nodeName": {"type": "text"},
                                    "method": {"type": "text"},
                                    "hidden": {"type": "boolean"},
                                    "draggable": {"type": "boolean"},
                                    "attributes": {"type": "nested"},
                                    "style": {"type": "nested"},
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


request_mapping = {
    "mappings": {
        "properties": {
            "type": [],
            "method": [],
            "url": {"type": "text"},
            "documentUrl": {"type": "text"},
            "originUrl": {"type": "text"},
            "document": {"type": "boolean"},
            "origin": {"type": "boolean"},
            "mainFrame": {"type": "boolean"},
            "parentFrame": {"type": "boolean"},
            "description": {"type": "text"}
        }
    }
}
