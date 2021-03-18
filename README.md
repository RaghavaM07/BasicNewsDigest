# Basic News Digest
This is a very basic web scraping project that scraps 4 news websites and returns top/trending news headlines and their links.

## Websites Scraped
The program scraps:
* indiatoday.in
* thehindu.com
* bbc.com
* aljazeera.com

## Requirements
The requirements needed to run the dash.py are provided in the `requirements.txt` file.
They are:
* colorama → For colored text in the terminal
* requests → To send/recieve HTTP requests
* bs4 → For scraping the page source obtained from `requests.get()`
* lxml → To parse the page source

To install the requirements run:
### Linux/Mac:
`pip3 install -r requirements.txt`
### Windows:
`pip install -r requirements.txt`

Cheers! Have a nice day!!

#### Note
This project was only made to practice web scraping. I'm still learning things...
