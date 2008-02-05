var gmap;
var gdir;
var geocoder = null;
var addressMarker;

function setDirections(fromAddress, toAddress, locale) {
  gdir.load("from: " + fromAddress + " to: " + toAddress,
            { "locale": locale });
  document.forms[1].save.disabled = false
}

function add_dir(username) {
    s='add_dir/' + username + '/'
    for (i=0; i < gdir.getNumGeocodes(); i++) {
      p = gdir.getMarker(i).getLatLng()
      s += p.lat()+','+p.lng()+'/'
    }
	GDownloadUrl(s, function(text, code){
		if (code==200) alert("Result: "+text);
		else alert("Error - not saved "+s)
	});
}

function handleErrors(){
   document.forms[1].save.disabled = true
   if (gdir.getStatus().code == G_GEO_UNKNOWN_ADDRESS)
     alert("No corresponding geographic location could be found for one of the specified addresses. This may be due to the fact that the address is relatively new, or it may be incorrect.\nError code: " + gdir.getStatus().code);
   else if (gdir.getStatus().code == G_GEO_SERVER_ERROR)
     alert("A geocoding or directions request could not be successfully processed, yet the exact reason for the failure is not known.\n Error code: " + gdir.getStatus().code);
   
   else if (gdir.getStatus().code == G_GEO_MISSING_QUERY)
     alert("The HTTP q parameter was either missing or had no value. For geocoder requests, this means that an empty address was specified as input. For directions requests, this means that no query was specified in the input.\n Error code: " + gdir.getStatus().code);

//   else if (gdir.getStatus().code == G_UNAVAILABLE_ADDRESS)  <--- Doc bug... this is either not defined, or Doc is wrong
//     alert("The geocode for the given address or the route for the given directions query cannot be returned due to legal or contractual reasons.\n Error code: " + gdir.getStatus().code);
     
   else if (gdir.getStatus().code == G_GEO_BAD_KEY)
     alert("The given key is either invalid or does not match the domain for which it was given. \n Error code: " + gdir.getStatus().code);

   else if (gdir.getStatus().code == G_GEO_BAD_REQUEST)
     alert("A directions request could not be successfully parsed.\n Error code: " + gdir.getStatus().code);
    
   else alert("An unknown error occurred.");
   
}

function onGDirectionsLoad(){ 
/*
	var mstart = gdir.getMarker(0)
	p = mstart.getLatLng()
	p = new GLatLng(p.lat()-0.001, p.lng())
    mstart = new GMarker(p, {draggable: true});
	GEvent.addListener(mstart, "dragend", function() {
	  mstart.openInfoWindowHtml("Just bouncing along...");
	});
    gmap.addOverlay(mstart);
	
	var mend = gdir.getMarker(1)
	mend = new GMarker(mend.getLatLng(), {draggable: true});
    gmap.addOverlay(mend);
	GEvent.addListener(mend, "dragend", function() {
	  mend.openInfoWindowHtml("Just bouncing along...");
	});
*/
}
