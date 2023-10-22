function getFact() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if(this.readyState == 4 && this.status == 200) {
            fact = JSON.parse(this.responseText);
            document.getElementById("fact-txt").innerHTML = fact["text"];
            document.getElementById("fact-txt").style.display = "block";
            document.getElementById("source_link").setAttribute("href", fact["source_url"]);
            document.getElementById("fact-btns").style.display = "block";
            console.log(fact["source_url"])
        }
    };
    xhttp.open("GET", "/getFact", true);
    xhttp.send();
}

function share() {
    console.log("share")
    var link = document.getElementById("source_link").getAttribute("href");
    navigator.clipboard.writeText(link);
    var tooltip = document.getElementById("tipText");
    tooltip.innerHTML = "Copied";

}
function outFunc() {
    var tooltip = document.getElementById("tipText");
    tooltip.innerHTML = "Copy to clipboard";
  }