import streamlit as st
import time
from datetime import datetime, timedelta

def create_timer():
    # Initialize session state variables if they don't exist
    if 'start_time' not in st.session_state:
        st.session_state.start_time = None
        st.session_state.duration = 0
        st.session_state.is_running = False

    st.title("⏱️ Countdown Timer")
    
    # Timer controls
    col1, col2 = st.columns(2)
    with col1:
        minutes = st.number_input("Minutes", min_value=0, max_value=60, value=0)
    with col2:
        seconds = st.number_input("Seconds", min_value=0, max_value=59, value=0)
    
    total_seconds = minutes * 60 + seconds
    
    # Start/Stop buttons
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Start"):
            st.session_state.start_time = datetime.now()
            st.session_state.duration = total_seconds
            st.session_state.is_running = True
    with col2:
        if st.button("Stop"):
            st.session_state.is_running = False

    # Display timer
    if st.session_state.is_running:
        time_elapsed = datetime.now() - st.session_state.start_time
        time_left = max(timedelta(seconds=st.session_state.duration) - time_elapsed, timedelta(0))
        
        # Convert time_left to minutes and seconds
        minutes_left = int(time_left.total_seconds() // 60)
        seconds_left = int(time_left.total_seconds() % 60)
        
        # Display timer in large text
        st.markdown(f"<h1 style='text-align: center; color: #1abc9c;'>{minutes_left:02d}:{seconds_left:02d}</h1>", 
                   unsafe_allow_html=True)
        
        # Stop timer when it reaches zero
        if time_left == timedelta(0):
            st.session_state.is_running = False
            st.balloons()
        
        # Rerun the app every second to update the timer
        time.sleep(0.1)
        st.rerun()

if __name__ == "__main__":
    create_timer()
