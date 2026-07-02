import streamlit as st

st.title("Contacts")
st.write("This is an app that will hold your contacts for you effortlessly!")

# Create a place to store contacts that persists across reruns
if "contacts" not in st.session_state:
    st.session_state.contacts = []

contact = st.text_input("Whos contact do you want to save?")

if contact:
    contactNumber = st.number_input(
        f"What is {contact}'s number",
        min_value=0,
        step=1,
        format="%d"
    )

    if st.button("Save Contact"):
        st.session_state.contacts.append({"name": contact, "number": contactNumber})
        st.success(f"Saved {contact}!")

# Print out all saved contacts
st.subheader("Saved Contacts")
for person in st.session_state.contacts:
    st.write(f"{person['name']}: {person['number']}")