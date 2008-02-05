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


setDirections("{{ dir_from }}", "{{ dir_to }}", "fr");
document.forms[1].save.disabled = true
