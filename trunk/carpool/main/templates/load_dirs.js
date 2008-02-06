gmap = map
gdir = new GDirections(map);
GEvent.addListener(gdir, "error", handleErrors);
GEvent.addListener(gdir, "load", onGDirectionsLoad);
var queryopts = {"getPolyline":true}

{% for dir in db_dirs %}
dir{{forloop.counter}} = new GDirections();
dir{{forloop.counter}}.{{ dir.js }}

GEvent.addListener(dir{{forloop.counter}}, "load", function() {
  var poly = dir{{forloop.counter}}.getPolyline();
  gmap.addOverlay(poly);
});

{% endfor %}

  var letteredIcon = new GIcon(G_DEFAULT_ICON);
  letteredIcon.image = "/static/icons/home.png";
  markerOptions = { 'icon':letteredIcon };
  var marker = new GMarker(new GLatLng(44,1), markerOptions);
  gmap.addOverlay(marker);

setDirections("{{ dir_from }}", "{{ dir_to }}", "fr");
document.forms[1].save.disabled = true
