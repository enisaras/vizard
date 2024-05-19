tools = [
    {
        "type": "function",
        "function": {
            "name": "scatter_plot",
            "description": "Create a scatter plot of two columns from a pandas dataframe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "df": {
                        "type": "object",
                        "description": "pandas dataframe containing the data, this is required to plot.",
                    },
                    "x": {
                        "type": "string",
                        "description": "column name for x value in the dataframe",
                    },
                    "y": {
                        "type": "string", 
                        "description": "column name for y value in the dataframe"
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
                "required": ["df", "x", "y"],
            },
        },
    },

    {
        "type": "function",
        "function": {
            "name": "line_plot",
            "description": "Create a line plot of two columns from a pandas dataframe",
            "parameters": {
                "type": "object",
                "properties": {
                    "df": {
                        "type": "object",
                        "description": "pandas dataframe containing the data, this is required to plot.",
                    },
                    "x": {
                        "type": "string",
                        "description": "column name for x value in the dataframe",
                    },
                    "y": {
                        "type": "string",
                        "description": "column name for y value in the dataframe",
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
                "required": ["df", "x", "y"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "bar_plot",
            "description": "Create a bar plot of two columns from a pandas dataframe.",
            "parameters": {
                "type": "object",
                "properties": {
                    "df": {
                        "type": "object",
                        "description": "pandas dataframe containing the data, this is required to plot.",
                    },
                    "x": {
                        "type": "string",
                        "description": "column name for x value in the dataframe",
                    },
                    "y": {
                        "type": "string", 
                        "description": "column name for y value in the dataframe"
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
                "required": ["df", "x", "y"],
            },
        },
    }

]
