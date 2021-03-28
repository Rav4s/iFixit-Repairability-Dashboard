# iFixit-Repairability-Dashboard

Pulls repairability scores for various devices from iFixit, which are then displayed on a website in a few categories.

## What does each file do?

The scraper.py file scrapes iFixit's webpages at https://www.ifixit.com/smartphone-repairability, https://www.ifixit.com/laptop-repairability, and https://www.ifixit.com/tablet-repairability. It then takes the html and parses it to find three fields for each device:  Manufacturer, Device Model, and Repairability Score. The data for these three fields is then written to one of three csv files (laptop.csv, smartphone.csv, and tablet.csv) based on the device type.

Once these files are stored, you can run Web_Dashboard/app.py, which starts a waitress server that serves webpages for each repairability score. The webpage templates are located in the Web_Dashboard/templates directory and the stylesheets are located in the Web_Dashboard/static directory. The webserver will be accessible at 0.0.0.0:1235.

## Live Demo

A live demo of this project is available at https://repairability.yeetpc.com

Note: this project is neither sponsored by nor affiliated with iFixit.
