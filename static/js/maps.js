 $( document ).ready(function() {
    var map = new GMaps({
      el: '#map',
      lat: -12.043333,
      lng: -77.028333
  });
    var locations = $(".location-data");
 
    locations.each( function( key, value ) {
        var loc_id = $(this).data('id');
        map.addMarker({
          lat: $(this).data('latitude'),
          lng: $(this).data('longitude'),
          title: $(this).html(),
          click: function(e) {
            window.open("location/"+loc_id+"/detail/", "_self");
        }
    });  
    });
    map.fitZoom();
});