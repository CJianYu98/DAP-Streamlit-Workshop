import streamlit as st

class MultiPageApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

    def run(self):
        st.sidebar.header("Navigation")
        app = st.sidebar.radio(
        # app = st.selectbox(
            '',
            self.apps,
            format_func=lambda app: app['title'])

        app['function']()