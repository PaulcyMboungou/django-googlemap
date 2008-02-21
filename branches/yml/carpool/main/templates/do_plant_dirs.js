  //var icon = new GIcon(G_DEFAULT_ICON);
  //icon.image = "/static/icons/work.png";
  //markerOptions = { 'icon':icon };
  var marker = new GMarker({{ plant.position.js }});
  map.addOverlay(marker);

var pos;
var m = null;
var poly = null;
var dir

function calc_directions() {
    if (poly!=null) map.removeOverlay(poly)
	dir = new GDirections();
	dir.loadFromWaypoints([pos, {{ plant.position.js }}], {"getPolyline":true});
	
	GEvent.addListener(dir, "load", function() {
	  poly = dir.getPolyline();
	  map.addOverlay(poly);
	});
}

GEvent.addListener(map, 'click', function(marker, point) {
    if (m!=null) map.removeOverlay(m)
    if (dir!=null) map.removeOverlay(dir)
	m = new GMarker(point, {draggable: true});
	//map.clearOverlays()
	map.addOverlay(m);
	m.openInfoWindowHtml("Can be moved with drag and drop.");
	pos = m.getLatLng()
	//document.forms[0].lat.value = point.lat()
	//document.forms[0].lon.value = point.lng()
	GEvent.addListener(m, "dragend", function() {
	  m.openInfoWindowHtml("Moved ...");
	  pos = m.getLatLng();
	  calc_directions();
	});
	
	calc_directions();
});
