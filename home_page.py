import streamlit as st

def home_page():
    st.markdown(
        """
        <div style="text-align: center;">
            <h1>LOAN PREDICTION SYSTEM</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
    """
    <style>
    /* Apply background image to the main content area */
    .main {
        background-image: url('https://miro.medium.com/v2/resize:fit:735/0*_DPvD2SGibZBsb9f.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-color: rgba(255, 255, 255, 0.5);
        background-blend-mode: overlay;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

    # Center the image
    st.markdown(
        """
        <div style="text-align: center;">
            <img src="https://media.istockphoto.com/id/508021898/video/education-expenses-loan-graduation-cap-on-smart-phone-pad-mobile.jpg?s=640x640&k=20&c=eBi43oQi4lApJzAuYDVVWOQBf0nZ3sb99fbn-pJEBhg=" style="max-width: 40%;">
        </div>
        """,
        unsafe_allow_html=True
    )
