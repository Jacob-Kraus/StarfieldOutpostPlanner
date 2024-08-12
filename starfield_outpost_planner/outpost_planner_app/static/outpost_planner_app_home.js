
last_row_id = 'row-1';


function setValue(domObjId, value) {
    document.getElementById(domObjId).value=value;
}


function deleteOutpostModuleLine(rowIndex)
{
    console.log(`deleteOutpostModuleLine(${rowIndex})`);
    outpostModuleSelectionChanged(delRowIndex=rowIndex);
}


function getNewURLData(delRowIndex=null) {
    var rows = document.getElementById("itemizationBody").rows;
    console.log(`getNewURLData(): rows.length = ${rows.length}`)
    // iterates over the <table>'s <tbody>'s <tr>s to construct the data for new URL navigation
    var valuePairs = new Array();
    var length = rows.length

    for (i=0; i < length; i++) {
        if ( delRowIndex == i ) { continue; } // skip the row we are deleting

        // add tuple to list (moduleID, count)
        var v1 = parseInt(document.getElementById(`outpostModuleName${i}`).value);
        var v2 = parseInt(document.getElementById(`num${i}`).value);
        var NaNvs = '';
        if ( isNaN(v1) ) {
            console.error('getNewURLData(): Parameter is not a number! (v1)');
        }
        if ( isNaN(v2) ) {
            console.error('getNewURLData(): Parameter is not a number! (v2)');
        }
        if ( !(isNaN(v1) || isNaN(v2)) ) {
            // console.log(`getNewURLData(): pushing new Array(${v1}, ${v2})`);
            valuePairs.push(new Array(v1, v2));
        }
    }
    console.log(`getNewURLData(): valuePairs = ${valuePairs}`);
    // construct the string
    var destination = new Array();
    for (i=0; i < valuePairs.length; i++) {
        var tempStr = `_${valuePairs[i][0]}-${valuePairs[i][1]}`;
        // console.log(`getNewURLData(): i=${i}, tempStr=${tempStr}`)
        destination.push(tempStr);
        // console.log(`getNewURLData(): destination=${destination}`);
    }
    let soln = destination.join("");
    // console.log(`getNewURLData(): ${soln}`);
    return soln;
}


async function outpostModuleSelectionChanged(delRowIndex=null)
{
    console.log(`outpostModuleSelectionChanged(delRowIndex=${delRowIndex})`);
    // test out prototype new data collection
    var destinationSlug = getNewURLData(delRowIndex=delRowIndex);
    console.log(`outpostModuleSelectionChanged: destination = (${Object.prototype.toString.call(destinationSlug)}) ${destinationSlug}`);

    // parse relative URL
    var url_path = document.URL;
    var url_arr = url_path.split("/");
    var last = url_arr.pop();
    if ( last == 'home' ) {
        url_arr.push(last); // keep the '/home' url ending, drop others
    }
    url_arr.push(destinationSlug);
    url_path = url_arr.join('/');
    // redirect to URL
    window.location.href = `${url_path}`;
}


async function getNewRow(rowIndex)
{
    // Reading the docs helped me get this function working correctly
    //  https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
    // We want the id attribute values to have the rowIndex included so we can more easily
    //  update the power and required items when the selected outpost module or count changes.
    console.log(`getNewRow(rowIndex=${rowIndex})`)
    const url = `outpostSelector${rowIndex}`;
    try {
        let response = await fetch(url);
        if (!response.ok) {
            throw new Error(`getNewRow: Response status: ${response.status}`);
        }
        try {
            // console.log(`response:\n${response}`)
            let htmlText = await response.text();
            // console.log(`getRow():\n${htmlText}`); // TODO: why is this good, but the return value not good?
            return htmlText;
        } catch (error) {
            console.error('getNewRow: response.text() error: ' + error.message);
        }
    } catch (error) {
        console.error('getNewRow: fetch() error: ' + error.message);
    }
    return null;
}


async function addOutpostModuleLine()
{
    console.log('addOutpostModuleLine()');
    // new attempt at writing function
    var destinationSlug = getNewURLData();
    destinationSlug = destinationSlug + '_0-0';
    console.log(`destinationSlug=${destinationSlug}`)

    // parse relative URL
    var url_path = document.URL;
    var url_arr = url_path.split("/");
    var last = url_arr.pop();
    if ( last == 'home' ) {
        url_arr.push(last); // keep the '/home' url ending
    }
    url_arr.push(destinationSlug);
    console.log(`url_arr=${url_arr}`);
    url_path = url_arr.join('/');
    console.log(`url_path=${url_path}`);
    // redirect to URL
    window.location.href = `${url_path}`;
}
