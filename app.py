import streamlit as st
from multipage import MultiPageApp
from project import proj1, proj2, proj3

app = MultiPageApp()


# Adding your projects
app.add_app("Stock Price App", proj1.app)
app.add_app("Food Review App", proj2.app)
app.add_app("Iris Classification App", proj3.app)

app.run()