import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import time


############################
#       DISPLAY TEXT       #
############################

# Adding title
st.title("My First Streamlit App")

# Adding header
st.header("Header")

# Adding subheader
st.subheader("Sub Header")

# Add text
st.text("I love DAP")

# Add a markdown - can refer to the markdown cheatsheet
st.markdown("""
    # H1 tag
    ## H2 tag
    ### H3 tag
    :moon: <br>
    :smile: <br>
    ** bold **
    _ italics _
""", True)

# Adding mathematical expressions as Latex
st.latex(r'''
        a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
...     \sum_{k=0}^{n-1} ar^k =
...     a \left(\frac{1-r^{n}}{1-r}\right)
...     ''')

# Writing with arguments
data_dict = {
    "numbers": [1, 2, 3, 4],
    "fruits": ['apple', 'orange', 'pear', 'banana'],
    "colours": ['red', 'blue', 'yellow', 'pink']
}

st.write(data_dict)
st.write(sum)
st.write(" ## The _ write _ function is very powerful!")


############################
#       DISPLAY DATA       #
############################

data_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
data_dict = {
    "numbers": [1, 2, 3, 4],
    "fruits": ['apple', 'orange', 'pear', 'banana'],
    "colours": ['red', 'blue', 'yellow', 'pink']
}

# Display dataframe
df1 = pd.DataFrame(data_dict)
st.dataframe(df1, width=400, height=200)
st.write(df1)

# Writing text with dataframe as a block of code
df2 = pd.read_csv('./demo_data.csv')
st.write(
    'This is referring to the DataFrame below', 
    df2, 
    'This is referring to the DataFrame above'
)

# Display all data records as a table
st.table(data_list)

# Display json data
st.json(data_dict)

# Caching 
@st.cache
def load_date_slowly(df):
    start_time = time.time()
    time.sleep(5)
    df = pd.read_csv('./demo_data.csv')
    print(time.time() - start_time)
    return df

if st.checkbox("DataFrame1"):
    st.write(load_date_slowly(df1))

if st.checkbox("DataFrame2"):
    st.write(load_date_slowly(df1))


############################
#       DISPLAY PLOT       #
############################
# able to show native streamlit charts, matplotlib, altair, plotly

data = pd.DataFrame(
    np.random.randn(100, 3),
    columns = ['a', 'b', 'c']
)

# Streamlit line chart
st.line_chart(data)

# Streamlit area chart
st.area_chart(data)

# Streamlit bar chart
st.bar_chart(data)

# Streamlit map plot
df = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)

# Using matplotlib 
x = data['a']
y = data['b']

fig, ax = plt.subplots()
ax.scatter(x, y)
plt.title("Scatter Plot")
st.pyplot(fig)

# Using plotly
plotly_fig = px.scatter(x=[0, 1, 2, 3, 4], y=[0, 1, 4, 9, 16])
st.plotly_chart(plotly_fig)

# Adding image
st.image('SMU Logo.png')


############################
#       DISPLAY WIDGET     #
############################

# Adding buttons
if st.button('Click Me!'):
    st.write("You have clicked me!")

# Adding 1 line text input
name = st.text_input("Name")
st.write(name)

# Adding multi line text input
address = st.text_area("Enter your address")
st.write(address)

# Adding date input
st.date_input('Enter a date')

# Adding time input
st.time_input('Enter a time')

# Add checkbox
if st.checkbox("Click me"):
    st.write("Thank you!")

# Adding radio input
v1 = st.radio('Colours', ['r', 'g', 'b'], index =0)
st.write(v1)

# Adding dropdown select box input
v2 = st.selectbox('Colours', ['r', 'g', 'b'], index =0)
st.write(v2)

# Adding multi select input
v3 = st.multiselect('Colours', ['r', 'g', 'b'])
st.write(v3)

# Adding a slder
st.slider("Age", min_value=18, max_value=60, value=18, step=2)

# Adding number input
st.number_input("Number", min_value=18.0, max_value=60.0, value=18.0, step=2.0)

# Adding file upload
img = st.file_uploader("Upload a file")
# st.image(img)


############################
#      DISPLAY SIDEBAR     #
############################

data = {
    'num': [x for x in range(1,11)],
    'square': [x**2 for x in range(1,11)],
    'twice': [x*2 for x in range(1,11)],
    'thrice': [x*3 for x in range(1,11)],
}

rad = st.sidebar.radio("Navigation", ['Home', 'About Us'])

if rad == 'Home':
    df = pd.DataFrame(data)

    column_names = list(df.columns)
    cols = st.sidebar.multiselect("Select a number", column_names, default=['num'])
    fig, ax = plt.subplots()
    ax.plot(df['num'], df[cols])

    st.pyplot(fig)

if rad == 'About Us':
    st.write('You are in About Us Page')

    progress = st.progress(0)
    for i in range(100):
        time.sleep(0.1)
        progress.progress(i+1)

    st.error("Error")
    st.success("Success")
    st.info("Infomation")
    st.exception(RuntimeError('Error'))
    st.warning("Warning")


############################
#          LAYOUT          #
############################
st.title("Registration Form")

first, last = st.beta_columns(2)

first.text_input("First Name")
last.text_input("Last Name")

email, mobile = st.beta_columns([3, 1])
email.text_input('Email')
mobile.text_input('Mobile')

# empty column
c1, b1, c2 = st.beta_columns(3)
c1.checkbox('I Agree')
c2.button('Submit!')