"""
A very simple Base64 encoder/decoder in Python for learning purposes
"""

"""
"THE BEER-WARE LICENSE" (Revision 42):
zmey20000@yahoo.com wrote this file. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return Mikhail Zakharov
"""


class Base64:
    BASE64_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'

    def encode(self, dec):
        enc = ''
        length = len(dec)
        for tptn in range(0, length, 3):
            # Input octets
            ot0 = ord(dec[tptn])
            ot1 = ord(dec[tptn + 1]) if tptn + 1 <= length - 1 else 0
            ot2 = ord(dec[tptn + 2]) if tptn + 2 <= length - 1 else 0
            # Output sextets
            st0 = self.BASE64_ALPHABET[ot0 >> 2]
            st1 = self.BASE64_ALPHABET[(ot0 & 0x3) << 4 | ot1 >> 4]
            st2 = '=' if not ot1 else self.BASE64_ALPHABET[(ot1 & 0xF) << 2 | ot2 >> 6]
            st3 = '=' if not ot2 else self.BASE64_ALPHABET[ot2 & 0x3F]

            enc += st0 + st1 + st2 + st3

        return enc

    def decode(self, enc):
        dec = ''
        length = len(enc)
        for qttn in range(0, length, 4):
            # Input sextets
            st0 = self.BASE64_ALPHABET.index(enc[qttn])
            st1 = self.BASE64_ALPHABET.index(enc[qttn + 1])
            st2 = self.BASE64_ALPHABET.index(enc[qttn + 2]) if enc[qttn + 2] != '=' else 0
            st3 = self.BASE64_ALPHABET.index(enc[qttn + 3]) if enc[qttn + 3] != '=' else 0
            # Output octets
            ot0 = chr(st0 << 2 | st1 >> 4)
            ot1 = chr((st1 & 0xF) << 4 | st2 >> 2) if st2 else ''
            ot2 = chr((st2 & 0x3) << 6 | (st3 & 0x3F)) if st3 else ''

            dec += ot0 + ot1 + ot2

        return dec


if __name__ == '__main__':
    pass
