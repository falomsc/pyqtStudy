import urllib.request
import urllib.parse
import string

def get_params():
    url = "http://www.baidu.com/s?wd="

    params = {
        "wd":"中文",
        "key":"zhang",
        "value":"san"

    }
    str_params = urllib.parse.urlencode(params)
    final_url = url + str_params

    end_url = urllib.parse.quote(final_url, safe=string.printable)

    response = urllib.request.urlopen(end_url)
    data = response.read().decode("utf-8")
    print(data)


get_params()