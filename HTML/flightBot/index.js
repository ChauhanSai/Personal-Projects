const index = JSON.parse('{ "keywords": [ "IFR", "{callsign} cleared to {destination} via IFR", "pushback", "{callsign} pushback approved facing {direction}", "startup", "{callsign} startup approved", "taxi", "{callsign} taxi {runway}", "clearance", "{callsign} cleared to {destination}", "holding short", "{callsign} cross runway {runway} {intersection}", "passing, altitude", "{callsign} radar contact, /centre" ], "commands": { "ground":[ "{departure} ground", "_callsign", "_departure", "_destination" ], "tower": [ "", "_runway" ], "centre": [ "{callsign} maintain {altitude}", "_altitude" ], "approach": [ "{callsign} runway {runway} cleared to land", "_runway" ] }, "ext": [ "{callsign} runway {runway} cleared for takeoff", "{callsign} expedite climb", "{callsign} climb and maintain {altitude}", "{callsign} descend and maintain {altitude}" ] }')
var debug = 0;

var data = [["", ""], ["", ""], ["", ""], ["", ""], ["", ""]]

var callsign = "";
var destination = "";
var departure = "";
var runway = "";
var altitude = 32000;

var direction = "";
var intersection = "";

var takeoffRand = 0;
var takeoffTime = 0;
var expediteRand = 0;
var expediteTime = 0;
var cruiseRand = 0;
var cruiseTime = 0;


function input(input) {
    input = document.getElementById("textInput").value.replace("\n", " ");
    let temp = "";
    if (input.includes('/'))
        temp = replace(getCommand(input));
    else temp = replace(getKeyword(input));

    add(input, temp);
}

function add(input, output){
    if (input == "") 
        input = "···"
    if (output == "") 
        output = "···"
    for (let i = 0; i < data.length; i++) {
        if (data[i][1] == "") {
            data[i][0] = input;
            data[i][1] = output;
            console.log(rerender());
            return output;
        }
    }
    //else shift
    for (let i = 0; i < data.length - 1; i++) {
        data[i][0] = data[i + 1][0];
        data[i][1] = data[i + 1][1];
    }
    data[data.length - 1][0] = input;
    data[data.length - 1][1] = output;
    console.log(rerender());
    return output;
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
        departure = param[1];
        destination = param[2];
        document.getElementById("tooltip").innerHTML = "> /tower [runway]";
        return index.commands.ground[0];
    }

    //tower
    if (command == "tower") {
        runway = param.join(" ").replace(/runway/i, "");
        if(runway.substring(0,1) == " ")
            runway = runway.substring(1);
        document.getElementById("tooltip").innerHTML = "> /centre [altitude]";
        takeoffRand = Math.round(Math.random()*10)+1;
        takeoffTime = 0;
        takeoffVal = setInterval(takeoff, 1000);
        console.log(`Starting takeoffVal at ${takeoffTime} until ${takeoffRand}`)
        return index.commands.tower[0];
    }

    //centre
    if (command == "centre" || command == "center") {
        altitude = parseInt(param[0]);
        if (altitude < 0)
            altitude = 32000;
        document.getElementById("tooltip").innerHTML = "> /approach [runway]";
        cruiseRand = Math.round(Math.random() * 3600) + 180;
        cruiseTime = 0;
        cruiseVal = setInterval(cruise, 1000);
        console.log(`Starting cruiseVal at ${cruiseTime} until ${cruiseRand}`)
        clearInterval(expediteVal);
        console.log("expediteVal complete")
        return index.commands.centre[0];
    }

    //approach
    if (command == "approach") {
        runway = param.join(" ").replace(/runway/i, "");
        if (runway.substring(0, 1) == " ")
            runway = runway.substring(1);
        document.getElementById("tooltip").innerHTML = "> /ground [callsign] [departure] [destination]";
        clearInterval(cruiseVal);
        console.log("cruiseVal complete")
        return index.commands.approach[0];
    }

    return "Syntax error";
}

function takeoff() {
    takeoffTime++;
    if(takeoffTime == takeoffRand){
        add("", replace(index.ext[0]))
        expediteRand = Math.round(Math.random() * 170);
        expediteTime = 20;
        expediteVal = setInterval(expedite, 1000);
        console.log(`Starting expediteVal at ${expediteTime} until ${expediteRand}`)
        clearInterval(takeoffVal);
        console.log("takeoffVal complete")
    }
}

function expedite() {
    expediteTime++;
    if (expediteTime == expediteRand) {
        add("", replace(index.ext[1]))
        clearInterval(expediteVal);
        console.log("expediteVal complete")
    }
}

function cruise() {
    cruiseTime++;
    if (cruiseTime == cruiseRand) {
        let temp = Math.round(Math.random())
        if(temp == 0) temp = -1;
        altitude += temp*1000;
        if(temp < 0)
            add("", replace(index.ext[3]))
        else
            add("", replace(index.ext[2]))
        cruiseRand = Math.round(Math.random() * 3600);
        cruiseTime = 360;
        cruiseVal = setInterval(cruise, 1000);
        console.log("cruiseVal complete")
        console.log(`Starting cruiseVal at ${cruiseTime} until ${cruiseRand}`)
    }
}

function replace(text) {
    return text.replace("{callsign}", callsign).replace("{destination}", destination).replace("{departure}", departure).replace("{runway}", runway).replace("{altitude}", altitude).replace("{direction}", direction).replace("{intersection}", intersection);
}

function rerender() {
    //RENDER HTML
    document.getElementById("textInput").value = "";
    document.getElementById("textInput").focus();
    let tx = 1
    for (let i = data.length-1; i >= 0; i--)
        if(data[i][1] != ""){
            let tempS = "tx" + tx + "s";
            let tempR = "tx" + tx++ + "r";
            document.getElementById(tempS).innerHTML = "→ " + data[i][0];
            document.getElementById(tempR).innerHTML = "← " + data[i][1];
        }
}

function openTheme() {
    document.getElementById("dropdown").style.display = 'block';
    document.getElementById("button").style.display = 'none';
    debug++;
    if(debug >= 3){
        console.log("debug")
        window.open("https://chauhansai.github.io/Script-Projects/HTML/flightBot/themes", "_self")
        debug = 0;
    }

    let filters = document.getElementById("filters");
    let color = document.getElementsByClassName("color");
    let airln = document.getElementsByClassName("airln");
    filters.addEventListener("input", function (event) {
        if (filters.value == "color") {
            for (let i = 0; i < color.length; i++)
                color[i].style.display = "block";
            for (let i = 0; i < airln.length; i++)
                airln[i].style.display = "none";
            return;
        } 
        if (filters.value == "airln") {
            for (let i = 0; i < airln.length; i++)
                airln[i].style.display = "block";
            for (let i = 0; i < color.length; i++)
                color[i].style.display = "none";
            return;
        }
        for (let i = 0; i < airln.length; i++) 
            airln[i].style.display = "block";
        for (let i = 0; i < color.length; i++)
            color[i].style.display = "block";
    }, false);
}

function choice(themeName){
    if (themeName != null) {
        document.getElementById("theme").href = "themes/" + themeName + ".css";
        console.log(themeName);
    }
    debug = 0;
    document.getElementById("dropdown").style.display = 'none';
    document.getElementById("button").style.display = 'unset';

}