import streamlit as st

def main():
    st.title("WELCOME TO")
    
    if st.button("BUTONA TIKLA"):
        st.write("AMCA BENİ AFFET".upper())
        st.balloons()

if __name__ == "__main__":
    main()
