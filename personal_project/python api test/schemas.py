get_gen_clients_language_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "packageName": {
            "type": "object",
            "properties": {
                "opt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "default": {
                    "type": "string"
                }
            }
        },
        "projectName": {
            "type": "object",
            "properties": {
                "opt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                }
            }
        },
        "packageVersion": {
            "type": "object",
            "properties": {
                "opt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "default": {
                    "type": "string"
                }
            }
        },
        "packageUrl": {
            "type": "object",
            "properties": {
                "opt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                }
            }
        },
        "sortParamsByRequiredFlag": {
            "type": "object",
            "properties": {
                "opt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "default": {
                    "type": "string"
                }
            }
        },
        "hideGenerationTimestamp": {
            "type": "object",
            "properties": {
                "opt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "default": {
                    "type": "string"
                }
            }
        },
        "library": {
            "type": "object",
            "properties": {
                "opt": {
                    "type": "string"
                },
                "description": {
                    "type": "string"
                },
                "type": {
                    "type": "string"
                },
                "default": {
                    "type": "string"
                }
            }
        }
    }
}
post_gen_clients_language_schema = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "code": {
            "type": "string"
        },
        "link": {
            "type": "string"
        }
    }
}