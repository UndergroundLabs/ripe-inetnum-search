# RIPE Inetnum Search

I created this script to search the RIPE database for IP ranges for a given search term, and output the results in the terminal. This is useful for piping into other programs such as NMAP.

## Installation

Ensure the following packages are installed:

    pip install netaddr
    pip install requests

Clone the repo:

    git clone git@github.com:UndergroundLabs/ripe-inetnum-search.git

(Optional) Move to `/usr/local/bin`:

    cd ripe-inetnum-search
    mv inetnum.py /usr/local/bin/inetnum
    inetnum facebook

## Usage

    cd ripe-inetnum-search
    ./inetnum.py facebook

Results:

    159.255.222.40/29
    193.240.159.104/29
    212.187.194.160/28
    212.187.196.96/28

