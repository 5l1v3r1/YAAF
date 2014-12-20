from time import gmtime, strftime
import os, pwd

results = []
home_dir = pwd.getpwuid(os.getuid()).pw_dir + "/"
output_dir = home_dir + ".yaaf_output"

def current_time():
    return strftime("%H%M%S_%d%m%Y", gmtime())

def check_logs():
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

def display_results():
    print("\nResults:\n")
    for re in results:
        print(re)
    print("\n")

def save_results():
    with open(output_dir+"/"+current_time(), 'w') as log_file:
        log_file.writelines(results)

def sanitize_link(link_to_parse):

    if "https://" in link_to_parse:
        link_to_parse = link_to_parse.replace("https://", "")
    elif "http://" in link_to_parse:
        link_to_parse = link_to_parse.replace("http://", "")

    if link_to_parse[::-1][0] == '/':
        link_to_parse = link_to_parse.rstrip('/')

    if link_to_parse[:4] == "www.":
        return link_to_parse[4:]
    else:
        return link_to_parse
