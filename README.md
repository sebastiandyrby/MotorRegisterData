# MotorRegisterData
Repository including all coding and data used for my master's thesis on the impact of the Danish car registration tax. 

The register data can be downloaded from:
https://data.virk.dk/datakatalog/skat/koeretoejsdata

# Files included
1. JavaScript-file for parsing of the large XML file of the Danish Register of Motor Vehicles (_xmlstream.js_, dependencies described in _dependencies.txt_). Code for compiling parsed data is included, although not well written, but it does the trick (_motorreg_read.py_).
2. Webscraper used for scraping prices and technical characteristics from Bilbasen.dk (_bilbasen_scrape.py_).
3. Dataset used in the analysis is included. For the raw dataset in csv-format or JSON-format, please feel free to contact me - it was to big to upload here.
4. Scraped dataset including prices and various technical characteristics (_bilbasen_scrape.csv_).

# The XML parser
JavaScript for parsing XML file extracted from the Danish Central Motor Register, extracting specific nodes.
See dependencies.txt for relevant dependecies required for the xml-stream.
Output is a JSON-file containing an array with the specific nodes.

Can be compiled using the included compilation code. 

# Use of the dataset
The data is free to use for further research or other projects. 
