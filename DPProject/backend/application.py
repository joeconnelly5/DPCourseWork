# ------------------------------------------------------------------------ #
# Initialization
# ------------------------------------------------------------------------ #
# Load external dependencies
# ---------------------------------------------#
import flask

# Initialize the flask application
# ---------------------------------------------#
application = flask.Flask(__name__, 
    template_folder = 'C:/Users/joeco/DPCourseWork/DPProject/frontend', 
    static_folder = 'C:/Users/joeco/DPCourseWork/DPProject/frontend')

# Load internal dependencies
# ---------------------------------------------#
import sys
sys.path.append('backend')
import dataprocessing as dp

# ------------------------------------------------------------------------ #
# Test Functions
# ------------------------------------------------------------------------ #

## Note: Try with US, Germany, UK
for i in [[-71.08328259999999, 42.3662154],[10.48328259999999, 51.3662154],[-1.78328259999999, 52.4662154]]:
    try:
        lon = i[0]
        lat = i[1]
        data = dp.location_mobility_data(longitude = lon, latitude = lat)
        print("Country name: ", data[0])
        print("Decrease in # of walking calls (%): " + str(data[1]))
        print("Decrease in # of driving calls (%): " + str(data[2]))
    except:
        print("Country not found.")

# ------------------------------------------------------------------------ #
# Define views
# ------------------------------------------------------------------------ #

# home
# ---------------------------------------------#
@application.route('/home')
def home_view():

    # Render the home page
    return flask.render_template('index.html')

# update_country
# ---------------------------------------------#
@application.route('/update_country')
def update_country_view():

    # Extract the data received from frontend
    long = flask.request.args.get('longitude')
    lat  = flask.request.args.get('latitude')

    # Retrieve the location-specific data
    location_data = dp.location_mobility_data(longitude = long, latitude = lat)

    # Pass the data to the home page & updated page
    return flask.jsonify({"Country":location_data[0], "WalkingDecrease":location_data[1], 
        "DrivingDecrease":location_data[2]})

application.run()