import argparse
from .funcs import threads

def main_function():

    parse = argparse.ArgumentParser(description="Description here")

    parse.add_argument("-u", "--url=", action="store", dest="URL", help="Website url")
    parse.add_argument("-t", "--threads=", action="store", dest="NUMBER", help="Number of threads to use")
    parse.add_argument("-w", "--wordlist=", action="store", dest="NAME", help="Wordlist to use")
    parse.add_argument("-e", "--ext=", action="store", dest="EXT", help="Wordlist to use")
    parse.add_argument("-no", "--no-output", action="store_true", dest="NO_OUTPUT", help="If outputs every try")
    parse.add_argument("-l", "--log", action="store_true", help="Saves the results to a file")
    parse.add_argument("-ua", "--user-agent=", action="store", dest="UAGENT", help="Custom user-agent")
    parse.add_argument("-s", "--sanitize", action="store_true", help="Sanitizes the url given")

    parsed_args = parse.parse_args()

    if parsed_args.URL and parsed_args.NAME and not parsed_args.EXT and not parsed_args.UAGENT:
        if parsed_args.NUMBER:
            if  1 <= int(parsed_args.NUMBER) <= 10:
                threads.start_threads(parsed_args.URL, parsed_args.NAME, num_threads=int(parsed_args.NUMBER),
                              log_res=parsed_args.log, output=parsed_args.NO_OUTPUT, sanitize=parsed_args.sanitize)
            else:
                print("Number of threads must be between 1 and 10.")
        else:
            threads.start_threads(parsed_args.URL, parsed_args.NAME, log_res=parsed_args.log, output=parsed_args.NO_OUTPUT,
                          sanitize=parsed_args.sanitize)

    elif parsed_args.URL and parsed_args.NAME and parsed_args.EXT and not parsed_args.UAGENT:
        if parsed_args.NUMBER:
            if  1 <= int(parsed_args.NUMBER) <= 10:
                threads.start_threads(parsed_args.URL, parsed_args.NAME, num_threads=int(parsed_args.NUMBER),
                              log_res=parsed_args.log, output=parsed_args.NO_OUTPUT, extension=parsed_args.EXT,
                              sanitize=parsed_args.sanitize)
            else:
                print("Number of threads must be between 1 and 10.")
        else:
            threads.start_threads(parsed_args.URL, parsed_args.NAME, log_res=parsed_args.log, output=parsed_args.NO_OUTPUT,
                          extension=parsed_args.EXT, sanitize=parsed_args.sanitize)

    elif parsed_args.URL and parsed_args.NAME and not parsed_args.EXT and parsed_args.UAGENT:
        if parsed_args.NUMBER:
            if  1 <= int(parsed_args.NUMBER) <= 10:
                threads.start_threads(parsed_args.URL, parsed_args.NAME, num_threads=int(parsed_args.NUMBER),
                              log_res=parsed_args.log, output=parsed_args.NO_OUTPUT, u_agent=parsed_args.UAGENT,
                              sanitize=parsed_args.sanitize)
            else:
                print("Number of threads must be between 1 and 10.")
        else:
            threads.start_threads(parsed_args.URL, parsed_args.NAME, log_res=parsed_args.log, output=parsed_args.NO_OUTPUT,
                          sanitize=parsed_args.sanitize)

    elif parsed_args.URL and parsed_args.NAME and parsed_args.EXT and parsed_args.UAGENT:
        if parsed_args.NUMBER:
            if  1 <= int(parsed_args.NUMBER) <= 10:
                threads.start_threads(parsed_args.URL, parsed_args.NAME, num_threads=int(parsed_args.NUMBER),
                              log_res=parsed_args.log, output=parsed_args.NO_OUTPUT, extension=parsed_args.EXT,
                              u_agent=parsed_args.UAGENT, sanitize=parsed_args.sanitize)
            else:
                print("Number of threads must be between 1 and 10.")
        else:
            threads.start_threads(parsed_args.URL, parsed_args.NAME, log_res=parsed_args.log, output=parsed_args.NO_OUTPUT,
                          extension=parsed_args.EXT, u_agent=parsed_args.UAGENT, sanitize=parsed_args.sanitize)
    else:
        print("URL and WordList are mandatory.")
