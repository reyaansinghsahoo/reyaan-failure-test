import streamlit as st

st.title("reyaan failure test")

with st.form("question 1"):
    n1=51
    n2=34
    s=n1+n2
    a=s st.number_input("enter your answer", step=1)
    if st.form_submit_buton("check awnswer"):
        st.write("your anwswer",a)
        st.write("actual anwswer:",s)
        if a==s:
            st.write("fantastic whoooohoooooooo")
        else:
            st.write("boo red card")



















