from streamlit import *
import qrcode

set_page_config("qrcode_app")
write("Welcome in qrcode genrator")
a=text_area("Enter your grade level and enter your name and your phone number:")



if button("genrate"):
    img=qrcode.make(a)
    img.save("qr.ico")
    

    image("qr.ico",caption="qrcode")