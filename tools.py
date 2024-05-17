tools = [
    {
        "type": "function",
        "function": {
            "name": "scatter_plot",
            "description": "Create a scatter plot of two lists.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {
                        "type": "array",
                        "description": "x value for scatter plot",
                        "items": {
                            "type": "number",
                        },
                    },
                    "y": {
                        "type": "array", 
                        "items": {
                            "type": "number",
                        },
                        "description": "y value for scatter plot"
                    },
                    "title": {
                        "type": "string",
                        "description": "title for the plot",
                    },
                },        
                "required": ["x", "y"],
            },
        },
    }
]
