/**********************************************************
===========================================================
==================MAIN JS OF ALL PAGES=====================
===========================================================
===========================================================
***********************************************************/



// The function for the toggle bar
function toggle_menue_bar() {
	var status = document.getElementById("nav_links").style.display;

	// Checking if the links are displayed
	if ( status === "none" ) {
		document.getElementById("nav_links").style.display = "block";
	} else {
		document.getElementById("nav_links").style.display = "none";
	}
}

