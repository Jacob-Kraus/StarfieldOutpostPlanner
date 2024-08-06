
last_row_id = 'row-1';


function deleteOutpostModuleLine(rowIndex)
{
    rowIndex = parseInt(rowIndex);
    var table = document.getElementById("itemizationTable");
    table.deleteRow(rowIndex);
    console.log("deleted rowIndex = " + rowIndex);
}


async function outpostModuleSelectionChanged(rowIndex)
{
    // get the module ID and the number of modules
    var moduleCount = parseInt(document.getElementById(`num${rowIndex}`).value);
    if (moduleCount > 99 || moduleCount < 1){
        // todo: set value to 1
    }
    var moduleID = parseInt(document.getElementById(`outpostModuleName${rowIndex}`).value);
    if (moduleID == null) {
        console.log("outpostModuleSelectionChanged got null moduleID");
        return; // no specified outpost module name (was the filler '----------' value)
    }

    // lookup the cost to craft 1 of one of the selected module
    const url = `costLookup${moduleID}`
    try {
        let response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        try {
            let recipeDict = await response.json();
            console.log(recipeDict);
            var recipeKeys = keys(recipeDict).sort((a, b) => a.localeCompare(b));
            //
        } catch (error) {
            console.error('response.text() error: ' + error.message);
        }
    } catch (error) {
        console.error('fetch() error: ' + error.message);
    }

    // write values to rendered webpage
    var requiredResourcesDOM = document.getElementById(`requires${rowIndex}`);
    var powerModificationDOM = document.getElementById(`power${rowIndex}`);

    // TODO
    console.log("TODO: outpostModuleSelectionChanged(rowIndex)")
}


async function getNewRow(rowIndex)
{
    // Reading the docs helped me get this function working correctly
    //  https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
    // We want the id attribute values to have the rowIndex included so we can more easily
    //  update the power and required items when the selected outpost module or count changes.
    const url = `outpostSelector${rowIndex}`;
    try {
        let response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        try {
            // console.log(`response:\n${response}`)
            let htmlText = await response.text();
            // console.log(`getRow():\n${htmlText}`); // TODO: why is this good, but the return value not good?
            return htmlText;
        } catch (error) {
            console.error('response.text() error: ' + error.message);
        }
    } catch (error) {
        console.error('fetch() error: ' + error.message);
    }
    return null;
}


async function addOutpostModuleLine(rowIndex)
{
    // rowIndex will be the index in the table which the new line/row will inhabit.
    let htmlText = await getNewRow(rowIndex);
    var table = document.getElementById("itemizationTable");

    var row = table.insertRow(rowIndex);
    if (row != null) {
        row.innerHTML = htmlText;
        console.log("added rowIndex(" + rowIndex + ")");
    }
    console.log("failed to add rowIndex(" + rowIndex + ")")
}
