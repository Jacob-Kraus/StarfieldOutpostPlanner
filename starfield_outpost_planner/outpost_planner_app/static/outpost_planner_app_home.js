
last_row_id = 'row-1'


function deleteOutpostModuleLine(rowIndex)
{
    console.log("deleting rowIndex = " + rowIndex);
    rowIndex = parseInt(rowIndex);
    var table = document.getElementById("itemizationTable");
    table.deleteRow(rowIndex);
}


async function getRow(rowIndex)
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
            console.log(`response:\n${response}`)
            let htmlText = await response.text();
            console.log(`getRow():\n${htmlText}`); // TODO: why is this good, but the return value not good?
            return htmlText;
        } catch (error) {
            console.error('response.text() error: ' + error.message);
        }
    } catch {
        console.error('fetch() error: ' + error.message);
    }
}


function outpostModuleSelectionChanged(id, moduleName, moduleCount)
{
    // TODO
    var moduleTag = document.getElementById(id);
    console.log("TODO: outpostModuleSelectionChanged(id, moduleName, moduleCount)")
}


async function addOutpostModuleLine(rowIndex)
{
    // rowIndex will be the index in the table which the new line/row will inhabit.
    let htmlText = await getRow(rowIndex);
    console.log(`addOutpostModuleLine():\n${htmlText}`);
    console.log("acquired row contents string");
    var table = document.getElementById("itemizationTable");
    var lastRow = document.getElementById(last_row_id);

    // this approach didn't work:
    var row = table.insertRow(rowIndex);
    console.log("added rowIndex = " + rowIndex);
    row.innerHTML = htmlText;
}
