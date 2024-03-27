import streamlit as st

# Title of your personal website
st.title('My Personal Website')

# Profile picture
st.image('profile_picture.jpg', caption='Yifan Wang Profile Picture', use_column_width=True)

# About Me section
st.header('About Me')
st.write('Hi, my name is Yifan Wang.')

# Education section
st.header('Education')
st.write('''
- University of Washington, Seattle, WA
''')

# Work Experience section
st.header('Work Experience')
st.write('''
- Job Title, Company Name, Employment Dates
    - Description
''')

# Projects
st.header('Projects')
st.write('''
- **Project Name**: Aeyesafe
''')

# Contact Me
st.header('Contact Me')

