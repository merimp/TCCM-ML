import streamlit as st

print(st.__version__)
st.title("This is my first app")


my_button = st.button("Show me weather features")

if my_button:
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "70 °F", "1.2 °F")
        col2.metric("Wind", "9 mph", "-8%")
        col3.metric("Humidity", "86%", "4%")


values = st.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0))
st.write('Values:', values)


#age = st.slider('How old are you?', 0, 130, 25)
#st.write("I'm ", age, 'years old')
~                                  
