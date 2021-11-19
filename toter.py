#!/usr/bin/python3

import sys, time, struct, hmac
from qrcode import QRCode
from hashlib import sha1
from base64 import b32decode

secret = "NBSXSIDIMV4SA2DFPF4SCCQ=" # "hey hey heyy!"
uri = "otpauth://totp/Test:User1?secret="+ secret + "&issuer=Orgnization&digits=00&type=totp&period=30"

# create a QRCode image based on uri and save it to a png file
def make_qr_code(string):
  qr = QRCode(version=1,box_size=10,border=5)
  qr.add_data(string)
  qr.make(fit=True)
  qr.print_ascii()
  img = qr.make_image(fill='black', back_color='white')
  img.save('qrcode.png')
  print("qrcode.png saved in same directory")

# hash one-time based token generation
def hotp_token(secret, interval):
    key = b32decode(secret, True)
    msg = struct.pack(">Q", interval)

    hash = hmac.new(key, msg, sha1).digest()
    hash_bits = hash_bits = hash[19] & 15

    hash = (struct.unpack(">I", hash[hash_bits:hash_bits+4])[0] & 0x7fffffff) % 1000000
    return hash

def get_totp(secret):
    seconds = 30
    interval = int(time.time()) // seconds
    token = str( hotp_token(secret, interval ) )

    tok_len = len(token)
    repeat = 0
    if tok_len != 6:
       repeat = 6 - tok_len
    char = "0"

    # insert zeros in the beginning if token is less than 6 digits
    token = "" + (char*repeat) + token

    return token

def main():
  args = sys.argv[1:]

  if len(args) != 1:
    print("please type in one of the following options:\n")
    print("\t","--qr", "\t\t", "to generate a QR image of OTP info")
    print("\t","--otp", "\t\t", "to obtain current OTP code\n\n")
    return
  elif args[0] == "--qr":
    make_qr_code(uri)
    return
  elif args[0] == "--otp":
    print("One-time passcode is:", get_totp(secret))
    print("Differences between Google Authenticator and current OTP are due to time sync on current host")
    return
  else:
    return

if __name__ == "__main__":
   main()
