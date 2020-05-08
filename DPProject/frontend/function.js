// Defining functions
// ---------

// InitializeGraph
function InitializeGraph() {

  // Make a client-side API call to obtain the user's location
  $.getJSON("http://ip-api.com/json", function (data, status) {

    // Inspect the data returned from the API
    console.log(data)

    // Extract the user's longitude and latitude from the data that the API returns
    user_longitude = data.lon;
    user_latitude  = data.lat;

    // Log the longitude and latitude to the console
    console.log("Longitude: " + user_longitude)
    console.log("Latitude: " + user_latitude)
     
    // Update the interface the user sees with their location
    document.getElementById("location").innerHTML = "Your location:<br> Latitude: " + user_latitude + "<br>Longitude: " + user_longitude;
  
    // Draw the graph
    // ** Note: Data is hard-coded > next step: Replace hard-coded data with an API call to the server, i.e., backend 
    // ** API call specification: Send to server: Longitude, latitude / Receive from server: Corresponding country, decrease in walking direction requests, decrease in driving direction requests
    // Make API call to backend & draw graph
    $.getJSON("/update_country", {longitude: user_longitude, latitude:user_latitude}, 
    function (data, status) {

    // Inspect the data returned from the API
      console.log(data)

      // Draw graph
      DrawGraph(data.Country,data.WalkingDecrease, data.DrivingDecrease);
    }
    )


  })
}

// DrawGraph
google.charts.load('current', {packages: ['corechart', 'bar']});

function DrawGraph(country, walkingdecrease, drivingdecrease) {

  // Generate and format the data
  var data = google.visualization.arrayToDataTable([
    ['Country', 'WalkingDecrease', 'DrivingDecrease'],
    [country, walkingdecrease, drivingdecrease]
  ]);

  // Customize the graph
  var options = {
    colors: ['#b0120a', '#ffab91'],
    chartArea: {width: '50%'},
    hAxis: {
      title: '% decrease in the number of walking and driving direction requests'
    }
  };

  // Generate the graph
  var chart = new google.visualization.BarChart(document.getElementById('chart'));

  // Display the graph
  chart.draw(data, options);

}



