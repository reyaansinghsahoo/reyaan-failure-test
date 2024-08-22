import streamlit as st

st.title("reyaan failure test")

q=[1,2,3,4,5,6,7,8,9,10]

for c in q:
    st.write(c)

    with st.form("question 1"):
        n1=51
        n2=34
        s=n1+n2
        st.write("what is the sum of",n1," and ",n2)
        a=st.number_input("enter your answer", step=1)
        if st.form_submit_button("check answer"):
            st.write("your anwswer is",a)
            st.write("actual anwswer:",s)
            if a==s:
                st.write("fantastic whoooohoooooooo")
            else:
                st.write("boo red card")
    


















