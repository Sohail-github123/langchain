import streamlit as st
import langchain_helper as lch

st.title("Pets Name Generator")

user_animal_type = st.sidebar.selectbox("What is your pet?", ("Dog", "Cat", "Hamster", "Cow"))

if user_animal_type == 'Dog':
    pet_color =st.sidebar.text_area(label='what color is your Dog?',
    max_chars=15)

if user_animal_type == 'cat':
    pet_color =st.sidebar.text_area(label='what color is your cat?',
    max_chars=15)

if user_animal_type == 'Hamster':
    pet_color =st.sidebar.text_area(label='what color is your Hamster?',
    max_chars=15)

if user_animal_type == 'cow':
    pet_color =st.sidebar.text_area(label='what color is your cow?',
    max_chars=15)
   
if pet_color :
    response = lch.generate_pet_name(user_animal_type, pet_color)
    st.text(response)