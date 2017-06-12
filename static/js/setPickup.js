var selectedDriver = null;
    window.onload = function() {
        $('#requestLyft').modal();
        $('#waitingDriver').modal();
    }

    $(document).ready(function(){
        $("#from").change(function(){
            if ($(this).val() == '') {
                $(this).val() = 'IES Francesc Borja Moll, Illes Balears'
            }
            initMap();
        });
        $("#destination").change(function(){
            initMap();
        });
    });

    $('#chat-button').click(function(){
        $('#chat-content').css("z-index", "11");
        $('#profile-content').css("z-index", "8");
    });
    $('#profile-button').click(function(){
        $('#profile-content').css("z-index", "11");
        $('#chat-content').css("z-index", "8");
    });
    $('#navigation-button').click(function(){
        $('#chat-content').css("z-index", "8");
        $('#profile-content').css("z-index", "8");
    });

  //SCRIPT GOOGLE MAPS
  function initMap() {
    var directionsDisplay = new google.maps.DirectionsRenderer;
    var directionsService = new google.maps.DirectionsService;
    var mapOrigin=$('#from').val();
    var mapDestination=$('#destination').val();
    var map = new google.maps.Map(document.getElementById('googleMap'), {
      zoom: 14,
      center: {lat: 37.77, lng: -122.447}
    });
    directionsDisplay.setMap(map);

    calculateAndDisplayRoute(directionsService, directionsDisplay, mapOrigin, mapDestination);
  };  

  function calculateAndDisplayRoute(directionsService, directionsDisplay, mapOrigin, mapDestination) {
    var selectedMode = 'DRIVING';
    directionsService.route({
      origin: mapOrigin,
      destination: mapDestination,
      travelMode: google.maps.TravelMode[selectedMode]
    }, function(response, status) {
      if (status == 'OK') {
        directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  };
  //END SCRIPT GOOGLE MAPS

  $('#pickup').click(function(){
    var startPoint = $('#from').val()
    var endPoint = $('#destination').val()
    url = "/getParameters/"+startPoint+"-"+endPoint;
    $.ajax({
        url: url,
        dataType: 'json',
        type: 'GET',
        beforeSend: function () {
        },
        success: function (responseText) {
            console.log(responseText);
            $('#requestLyft').modal('open');
            $('.modalFrom').html(" "+startPoint);
            $('.modalDestination').html(" "+endPoint);
            $('#time').html(responseText["time"]);
            $('#distance').html(responseText["distance"]);
            $('#modalCost').html(responseText["cost"]);
        },
        error: function (req, status, err) {
            console.log('Error: ' + err);
            alert("Esta ruta no es válida. \nPor favor, pide un avión!")
        }
    });
  });

$('#requestDriver').click(function(){
    url = "/getDriver";
    $.ajax({
        url: url,
        dataType: 'json',
        type: 'GET',
        beforeSend: function () {
        },
        success: function (responseText) {
            console.log(responseText);
            selectedDriver = responseText;
            $('#waitingDriver').modal('open');
            $('#driverName').html(responseText["firstName"]);
            $('#carModel').html(responseText["carModel"]);
            $('#carLicense').html(responseText["carLicense"]);
            $('#carPhoto').attr("src", responseText["carPhoto"]);
            $('#driverPhoto').attr("src", responseText["profilePhoto"]);
            $('#averageRate').html(responseText["averageRate"]);
            $('#driverId').val(responseText['id']);
        },
        error: function (req, status, err) {
            console.log('Error: ' + err);
            alert("Esta ruta no es válida. \nPor favor, pide un avión!")
        }
    });
  });
$('#goPayment').click(function() {
    var input_value = [];
    var startPointVal = $('.modalFrom').html().substring(1);
    var endPointVal = $('.modalDestination').html().substring(1);
    var distanceVal = parseFloat($('#distance').html());
    var timeVal = parseInt($('#time').html());
    var costVal = parseFloat($('#modalCost').html());
    var driverVal = parseInt($('#driverId').val());
    var json_values = {
        startPoint: startPointVal,
        endPoint: endPointVal,
        distance: distanceVal,
        time: timeVal,
        cost: costVal,
        driver: driverVal
    };
    var output = JSON.stringify(json_values);
    console.log(output);
    $('#data').val(output);
});