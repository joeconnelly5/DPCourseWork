# Load dependencies
# ---------------------------------------------#
import pandas as pd
import geopy as gp
# ------------------------------------------------------------------------ #
# Define Functions
# ------------------------------------------------------------------------ #

# location_mobility_data


def location_mobility_data(longitude, latitude):
    # Load the data
    mobility_df = pd.read_csv("CoronaData.csv", encoding="utf-8")
    # Geocode the longitude/latitude data if not provided with country
    ## Initialize the geocoder
    locator = gp.geocoders.Nominatim(user_agent="myGeocoder")
    ## Reverse geocode (longitude, latitude > country)
    coordinates = str(latitude) + ", " + str(longitude)
    geocode_data = locator.reverse(coordinates)
    country = geocode_data.raw['address']['country']
    ## Extract data for country
    mobility_location_df = mobility_df[mobility_df["Region"]==country]
    ## Extract data for walking & calculate change in # of walking calls
    walking = mobility_location_df[mobility_location_df["Transportation"] == "walking"]
    walking_chg = 1 - walking["Requests_4/14/2020"]/walking["Requests_1/13/2020"]
    walking_chg = int(walking_chg*100)
    ## Extract data for driving & calculate change in # of driving calls
    driving = mobility_location_df[mobility_location_df["Transportation"] == "driving"]
    driving_chg = 1 - driving["Requests_4/14/2020"]/driving["Requests_1/13/2020"]
    driving_chg = int(driving_chg*100)
    # Return the results
    return([country, walking_chg, driving_chg])

