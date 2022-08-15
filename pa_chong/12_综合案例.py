import requests
from Crypto.Cipher import AES
from base64 import b64encode
import json
url = "https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

params = {
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "1",
    "pageSize": "20",
    "rid": "R_SO_4_1968781675",
    "threadId": "R_SO_4_1968781675"
}
# i "BBK4o9dTOijGvtBb"
# key "d4c23844685428dd7939c3c74cd1314a085b33a367979bd4c6af93fc42805cd227518c68dc902d63fd759bbf3a76b6c05b95a9edc0257dd669962e8941c09532c975a10411ba2804e251e3521d53f33dcd78574b75db4b21175a9763da6cb27eaeaa8a9f099ef711fc5befd42c2582ca41974f321fa7fbe53b5a071e53bba4b7"
# e, f, g 对应以下的值
# buV2x(["流泪", "强"]) => 010001 = e
# buV2x(["爱心", "女孩", "惊恐", "大笑"]) => 0CoJUm6Qyw8W8jud = g
# buV2x(Rg8Y.md) = f
# 00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7
"""
function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g), h.encText = b(h.encText, i), h.encSecKey = c(i, e, f), h
    }
    function e(a, b, d, e) {
        var f = {};
        return f.encText = c(a + e, b, d),
        f
    }
    window.asrsea = d,
    
    encText = params
    encSecKey = encSecKey
"""

i = "BBK4o9dTOijGvtBb"
enc_key = "d4c23844685428dd7939c3c74cd1314a085b33a367979bd4c6af93fc42805cd227518c68dc902d63fd759bbf3a76b6c05b95a9edc0257dd669962e8941c09532c975a10411ba2804e251e3521d53f33dcd78574b75db4b21175a9763da6cb27eaeaa8a9f099ef711fc5befd42c2582ca41974f321fa7fbe53b5a071e53bba4b7"
e = "010001"
g = "0CoJUm6Qyw8W8jud"
f = "00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"


def to_16(data):
    pat = 16 - len(data) % 16
    data += chr(pat) * pat
    return data


def enc_params(data, key):
    iv = "0102030405060708"
    data = to_16(data)
    aes = AES.new(key=key.encode("utf-8"), iv=iv.encode("utf-8"), mode=AES.MODE_CBC)
    bs = aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs), "utf-8")


def get_params(data):
    enc_a = enc_params(data, g)
    res = enc_params(enc_a, i)
    return res


page_res = requests.post(url, data={
    "params": get_params(json.dumps(params)),
    "encSecKey": enc_key
})

print(page_res.json())
