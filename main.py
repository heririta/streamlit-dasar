import streamlit.components.v1 as components
import time
import streamlit as st
import pandas as pd

st.title("coba memakai streamlit framework")


# create dataset

df = pd.DataFrame(
    {'first': ['None', 1, 2, 3, 4, 5], 'second': [6, 7, 8, 9, 10, 11]})

# st.write(df)

# df  # magic command

# visualization
# st.sidebar.line_chart(df)

# checkbox

if st.checkbox("show the table..."):
    df

# selectbox

opt = st.selectbox('which number you want to select :', df['first'])

if opt == 'None':
    st.write("you haven't selected yet.. please select a value.")
else:
    st.write('you just selected :', opt)

# slidebar
maxVal = 50
minVal = 0

val = st.slider("slider", maxVal, minVal)

if val != 50:
    st.write("The Slider value is :", val)
else:
    st.write("you just reached the maximum value")


# progress bar

pro = st.progress(0)

for i in range(50):
    pro.progress(i+1)

    time.sleep(0.2)

# beta columns st.beta_columns will be removed after 2021-11-02.

# left, right = st.beta_columns(2)

# left.write(df['first'])
# right.write(df['second'])

# beta expander st.beta_expander will be removed after 2021-11-02.
# expander = st.beta_expander("Hello")

# expander.write("how are you")

# spinner
with st.spinner("Loading..."):
    time.sleep(5)


st.error("Loading Unsuccessfull")  # Error Message


st.success("Loaded Successfull")  # Success Message


st.warning("this is a warning message")  # Warning Message


st.info("This is a info message")  # Info Message

st.balloons()  # ballons animation


components.html("<html><body>This is the HTML Part</body></html>")
