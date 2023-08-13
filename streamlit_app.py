import streamlit as st

def main():
    st.title("WELCOME TO")
    
    if st.button("BUTONA TIKLA"):
        st.header("AMCA BENİ AFFET".upper())
        st.balloons()
        st.success("AMCAAAAAAAAAAAA BOĞULUYORUMMMMMMMM")
        st.error("AMCAAA BANA BAKLAVA VEEEEER")

if __name__ == "__main__":
    main()
