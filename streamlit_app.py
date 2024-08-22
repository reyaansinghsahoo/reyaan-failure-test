import streamlit as st

st.title("reyaan failure test")

q=[1,2,3,4,5,6,7,8,9,10]
list1=[100,200,300,400,500,600,700,800,900,1000]
list2=[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]

st.write(list1[3])
i=0
for c in q:
    st.write(c)

    with st.form(str(c)):
        n1=list1[i]
        n2=list2[i]
        i=i+1
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
    


















