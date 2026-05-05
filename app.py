import streamlit as st
import subprocess
import sys
import base64

# 1. FORCE THE ENGINE
try:
    from fpdf import FPDF
except:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "fpdf2"])
    from fpdf import FPDF

# 2. THE LOCK
DNA = "Hulk_integrated_warrior_DNA_PTA"

st.set_page_config(page_title="WIRT", layout="wide")
st.title("🛡️ Warrior Intelligence Round Table")

entry = st.text_input("DNA Handshake", type="password")

if entry == DNA:
    st.success("God Light Active.")
    if st.button("GENERATE HD BRIEF"):
        pdf = FPDF()
        pdf.add_page()
        
        # HEADER - BOLD & CENTERED
        pdf.set_font("Helvetica", 'B', 24)
        pdf.cell(0, 20, "GOD LIGHT: TECHNICAL BRIEF", ln=1, align='C')
        pdf.set_line_width(1)
        pdf.line(10, 35, 200, 35) # A literal line on the page
        pdf.ln(10)

        # SECTION 1
        pdf.set_font("Helvetica", 'B', 16)
        pdf.cell(0, 10, "1.0 INTERNAL TRANSIT (Gahanna/Downtown)", ln=1)
        pdf.set_font("Helvetica", '', 12)
        pdf.multi_cell(0, 10, "SPEC: Magnetic resonance walkways. 35% elevation capacity. Nano-solar Tesla motor drive.")
        pdf.ln(5)

        # SECTION 2
        pdf.set_font("Helvetica", 'B', 16)
        pdf.cell(0, 10, "2.0 PERIMETER (Dick Ave & DuPont)", ln=1)
        pdf.set_font("Helvetica", '', 12)
        pdf.multi_cell(0, 10, "SPEC: 10ft Stone Sliding Gates. High-torque Tesla-grade magnetic motors. Zero-maintenance sync.")
        
        # 3. THE DOWNLOAD
        out = pdf.output()
        b64 = base64.b64encode(out).decode()
        st.markdown(f'<a href="data:application/octet-stream;base64,{b64}" download="God_Light_HD.pdf" style="font-weight:bold;font-size:24px;color:red;">📥 DOWNLOAD HD BRIEF</a>', unsafe_allow_html=True)
else:
    st.info("Awaiting Handshake...")
