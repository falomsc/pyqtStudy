import urllib.request
import urllib.parse
import string

def get_method_params():
    url = "http://www.baidu.com/s?wd="
    name = "美女"
    final_url = url+name
    print(final_url)
    encode_new_url = urllib.parse.quote(final_url, safe=string.printable)
    response = urllib.request.urlopen(encode_new_url)
    print(response)
    data = response.read().decode()
    print((data))
    with open("02-encode.html", "w", encoding = "utf-8") as f:
        f.write(data)

get_method_params()