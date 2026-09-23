"""
AI Smart Health Kiosk - User Interface
A simple interface for checking health risk using AI
"""

import streamlit as st
import pickle
import pandas as pd

# Load the trained model
@st.cache_resource
def load_model():
    with open('health_model.pkl', 'rb') as f:
        model = pickle.load(f)
    return model

# Main app
def main():
    # Set page title
    st.set_page_config(page_title="AI Health Kiosk", page_icon="🏥")
    
    # Title
    st.title("🏥 AI Smart Health Kiosk")
    st.write("Enter your health information to get an instant risk assessment")
    
    st.markdown("---")
    
    # Create two columns for better layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📋 Basic Information")
        age = st.number_input(
            "Your Age", 
            min_value=1, 
            max_value=120, 
            value=25,
            help="Enter your age in years"
        )
        
        temperature = st.number_input(
            "Temperature (°F)", 
            min_value=95.0, 
            max_value=106.0, 
            value=98.6,
            step=0.1,
            help="Normal range: 97-99°F"
        )
        
        heart_rate = st.number_input(
            "Heart Rate (beats/min)", 
            min_value=40, 
            max_value=200, 
            value=75,
            help="Normal range: 60-100 bpm"
        )
    
    with col2:
        st.subheader("🩺 Vital Signs")
        spo2 = st.number_input(
            "Blood Oxygen (SpO2 %)", 
            min_value=70, 
            max_value=100, 
            value=98,
            help="Normal range: 95-100%"
        )
        
        st.write("")  # Spacing
        st.write("")  # Spacing
        
        num_symptoms = st.slider(
            "Number of Symptoms", 
            min_value=0, 
            max_value=10, 
            value=0,
            help="How many symptoms are you experiencing?"
        )
    
    st.markdown("---")
    
    # Assess button
    if st.button("🔍 Check My Risk Level", type="primary", use_container_width=True):
        # Load model
        model = load_model()
        
        # Create input data
        input_data = pd.DataFrame({
            'age': [age],
            'temperature': [temperature],
            'heart_rate': [heart_rate],
            'spo2': [spo2],
            'num_symptoms': [num_symptoms]
        })
        
        # Make prediction
        prediction = model.predict(input_data)[0]
        
        # Show result with animation
        st.balloons()
        
        st.markdown("---")
        st.subheader("📊 Assessment Result")
        
        # Display result based on risk level
        if prediction == "LOW":
            st.success("### 🟢 LOW RISK")
            st.info("""
            **Good news!** Your vital signs appear normal.
            
            ✅ **Recommendations:**
            - Continue monitoring your health
            - Maintain a healthy lifestyle
            - Stay hydrated and get enough rest
            """)
            
        elif prediction == "MODERATE":
            st.warning("### 🟡 MODERATE RISK")
            st.info("""
            **Attention needed.** Some concerning signs detected.
            
            ⚠️ **Recommendations:**
            - Monitor your symptoms closely
            - Consider consulting a healthcare provider
            - Rest and avoid strenuous activities
            - Drink plenty of fluids
            """)
            
        else:  # HIGH
            st.error("### 🔴 HIGH RISK")
            st.info("""
            **Important!** Multiple concerning indicators detected.
            
            🚨 **Recommendations:**
            - Seek medical attention immediately
            - Do not ignore these symptoms
            - Contact your doctor or visit urgent care
            - Have someone accompany you if possible
            """)
        
        # Show the values entered
        with st.expander("📝 See your entered values"):
            st.write(f"- Age: {age} years")
            st.write(f"- Temperature: {temperature}°F")
            st.write(f"- Heart Rate: {heart_rate} bpm")
            st.write(f"- Blood Oxygen: {spo2}%")
            st.write(f"- Symptoms: {num_symptoms}")
    
    # Footer
    st.markdown("---")
    st.caption("⚠️ This is an AI-based screening tool and should not replace professional medical advice.")
    st.caption("💡 Always consult with healthcare professionals for medical decisions.")

if __name__ == "__main__":
    main()
