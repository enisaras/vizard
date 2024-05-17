import matplotlib.pyplot as plt
import streamlit as st


def scatter_plot(x, y, title, color='blue'):
    fig, ax = plt.subplots()
    ax.scatter(x, y, c=color)
    ax.set_title(title)
    return st.pyplot(fig)

def line_plot(x, y, title, color='blue'):
    fig, ax = plt.subplots()
    ax.plot(x, y, color=color)
    ax.set_title(title)
    return st.pyplot(fig)

def histogram(data, bins, title, color='blue'):
    fig, ax = plt.subplots()
    ax.hist(data, bins=bins, color=color)
    ax.set_title(title)
    return st.pyplot(fig)

def bar_plot(x, y, title, color='blue'):
    fig, ax = plt.subplots()
    ax.bar(x, y, color=color)
    ax.set_title(title)
    return st.pyplot(fig)

