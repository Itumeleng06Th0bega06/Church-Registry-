import streamlit as st
import pandas as pd

st.image("Shekinah_logo.png", width=300)
st.markdown("**:orange[Welcome to 2024 Building Legacy Conference!]**")
col1,col2=st.columns([2,1])

with col1:
    with st.form("form", clear_on_submit=True):
        star=st.markdown(":blue[required] "'*')
        name=st.text_input(":blue[Name and Surname]"' *')
        place=st.text_input(":blue[Place]"'   *')
        gender=st.radio(":blue[Gender]"'  *',["Male","Female"])
        att=st.multiselect(":blue[Select all days you will be Attending?]",["Thurs","Fri","Sat","Sunday"])
        family=st.text_input(":blue[Please Indicate how many Children are you coming with.]")
        contact=st.number_input(":blue[Contacts]"' *', value=None, step=1, placeholder="Only ten digits")
        submit=st.form_submit_button("Register", help="!!Please Make Sure Your information is correct before saving!!")
        # we initialize an empty storage
        if 'all_members_info' not in st.session_state:
            st.session_state.all_members_info = []
        # set conditions for the execution
        if submit:
            if name and place and gender and contact:# we check if required fields are filled and store the info in a dict.
                members_info=[name,
                      place,
                      gender,
                      att,
                      family,
                      contact]
                st.session_state.all_members_info.append(members_info)# we append the info back to the **initialization**            
                #st.write(st.session_state.all_members_info)
                st.success("Successfully Registered!")
            else:
                st.error("Please fill out all required fields.")

df=pd.DataFrame(st.session_state.all_members_info)
df.to_csv('members_data.csv',index=False)

with col2:
    st.image("building.jpg", width=380)
