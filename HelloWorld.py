import streamlit as st

st.title("Building Magic with Streamlit!🎨")

st.markdown(
    """ 
    🎉 **Welcome to Your Streamlit Playground!** 🚀  

    This is your space to experiment, explore, and have **fun** with Streamlit!  

    🔥 **What can you do here?**  
    - 🎨 Pick a color and customize :rainbow[**'Hello, World!'**] 
    - 🎈 Send :rainbow[**balloons**] to celebrate  
    - 🎉 Shower the screen with :rainbow[**confetti**]
     
    Ready? Let's make something awesome! 🚀
    """
)

st.markdown(
    """
    <style>
        .color-picker-title {
            text-align: center;
            font-size: 32px; 
            font-weight: bold;
        }
    </style>
    <h2 class='color-picker-title'>🎨 Pick a Color for Hello World! 🎨</h2>
    """,
    unsafe_allow_html=True
)

r = st.slider("Red", 0, 255, 255)
g = st.slider("Green", 0, 255, 0)
b = st.slider("Blue", 0, 255, 0)
text_color = f"rgb({r}, {g}, {b})"

st.markdown(f"<h1 style='color:{text_color}; text-align: center;'>Hello World!</h1>", unsafe_allow_html=True)

st.write("")  

st.markdown(
    """
    <style>
        .button-container {
            display: flex;
            justify-content: center;
            gap: 20px;
        }
        .stButton>button {
            width: 200px;
            height: 50px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 10px;
            transition: 0.3s;
        }
        .stButton>button:hover {
            transform: scale(1.1);
        }
    </style>
    """,
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    if st.button("🎈 Send Balloons!"):
        st.balloons()

with col2:
    if st.button("🎉 Send Confetti!"):
        st.snow()
