GEvent.addListener(map, 'click', function(marker, point) {
	m = new GMarker(point);
	map.clearOverlays()
	map.addOverlay(m);
	pos = m.getLatLng()
	document.forms[0].lat.value = point.lat()
	document.forms[0].lon.value = point.lng()
	/*
	GDownloadUrl('../../../gmap/test/input/addpoint?lat='+escape(pos.lat())+'&lon='+escape(pos.lng()), function(text, code){
		confirm(code+text)
		window.location.reload()
	});
	*/
});
