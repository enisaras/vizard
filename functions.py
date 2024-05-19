import matplotlib.pyplot as plt
import streamlit as st
from utils import fig_utils
import os
import pandas as pd
output_folder = "charts/"
os.makedirs(output_folder, exist_ok=True)

global df
df = pd.read_csv('penguins.csv')



def line_plot(x, y, title, xlabel='', ylabel='', color='blue'):
    global df
    fig, ax = plt.subplots()
    ax.plot(df[x], df[y], color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_dir = fig_utils.save_fig(fig, output_folder, title)
    st.session_state.messages.append({"role": "assistant", "chart": save_dir})
    fig.savefig(save_dir)
    return st.pyplot(fig)

def histogram(column, bins, title, xlabel='', ylabel='', color='blue'):
    global df
    fig, ax = plt.subplots()
    ax.hist(df[column], bins=bins, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_dir = fig_utils.save_fig(fig, output_folder, title)
    st.session_state.messages.append({"role": "assistant", "chart": save_dir})
    fig.savefig(save_dir)
    return st.pyplot(fig)

def bar_plot(x, y, title, xlabel='', ylabel='', color='blue'):
    global df
    fig, ax = plt.subplots()
    ax.bar(df[x], df[y], color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_dir = fig_utils.save_fig(fig, output_folder, title)
    st.session_state.messages.append({"role": "assistant", "chart": save_dir})
    fig.savefig(save_dir)
    return st.pyplot(fig)

def scatter_plot(x, y, title, xlabel='', ylabel='', color='blue'):
    global df
    fig, ax = plt.subplots()
    ax.scatter(df[x], df[y], c=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_dir = fig_utils.save_fig(fig, output_folder, title)
    st.session_state.messages.append({"role": "assistant", "chart": save_dir})
    fig.savefig(save_dir)
    return st.pyplot(fig)



