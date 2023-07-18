import streamlit as st


st.header('Translate Medical Documents to Universal Common Code ICD-10-CM')
uploaded_file = st.file_uploader('Upload a file')

#with open(uploaded_file.name) as f:
#    line = f.readlines()

#st.text(line)

def click_button():
    pass

#st.button('start to translate... ', on_click=click_button)

#st.markdown(line)
st.markdown("**Medical Report:**")
st.markdown("'Patient is a 27-year-old while male. :red[Not an established patient]. Height is 74 inches, weight 220 lbs. Patient states he is allergic to penicillin, but has no other outstanding medical history. Does not smoke, exercises moderately.\n', 'Patient presents with chills, headache, cough, fever (101 degrees), difficulty breathing. :red[Examination via stethoscope] yields heavy rales. :red[Percussion test on thorax] suggests buildup in :red[lungs]. :red[Streptococcal pneumoniae] suspected.\n', 'Obtained blood sample for :red[Antistreptolysin O titer]. Results yield level of :red[ASO] above 200. :red[Diagnosis of streptococcal pneumoniae] confirmed. Prescribed patient two weeks of 500mg azithromycin (Zithromax), and scheduled follow-up for next week.'")
st.markdown("**Codes and rational:**")
st.markdown(":green[481 - pneumococcal pneumonia [streptococcum pneumoniae pneumonial]]")
st.markdown(":green[99203 - new patient, detailed history, a detailed examination, medical decision making of low complexity]")
st.markdown(":green[86060 - ASO is from pathology test]")


out_filename = 'newfile'

line = "test"
#st.download_button('Download Code for Claim', ''.join(line), file_name=out_filename)
st.download_button('Download Code for Claim', ''.join(line))

#https://docs.streamlit.io/library/api-reference/text/st.markdown


