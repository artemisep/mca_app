import streamlit as st
import time


st.header('Translate Medical Documents to Universal Common Code ICD-10-CM')
uploaded_file = st.file_uploader('Upload Medical Report: ')

#with open(uploaded_file.name) as f:
#    line = f.readlines()

#st.text(line)

def click_button():
    pass

#st.button('start to translate... ', on_click=click_button)


codes_output = ""
#st.markdown(line)
if uploaded_file:
    st.markdown("processing...")
    time.sleep(2)
    
    st.subheader("**Medical Report:**")
    st.markdown("'Patient is a 27-year-old white male. :red[Not an established patient]. Height is 74 inches, weight 220 lbs. Patient states he is allergic to penicillin, but has no other outstanding medical history. Does not smoke, exercises moderately.\n', 'Patient presents with chills, headache, cough, fever (101 degrees), difficulty breathing. :red[Examination via stethoscope] yields heavy rales. :red[Percussion test on thorax] suggests buildup in :red[lungs]. :red[Streptococcal pneumoniae] suspected.\n', 'Obtained blood sample for :red[Antistreptolysin O titer]. Results yield level of :red[ASO] above 200. :red[Diagnosis of streptococcal pneumoniae] confirmed. Prescribed patient two weeks of 500mg azithromycin (Zithromax), and scheduled follow-up for next week.'")

    st.subheader("**Codes and Validation:**")

    diagnosis_val = '481'
    st.markdown(diagnosis_val + ":green[ - pneumococcal pneumonia [streptococcum pneumoniae pneumonial]], Confidence Score: 98.01%")
    st.text_input("**Edit**", key='diagnosis')
    #st.checkbox("Submit", key='diagnosis_submit')

    HEM_val = '86060'
    st.markdown(HEM_val + ":green[ - ASO is from pathology test], Confidence Score: 99.5%")
    st.text_input("**Edit**", key='HEM')
    #st.checkbox("Submit", key='HEM_submit')

    pathology_val = '99203'
    st.markdown(pathology_val+ ":orange[ - new patient, detailed history, a detailed examination, medical decision making of low complexity], Confidence Score: 80.45%")
    pathology_val = st.text_input("**Edit**", key='pathology')
    if pathology_val: 
        st.markdown("updated code: " + pathology_val)
    #st.checkbox("Submit", key='submit')

    codes_output = diagnosis_val + ' ' + HEM_val + ' ' + pathology_val

    st.button('Submit ', on_click=click_button)

    out_filename = 'newfile'

    line = "test"
    #st.download_button('Download Code for Claim', ''.join(line), file_name=out_filename)
    st.download_button('Export Code for Claim', codes_output)

    #https://docs.streamlit.io/library/api-reference/text/st.markdown


