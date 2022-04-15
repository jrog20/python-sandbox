# Sites: pysical locations found on a map => ID, address
# Projects: things that have been done at a site => ID, start date, end date
# Meters: devices that measure energy usage at a site => 
#   ID, start datetime, end datetime, type of meter (electricity or gas), unit (kwh or therm), 
#   and value (typically associated w/a site)

##########################################################
# from datetime import datetime, timedelta

# my_datetime_str = '1/1/2017'
# parsed_date = datetime.strptime(my_datetime_str, "%m/%d/%Y")
# formatted_date = parsed_date.strftime('%Y%m%d %H:%M:%S')

# plus_one_day = timedelta(days=1)
# date_plus_one = parsed_date + plus_one_day
# formatted_date_plus_one = date_plus_one.strftime('%Y%m%d %H:%M:%S')

##########################################################
#
# Complete the 'parse_for_platform' function below.
#
# The function takes a list of dictionaries and is
# expected to return 3 lists of dictionaries.
# 
# See the problem description for additional notes.
#
##########################################################
# FINAL SUBMISSION
#!/bin/python3

import math
import os
import random
import re
import sys
from io import StringIO
import csv
from datetime import datetime, timedelta

def make_row(line):
    project_name, project_date, street, city, zipcode, read_from, read_to, amount, meter_number = line.split(",")
    return {
        "project_name": project_name,
        "project_date": project_date,
        "street": street,
        "city": city,
        "zipcode": zipcode,
        "read_from": read_from,
        "read_to": read_to,
        "amount": amount,
        "meter_number": meter_number,
    }

def parse_for_platform(raw_ami_data):
    sites = []
    projects = []
    meters = []
    
    lines_of_data = raw_ami_data.split("|")

    for line in lines_of_data:
        row = make_row(line)

        sites = [
            {
                "site_id": row["meter_number"],
                "raw_address": row["street"] + " " + row["city"] + " CA " + row["zipcode"],
            },
        ]
        
        projects = [
            {
               "project_id": row["project_name"],
               "blackout_start_date": datetime.strptime(row["project_date"], "%m/%d/%y").strftime('%Y-%m-%dT%H:%M:%S'),
               "intervention_active_date": datetime.strptime(row["project_date"], "%m/%d/%y").strftime('%Y-%m-%dT%H:%M:%S'),
                # ERROR - NEED TO USE site_id generated in the site spec above
               "project_site": sites[0]['site_id'],
            },
        ]
        
        meters = [
            {
                "meter_id": row["meter_number"],
                # ERROR - NEED TO USE site_id generated in the site spec above
                "meter_site": sites[0]['site_id'],
                "type": "gas" if row["meter_number"].startswith('G') else "electricity",
                "unit": "therm" if "type" == "gas" else "kwh",
                "start": datetime.strptime(row["read_from"], "%m/%d/%y").strftime('%Y%m%d %H:%M:%S'),
                "end": datetime.strptime(row["read_to"], "%m/%d/%y").strftime('%Y%m%d %H:%M:%S'),
                "value": row["amount"],
            },
        ]
        
    return sites, projects, meters

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    raw_ami_data = input()

    sites, projects, meters = parse_for_platform(raw_ami_data)
    
    site_out = StringIO()
    site_writer = csv.DictWriter(site_out, [
        "site_id",
        "raw_address",
    ])
    for site in sites:
        site_writer.writerow(site)
    
    proj_out = StringIO()
    project_writer = csv.DictWriter(proj_out, [
        "project_id",
        "blackout_start_date",
        "intervention_active_date",
        "project_site",
    ])
    for project in projects:
        project_writer.writerow(project)
    
    meter_out = StringIO()
    meter_writer = csv.DictWriter(meter_out, [
        "meter_id",
        "meter_site",
        "type",
        "unit",
        "start",
        "end",
        "value",
    ])

    for meter in meters:
        meter_writer.writerow(meter)
    
    fptr.write(site_out.getvalue())
    fptr.write(proj_out.getvalue())
    fptr.write(meter_out.getvalue())

    fptr.close()
