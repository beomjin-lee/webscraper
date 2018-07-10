"""
Webscraper
----------

Template for web-scraping PDF documentsself.
UC Berkeley's EECS70 Notes is given as an example.

Author
------
Beom Jin Lee <cluesbj@berkeley.edu>
"""

import requests


def download_file(download_url, output_path):
    print("Downloading from ", download_url)
    response = requests.get(download_url, stream=True)
    file = open(output_path, 'wb')
    file.write(response.content)
    file.close()
    print("Completed Downloading")


def main():
    for i in range(1, 27):
        download_file("http://www.eecs70.org/static/notes/n{}.pdf".format(i),
                      "~/Desktop/cs70/note{}.pdf".format(i))


if __name__ == "__main__":
    main()
