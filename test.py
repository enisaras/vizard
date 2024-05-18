from openai import OpenAI
from functions import scatter_plot, bar_plot, line_plot
from tools import tools
import json
import streamlit as st
from streamlit.delta_generator import DeltaGenerator
client = OpenAI(api_key="")

def run_conversation(system_prompt, user_prompt):
    # Step 1: send the conversation and available functions to the model
    system_message = {"role": "system", "content": system_prompt}
    user_message = {"role": "user", "content": user_prompt}
    messages = [system_message, user_message]
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message
    print(response_message)
    tool_calls = response_message.tool_calls
    chart = None
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "scatter_plot": scatter_plot,
            "bar_plot": bar_plot,
            "line_plot": line_plot,
        }  # only one function in this example, but you can have multiple
        messages.append(response_message)  # extend conversation with assistant's reply

        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                x=function_args.get("x"),
                y=function_args.get("y"),
                title=function_args.get("title"),
                color=function_args.get("color")
            )
            # Ensure function_response is JSON serializable
            if isinstance(function_response, DeltaGenerator):
                chart = function_response

            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": "Chart generated",
                }
            )  # extend conversation with function response
        print(messages)
        second_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        return second_response, chart

    return response, None
    


