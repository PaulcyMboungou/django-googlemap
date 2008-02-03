gmap = map
gdir = new GDirections(map);
GEvent.addListener(gdir, "error", handleErrors);
GEvent.addListener(gdir, "load", onGDirectionsLoad);

setDirections("Talence", "Bordeaux", "fr");

dir = new GDirections(map);
{% for dir in db_dirs %}
dir.{{ dir.js }}
{% endfor %}
