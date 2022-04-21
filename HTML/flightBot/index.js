const index = JSON.parse('{ "keywords": [ "IFR", "{callsign} cleared to {destination} via IFR", "pushback", "{callsign} pushback approved facing {direction}", "startup", "{callsign} startup approved", "taxi", "{callsign} taxi {runway}", "clearance", "{callsign} cleared to {destination}", "holding short", "{callsign} cross runway {runway} {intersection}", "passing, altitude", "{callsign} radar contact, /centre" ], "commands": { "ground":[ "{departure} ground", "_callsign", "_departure", "_destination" ], "tower": [ "{callsign} runway {runway} cleared for takeoff", "_runway" ], "centre": [ "{callsign} continue along flight path" ], "approach": [ "{callsign} runway {runway} cleared to land", "_runway" ] } }')

var data = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]

var callsign = "";
var destination = "";
var departure = "";
var runway = "";

var direction = "";
var intersection = "";

/*console.log(input("/ground BA345 KLAX KDFW"));
console.log(input("BA123 requesting IFR clearance to KDFW"));
console.log(input("BA123 requesting pushback facing north"));
console.log(input("BA123 holding short runway 9L at K"));
console.log(input("/tower 34L"));
console.log(input("/centre "));*/

function input(input) {
    input = document.getElementById("textInput").value.replace("\n", " ");
    let temp = "";
    if (input.includes('/'))
        temp = replace(getCommand(input));
    else temp = replace(getKeyword(input));

    for (let i = 0; i < data.length; i++) {
        if (data[i][1] == "") {
            data[i][0] = input;
            data[i][1] = temp;
            console.log(rerender());
            return temp;
        }
    }
    //else shift
    for (let i = 0; i < data.length - 1; i++) {
        data[i][0] = data[i + 1][0];
        data[i][1] = data[i + 1][1];
    }
    data[data.length - 1][0] = input;
    data[data.length - 1][1] = temp;
    console.log(rerender());
    return temp;

}

function getKeyword(key) {
    for (let i = 0; i < index.keywords.length; i += 2)
        if (key.includes(index.keywords[i])) {
            if (key.includes("pushback") && key.includes("facing "))
                direction = key.substring(key.indexOf("facing ") + 7)
            if (key.includes("taxi") && key.includes("to "))
                runway = key.substring(key.indexOf("to "))
            if (key.includes("holding short") && key.includes("runway ")) {
                runway = key.substring(key.indexOf("runway ") + 7)
                runway = runway.substring(0, runway.indexOf(" "))
            }
            if (key.includes("holding short") && key.includes("at "))
                intersection = key.substring(key.indexOf("at "))
            return index.keywords[i + 1];
        }
    return "Say again";
}

function getCommand(key) {
    if(!key.includes(" "))
        key += " ";
    let command = key.substring(key.indexOf("/") + 1, key.indexOf(" "));
    let param = key.substring(key.indexOf(" ") + 1).split(" ");
    //ground
    if (command == "ground") {
        callsign = param[0];
        destination = param[1];
        departure = param[2];
        document.getElementById("tooltip").innerHTML = "> /tower [runway]";
        return index.commands.ground[0];
    }

    //tower
    if (command == "tower") {
        runway = param[0];
        document.getElementById("tooltip").innerHTML = "> /centre ";
        return index.commands.tower[0];
    }

    //centre
    if (command == "centre" || command == "center") {
        document.getElementById("tooltip").innerHTML = "> /approach [runway]";
        return index.commands.centre[0];
    }

    //approach
    if (command == "approach") {
        runway = param[0];
        document.getElementById("tooltip").innerHTML = "> /ground [callsign] [departure] [destination]";
        return index.commands.approach[0];
    }

    return "Syntax error";
}

function replace(text) {
    return text.replace("{callsign}", callsign).replace("{destination}", destination).replace("{departure}", departure).replace("{runway}", runway).replace("{direction}", direction).replace("{intersection}", intersection);
}

function rerender() {
    //RENDER HTML
    document.getElementById("textInput").value = "";
    let tx = 1
    for (let i = data.length-1; i >= 0; i--)
        if(data[i][1] != ""){
            let tempS = "tx" + tx + "s";
            let tempR = "tx" + tx++ + "r";
            document.getElementById(tempS).innerHTML = "→ " + data[i][0];
            document.getElementById(tempR).innerHTML = "← " + data[i][1];
        }
}