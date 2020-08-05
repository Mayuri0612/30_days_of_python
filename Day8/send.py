import sys
import requests
from formatting import format_msg #internal importing
from datetime import datetime #builtin importing

def send(name, website=None, verbose=False):
    if website != None:
        msg = format_msg(my_name=name, my_website = website)
    else:
        msg = format_msg(my_name=name)
    if verbose:
        print(name,website)
    r = requests.get("http://httpbin.org/json")
    if r.status_code == 200:
        return r.json()
    else:
        return ("There was Error!!")

if __name__ == "__main__":
    print(sys.argv)
    name = "Unknown"
    if len(sys.argv) > 1:
        name = sys.argv[3]
    response = send("MK", verbose=True)
    print(response)