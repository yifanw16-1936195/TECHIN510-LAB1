import streamlit as st
import pandas as pd
import seaborn as sns
from datetime import datetime
import pytz

# Page configuration
st.set_page_config(page_title="Yifan Wang\'s Portfolio", page_icon="./images/favicon.png")

# Title
st.title('Yifan Wang\'s Portfolio')

# Introduction
st.header('Hi! I am Yifan Wang,')
st.subheader('A tech-driven, innovative, interdisciplinary UX Designer & Tech Lover')

st.image('./images/profile.jpeg', caption='Yifan Wang profile picture', use_column_width=True)

# Bio
st.header('About Me')
st.write("""
I developed an interest in UX design and research through my experiences interacting with my family members and the disability groups in an internship. While I grew a deep fascination in human factors, I became aware of the importance of bringing more accessible and sustainable designs for minority and senior groups who should also be benefited by technological development.

My research in HCI has ranged from launching a senior AI healthcare platform at the Seattle start-up that brings high-tech healthcare senior product, to building a metaverse extension for the Zoom office product that creates an immersive video communication experience.

I’ve explored a variety of approaches including data visualization, machine learning, Artificial Intelligence, VR/AR, etc.

In my free time, you can find me dancing K-pop and Jazz, traveling, staying with my cats, playing the pianos, and expanding my ever-growing collection of different cat foods in the world.
""")

# Work Experience
st.header('Work Experience')
st.write("""
**Nuubi | UX Designer Intern** (March 2024 - Present, Miami, FL - Remote)
- Collaborated with interdisciplinary teams to improve the user experience for Nuubi's e-learning platform across both mobile app and website interfaces.
- Initiated and designed the beta version of Nuubi's website.
- Engaged in pivotal product strategy and marketing discussions, leading to the website welcome page marketing strategy and design.
- Executed usability testing for the mobile app prototype, gathering critical feedback to pinpoint and address user experience pain points.

**Aeyesafe | UX Designer Intern** (Jan 2023 - June 2023, Redmond, WA)
- Initiated key feature design for a B2B senior healthcare web platform, using AI-assisted tech to digitalize caregiving experiences.
- Developed easy-to-read data visualization dashboard with complex inputs that increased usability while leveraging technology and uplifting business goals.
- Created 18 user-friendly alerts from complex decision trees with engineers.
- Increased key task completion by 35% by performing 10 usability tests to ensure optimum readability and efficacy.
- Created a design system to increase brand consistency.

**IWP Capital | UX Designer Intern** (June 2022 - Sept 2022, Fort Worth, TX)
- Redesigned the onboarding for a mobile fintech app to reduce drop-off rates.
- Iterated four versions of user flow and proposed the usage of stepper design.
- Facilitated discussions to align on success metrics, ensuring usability by gathering feedback from over 50 users and increasing onboarding success rate to 92%.
- Worked with cross-functional teams to create customer brand visual design and enhance feature discoverability.
""")

# Research Experience
st.header('Research Experience')
st.write("""
**CBH Youth | UX Designer & Developer** (June 2023 - Present, University of Washington CBH Research Group)
- Led the redesign of UW youth mental health research website.
- Revamped website with new UI and layout, boosting user satisfaction by 40%.
- Contributed to the web frontend development in HTML, CSS, and JavaScript.
- Elevated design documentation standards and published design system style guide with research lead, enhancing the handoffs to developers.
""")

# Education
st.header('Education')
st.write("""
**University of Washington**
- M.S in Technology Innovation, Specialization in HCI (Sept 2023 - March 2025)
- B.S in Human Center Interaction, B.S in Statistics - Data Science (Sept 2019 - June 2023)
""")

# Skills
st.header('Skills')
st.write("""
**Design Tools:** Figma, Illustrator, Adobe XD, Framer, Photoshop, Fusion360

**UX Skills:** Product Strategy, Usability Testing & Research, Accessibility, A/B Testing, Contextual Inquiry, Competitor Analysis, Information Architecture, Journey Mapping

**Programming:** HTML, CSS, Javascript, Python, TypeScript, React, Bootstrap, Node.js, D3.js, Chart.js
""")

# Awards
st.header('Awards')
st.write("""
- **iF Design Award 2023:** Finalist - Sanctify Fintech Redesign
""")
