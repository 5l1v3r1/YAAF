import threading
import multiprocessing
import queue
import http.client
import sys

from funcs import aux_functs
from funcs.colors import TermColors

i = 1
user_agent = {'User-Agent': ''}
word_queue = queue.Queue()

def check_link(response_status, link, word):

    global i
    i += 1
    possible_link = [301, 302]

    if response_status == 404:
            return "www.{}/{} - {} - Not found.".format(link, word, response_status)
    elif response_status in possible_link:
            return "{}www.{}/{} - {} - Possible page.{}".format(TermColors.YELLOW, link, word, response_status,
                                                                TermColors.ENDC)
    elif response_status == 200:
            aux_functs.results.append("www.{}/{} - {} - Found.".format(link, word, response_status))
            return "{}www.{}/{} - {} - Found.{}".format(TermColors.GREEN, link, word, response_status, TermColors.ENDC)
    else:
            return "www.{}/{} - {} - Not Identified.".format(link, word, response_status)

def find_admin(website, nr_words, no_output=True, extension="", sanitize=False, u_agent=""):

    if sanitize:
        website = aux_functs.sanitize_link(website)

    user_agent['User-Agent'] = u_agent

    if no_output:

        while True:
            item = word_queue.get()

            try:
                _connection = http.client.HTTPConnection(website)
                _connection.request("GET", "/" + item + extension, headers=user_agent)

                response = _connection.getresponse()
            except Exception as e:
                word_queue.task_done()
                print("Exception: {} \nCtrl-C to exit.".format(e))
                sys.exit(0)

            check_link(response.status, website, item+extension)
            word_queue.task_done()

    elif not no_output:

        while True:
            item = word_queue.get()

            try:
                _connection = http.client.HTTPConnection(website)
                _connection.request("GET", "/" + item + extension, headers=user_agent)

                response = _connection.getresponse()
            except Exception as e:
                word_queue.task_done()
                print("Exception: {} \nCtrl-C me pls".format(e))
                sys.exit(0)

            print("[{}/{}] {}".format(i, nr_words, check_link(response.status, website, item+extension)))
            word_queue.task_done()

def start_threads(website, word_list, num_threads=multiprocessing.cpu_count(), log_res=False, output=True, extension="",
                  sanitize=False, u_agent=""):

    aux_functs.check_logs()
    print("Loading wordlist...\n")
    with open(word_list, 'r') as w_file:
        content = w_file.read().splitlines()

    for word in content:
        word_queue.put(word)

    for f in range(num_threads):
        t = threading.Thread(target=find_admin, args=(website,len(content),output,extension, sanitize, u_agent))
        t.daemon = True
        t.start()

    try:
        word_queue.join()
        if len(aux_functs.results) >= 1:
            if log_res:
                aux_functs.save_results()
            aux_functs.display_results()
        else:
            if log_res:
                print("No results to print to file.")
            else:
                print("\nNo results.\n")
    except KeyboardInterrupt:
        print("\nTask interrupted.")
