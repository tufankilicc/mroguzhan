import streamlit as st

def main():
    st.title("WELCOME TO")
    
    if st.button("BUTONA TIKLA"):
        st.header("AMCA BENİ AFFET".upper())
        st.balloons()
        st.success("AMCAAAAAAAAAAAA BOĞULUYORUMMMMMMMM")
        st.error("AMCAAA BANA BAKLAVA VEEEEER")
        imgurl='https://www.baktad.org.tr/wp-content/uploads/2021/02/cengizbayindir.jpg'
        st.image(imgurl, caption='Örnek Resim', use_column_width=True)

if __name__ == "__main__":
    main()
