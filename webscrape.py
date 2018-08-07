"""
Webscraper
----------

Template for web-scraping PDF documents.
UC Berkeley's EECS70 Notes is given as an example.

Author
------
Beom Jin Lee <cluesbj@berkeley.edu>
"""

import requests
import os
import logging


def download_file(download_url, output_directory, prefix="note", file_type=".pdf"):
    if not os.path.exists(output_directory):
        os.makedirs(output_directory)

    output_name = output_directory + prefix + file_type

    logging.info("Downloading from ", download_url)

    response = requests.get(download_url, stream=True)
    file = open(output_name, 'wb')
    file.write(response.content)
    file.close()

    logging.info("Completed Downloading")


def main():
    for i in range(1, 27):
        prefix = "note" + str(i)
        download_file("http://www.eecs70.org/static/notes/n{}.pdf".format(i),
                      "/Users/beomjin_lee/Desktop/cs70/", prefix, file_type=".pdf")


if __name__ == "__main__":
    main()
