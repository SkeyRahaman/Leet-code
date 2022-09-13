class Codec:
    def __init__(self):
        self.data_encode = {}
        self.data_decode = {}
        self.url = "http://shakib.com/"
        Codec.count = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.data_encode:
            c = Codec.count
            Codec.count += 1
            self.data_encode[longUrl] = c
            self.data_decode[c] = longUrl
            return self.url + str(c)
        else:
            return self.url + self.data_encode[longUrl]
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.data_decode[int(shortUrl[18:])]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))