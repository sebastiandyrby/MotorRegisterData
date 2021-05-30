# MotorRegisterData
Repository including all coding and data used for my master's thesis on the impact of the Danish car registration tax. 

# Files included
1. JavaScript-file for parsing of the large XML file of the Danish Register of Motor Vehicles (_xmlstream.js_, dependencies described in _dependencies.txt_). Code for compilation is included (.
2. Webscraper used for scraping prices and technical characteristics from Bilbasen.dk.
3. Raw-data in JSON-format compiled from the parsing.
4. Scraped dataset including prices and various technical characteristics.

# The XML parser
JavaScript for parsing XML file extracted from the Danish Central Motor Register, extracting specific nodes.
See dependencies.txt for relevant dependecies required for the xml-stream.
Output is a JSON-file containing an array with the specific nodes.

Can be compiled using the included compilation code. 

# Use of the dataset
The data is free to use for further research or other projects. 
