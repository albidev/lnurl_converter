#!/usr/bin/env python3

import bech32

class LNURLConverter: 
    
    input = ''
    output = ''

    def islnurl(self, input):
        s = input.lower()
        if ':' in s:
            s = s.split(':')[1]
        return s[:6] == 'lnurl1'

    def parse(self, input):
        self.input = input
        if self.islnurl(input):
            self.output = self.decode(input)
        else:
            self.output = self.encode(input)
        return self.output

    def decode(self, lnurl):
        _, data = bech32.bech32_decode(lnurl)
        decoded_data = bech32.convertbits(data, 5, 8, False)
        url = bytearray(decoded_data).decode('utf-8')
        return url 
    
    def encode(self, url):
        words = bech32.convertbits(list(url.encode()), 8, 5)
        return bech32.bech32_encode('lnurl', words)

if __name__ == '__main__':
    url = 'https://service.com/api?q=3fc3645b439ce8e7f2553a69e5267081d96dcd340693afabe04be7b0ccd178df'
    conv = LNURLConverter()
    output = conv.parse(url)
    print(output)
    ret = conv.parse(output)
    print(ret)

    if url == ret:
        print('OK')