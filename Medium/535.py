class Codec:
    def __init__(self):
        self.encode_table = {}
        self.decode_table = {}
        self.base_url = "http://www.sheepurl.com/"

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.

        :type longUrl: str
        :rtype: str
        """
        if longUrl not in self.encode_table:
            shortUrl = self.base_url + str(len(self.encode_table) + 1)
            self.encode_table[longUrl] = shortUrl
            self.decode_table[shortUrl] = longUrl
        return self.encode_table[longUrl]

    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.

        :type shortUrl: str
        :rtype: str
        """
        return self.decode_table[shortUrl]


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
