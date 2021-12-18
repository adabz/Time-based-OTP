### Time-Based OTP Code generator 
The script toter.py is a Time-based One-time code generator, it will either generate a QRCode image in terminal (saved
as a png file in same directory). it can retreive OTP code similar to Google Authenticator at a given time.

##  Requirements
- Python 3.6+
- QRcode (installed using: sudo pip3 install qrcode)

## Usage

To use the program there are two modes of operation, one to generate a QRcode displaying it in terminal, saving it as a png in the same directory, or it will print current OTP code.

to generate a QRcode type the following:
>$ python3 totp.py --qr
>
>
>![QRcode](qrcode.png)
>                                                   
>                                                 
> qrcode.png saved in same directory


a QRcode image will be printed in the terminal as well as saved as a png file named qrcode.png, in current running dir.
to obtain current OTP code type:
> $ python3 totp.py --get-otp
>
> One-time passcode is: 313828
> ....


