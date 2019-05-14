/*
Generates a color based on gpa.

returns hexcode for the generated color
*/
function generateColor(gpa) {

	//amount of red and green in the color is related to gpa
	var green = Math.floor((gpa-2) / 2 * 255);
	var red = 255 - green;

	//in order to create brighter colors, add more of both when the gpa is around 3.
	green += Math.floor( (1-Math.abs(gpa-3)) * 127);
	red += Math.floor( (1-Math.abs(gpa-3)) * 127);

	var redString = red.toString(16);
	if (redString.length < 2)
		redString = "0" + redString;

	var greenString = green.toString(16);
	if (greenString.length < 2)
		greenString = "0" + greenString;

	return "#" + redString + greenString + "00";
}

function showTooltip(evt, text) {
	var tooltip = document.getElementById("tooltip");
	tooltip.innerHTML = text;
	//this is not the best way to do this - use jquery
	tooltip.style.display = "block";
	tooltip.style.left = $(document).width() / 2 > evt.pageX ? evt.pageX + 10 + 'px' : evt.pageX - text.length*4 - 10 + 'px';
	tooltip.style.top = evt.pageY + 10 + 'px';
}

function hideTooltip() {
	var tooltip = document.getElementById("tooltip");
	tooltip.style.display = "none";
}