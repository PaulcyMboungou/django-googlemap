gdir = new GDirections(map, document.getElementById("directions"));
GEvent.addListener(gdir, "error", handleErrors);

setDirections("San Francisco", "Mountain View", "en_US");
