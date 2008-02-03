gmap = map
gdir = new GDirections(map);
GEvent.addListener(gdir, "error", handleErrors);
GEvent.addListener(gdir, "load", onGDirectionsLoad);

{% for dir in db_dirs %}
dir{{forloop.counter}} = new GDirections(map);
dir{{forloop.counter}}.{{ dir.js }}
{% endfor %}


setDirections("{{ dir_from }}", "{{ dir_to }}", "fr");
document.forms[1].save.disabled = true
