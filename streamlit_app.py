import streamlit as st

def main():
    st.title("WELCOME TO")
    
    if st.button("BUTONA TIKLA"):
        st.header("AMCA BENİ AFFET".upper())
        st.balloons()
        st.success("AMCAAAAAAAAAAAA BOĞULUYORUMMMMMMMM")
        st.error("AMCAAA BANA BAKLAVA VEEEEER")
        imgurl='https://www.baktad.org.tr/wp-content/uploads/2021/02/cengizbayindir.jpg'
        st.image(imgurl, caption='Örnek Resim', width=600)
        imgurl2='https://media.licdn.com/dms/image/D4D03AQGGRw7tt3ncmQ/profile-displayphoto-shrink_800_800/0/1689504553913?e=2147483647&v=beta&t=EEW2IQkxhDk3OiICB1LtEEHfQyJz8Jl9VbmcnGzziLw'
        st.image(imgurl2,width=600)
if __name__ == "__main__":
    main()
