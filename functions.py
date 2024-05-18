import matplotlib.pyplot as plt
import streamlit as st
from utils import fig_utils
import os

output_folder = "charts/"
os.makedirs(output_folder, exist_ok=True)

def line_plot(x, y, title, xlabel='', ylabel='', color='blue'):
    fig, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_dir = fig_utils.save_fig(fig, output_folder, title)
    st.session_state.messages.append({"role": "assistant", "chart": save_dir})
    fig.savefig(save_dir)
    return st.pyplot(fig)

def histogram(data, bins, title, xlabel='', ylabel='', color='blue'):
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_dir = fig_utils.save_fig(fig, output_folder, title)
    st.session_state.messages.append({"role": "assistant", "chart": save_dir})
    fig.savefig(save_dir)
    return st.pyplot(fig)

def bar_plot(x, y, title, xlabel='', ylabel='', color='blue'):
    fig, ax = plt.subplots()
    ax.bar(x, y, color=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_dir = fig_utils.save_fig(fig, output_folder, title)
    st.session_state.messages.append({"role": "assistant", "chart": save_dir})
    fig.savefig(save_dir)
    return st.pyplot(fig)

def scatter_plot(x, y, title, xlabel='', ylabel='', color='blue'):
    fig, ax = plt.subplots()
    ax.scatter(x, y, c=color)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    save_dir = fig_utils.save_fig(fig, output_folder, title)
    st.session_state.messages.append({"role": "assistant", "chart": save_dir})
    fig.savefig(save_dir)
    return st.pyplot(fig)



