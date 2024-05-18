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
                    "xlabel": {
                        "type": "string",
                        "description": "label for the x-axis",
                    },
                    "ylabel": {
                        "type": "string",
                        "description": "label for the y-axis",
                    },
                },        
                "required": ["x", "y"],
            },
        },
    },

    {
        "type": "function",
        "function": {
            "name": "line_plot",
            "description": "Create a line plot of two lists.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {
                        "type": "array",
                        "description": "x value for line plot",
                        "items": {
                            "type": "number",
                        },
                    },
                    "y": {
                        "type": "array", 
                        "items": {
                            "type": "number",
                        },
                        "description": "y value for line plot"
                    },
                    "title": {
                        "type": "string",
                        "description": "title for the plot",
                    },
                    "xlabel": {
                        "type": "string",
                        "description": "label for the x-axis",
                    },
                    "ylabel": {
                        "type": "string",
                        "description": "label for the y-axis",
                    },
                },        
                "required": ["x", "y"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "bar_plot",
            "description": "Create a bar plot of two lists.",
            "parameters": {
                "type": "object",
                "properties": {
                    "x": {
                        "type": "array",
                        "description": "x value for bar plot",
                        "items": {
                            "type": "number",
                        },
                    },
                    "y": {
                        "type": "array", 
                        "items": {
                            "type": "number",
                        },
                        "description": "y value for bar plot"
                    },
                    "title": {
                        "type": "string",
                        "description": "title for the plot",
                    },
                    "color": {
                        "type": "string",
                        "description": "color of the bars",
                        "default": "blue"
                    },
                    "xlabel": {
                        "type": "string",
                        "description": "label for the x-axis",
                    },
                    "ylabel": {
                        "type": "string",
                        "description": "label for the y-axis",
                    },
                },        
                "required": ["x", "y"],
            },
        },
    }

]
