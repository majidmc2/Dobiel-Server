RequestSchema = {
    "type": "object",
    "properties": {
        "type": {
            "type": "array",
            "items": {
                "type": "string",
                "enum": [
                    "beacon",
                    "csp_report",
                    "font",
                    "image",
                    "imageset",
                    "main_frame",
                    "object_subrequest",
                    "ping",
                    "script",
                    "speculative",
                    "stylesheet",
                    "sub_frame",
                    "web_manifest",
                    "websocket",
                    "xbl",
                    "xml_dtd",
                    "xmlhttprequest",
                    "xslt"
                ]
            }
        },
        "method": {"type": "array"},
        "url": {"type": "string"},
        "documentUrl": {"type": "string"},
        "originUrl": {"type": "string"},
        "document": {"type": "boolean"},
        "origin": {"type": "boolean"},
        "mainFrame": {"type": "boolean"},
        "parentFrame": {"type": "boolean"},
        "description": {"type": "string"}
    },
    "additionalProperties": False,
    "required": ["origin"]
}
