import streamlit as st

# Define criteria for the dropdown
criteria = ["Blender", "3D Object", "FBX", "Cinema 4D", "MAX", "STL"]

# Create the dropdown with a clear label
selected_criterion = st.sidebar.selectbox("Choose a criterion:", criteria, key="criteria")

# Define functions for different pages
def page_1():
    st.title("Blender")
    st.write("Dive into the ocean of high definition blender models")

def page_2():
    st.title("3D Object")
    st.write("Explore the world of graphics using OBJ files for your work")

def page_3():
    st.title("FBX")
    st.write("Use the models with FBX models, a commonly used extension")

def page_4():
    st.title("Cinema 4D")
    st.write("This is the content for Cinema 4D, a world-wide prefered software")

def page_5():
    st.title("MAX")
    st.write("Use the speciality of MAX models to turn your models to a whole different world")

def page_6():
    st.title("STL")
    st.write("Turn your 3D models to reality")

# Map criteria to corresponding functions
page_mapping = {
    "Criterion 1": page_1,
    "Criterion 2": page_2,
    "Criterion 3": page_3,
    "Criterion 3": page_4,
    "Criterion 3": page_5,
    "Criterion 3": page_6,
}

# Call the appropriate function based on the selected criterion
page_mapping[selected_criterion]()