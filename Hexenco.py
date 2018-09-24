#!/usr/bin/python
print """
TEXT To HEX Encode
Coded : VanGans
Gretz : AnarchoXploit
"""
a = raw_input ('Masukkan Text = ').rstrip()
def hexcape(stri):
   f = ""
   for x in stri:
      f += "\\x"+x.encode('hex')
   return f
print(hexcape(a))
