MutationSchema = {
    "properties": {
        "target": {
            "type": "object",
            "properties": {
                "nodeName": {"type": "string"},
                "attributes": {"type": "object"},
                "style": {"type": "object"},
            },
            "additionalProperties": False
        },
        "type": {
            "type": "object",
            "properties": {
                "attributeMutation": {"type": "string"},
                "characterMutation": {"type": "boolean"},
                "childNodeMutation": {
                    "type": "object",
                    "properties": {
                        "addedNode": {
                            "type": "object",
                            "properties": {
                                "nodeName": {"type": "string"},
                                "method": {"type": "string"},
                                "hidden": {"type": "boolean"},
                                "draggable": {"type": "boolean"},
                                "attributes": {"type": "object"},
                                "style": {"type": "object"},
                            },
                            "additionalProperties": False
                        },
                        "removedNode": {
                            "type": "object",
                            "properties": {
                                "nodeName": {"type": "string"},
                                "method": {"type": "string"},
                                "hidden": {"type": "boolean"},
                                "draggable": {"type": "boolean"},
                                "attributes": {"type": "object"},
                                "style": {"type": "object"},
                            },
                            "additionalProperties": False
                        }
                    },
                    "additionalProperties": False
                },
                "additionalProperties": False
            }
        },
        "description": {"type": "string"}
    },
    "additionalProperties": False
}
