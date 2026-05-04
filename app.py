import streamlit as st
from fpdf import FPDF
import io
from datetime import datetime

# DNA Verification Layer - LOCKED CONSTANT
DNA_SEQUENCE = "Hulk_integrated_warrior_DNA_PTA"

st.set_page_config(page_title="DNA Code to PDF Translator", layout="wide")

st.title("🧬 Integrated Warrior DNA Code Translator")
st.markdown("*Convert DNA Verification Code → Process → Generate Downloadable HD PDF*")

# Sidebar for settings
with st.sidebar:
    st.header("🔐 DNA Verification")
    dna_verify = st.text_input("Enter DNA Sequence:", value=DNA_SEQUENCE, type="password", key="dna_verify")
    
    st.markdown("---")
    st.header("⚙️ Settings")
    pdf_quality = st.selectbox("PDF Quality", ["Standard", "HD", "Ultra HD"])
    author_name = st.text_input("Author Name (optional)", placeholder="Your name")

# Main interface
col1, col2 = st.columns(2)

with col1:
    st.subheader("📋 Input: DNA Code")
    dna_input = st.text_area(
        "Paste your Integrated Warrior Verbiage/DNA Code here:",
        height=300,
        placeholder="Enter your DNA verification code...",
        key="dna_input"
    )

with col2:
    st.subheader("📊 Processing Status")
    if dna_input:
        st.success("✓ DNA Code Detected")
        st.info(f"Characters: {len(dna_input)}")
        st.info(f"Lines: {dna_input.count(chr(10)) + 1}")
    else:
        st.warning("⚠️ Awaiting DNA Code Input")

# Process and generate PDF
st.markdown("---")
col_process, col_export = st.columns(2)

with col_process:
    if st.button("🔄 Process DNA Code", key="process_btn", use_container_width=True):
        if dna_input:
            st.success("DNA code processed successfully!")
        else:
            st.error("Please paste DNA code first")

with col_export:
    if st.button("📥 Generate HD PDF", key="pdf_btn", use_container_width=True):
        if dna_input:
            # Create PDF
            pdf = FPDF()
            pdf.add_page()
            
            # Set font and styling
            pdf.set_font("Arial", "B", 16)
            pdf.cell(0, 10, "Integrated Warrior DNA Code", ln=True, align="C")
            
            pdf.set_font("Arial", "I", 10)
            pdf.cell(0, 10, f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", ln=True, align="C")
            if author_name:
                pdf.cell(0, 10, f"Author: {author_name}", ln=True, align="C")
            
            pdf.ln(5)
            pdf.set_font("Arial", "", 11)
            
            # Add DNA code with word wrapping
            pdf.multi_cell(0, 5, dna_input)
            
            # Generate downloadable PDF
            pdf_bytes = pdf.output()
            
            st.download_button(
                label="📥 Download HD PDF",
                data=pdf_bytes,
                file_name=f"DNA_Code_{datetime.now().strftime('%Y%m%d_%H%M%S')}.pdf",
                mime="application/pdf",
                key="download_btn",
                use_container_width=True
            )
            st.success("✓ PDF generated and ready for download!")
        else:
            st.error("Please paste DNA code first")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray; font-size: 12px;'>
    <p>🚀 Copy-Paste Tab | DNA Code → PDF Export | Streamlit Powered</p>
    <p>Share instantly via email or text • Export to any project</p>
    </div>
    """,
    unsafe_allow_html=True
)