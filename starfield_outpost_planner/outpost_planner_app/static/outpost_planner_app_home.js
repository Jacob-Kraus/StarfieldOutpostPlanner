
last_row_id = 'row-1'


function deleteOutpostModuleLine(rowIndex)
{
    console.log("deleting rowIndex = " + rowIndex);
    rowIndex = parseInt(rowIndex);
    var table = document.getElementById("itemizationTable");
    table.deleteRow(rowIndex);
}

/* failed approach
function get(name){  // return get[name] || undefined (if var has no value or doesn't exist)
   if(name=(new RegExp('[?&]'+encodeURIComponent(name)+'=([^&]*)')).exec(location.search))
      return decodeURIComponent(name[1]);
}
*/


async function getRow(rowIndex)
{
    // Reading the docs helped me get this function working correctly
    //  https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch
    const url = `outpostSelector${rowIndex}`;
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response status: ${response.status}`);
        }
        try {
            const htmlText = await response.text();
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


function createElementFromHTML(htmlString) {
  var div = document.createElement('div');
  div.innerHTML = htmlString;
  // Change this to div.childNodes to support multiple top-level nodes.
  return div.firstChild;
}


function addOutpostModuleLine(rowIndex)
{
    // rowIndex will be the index in the table which the new line/row will inhabit.
    const htmlText = getRow(rowIndex);
    console.log(`addOutpostModuleLine():\n${htmlText}`);
    // TODO: why is htmlStr not the actual str? Why am I unable to get the value of my text??
    console.log("acquired row contents string");
    var table = document.getElementById("itemizationTable");
    var lastRow = document.getElementById(last_row_id);

    // this approach didn't work:
    var row = table.insertRow(rowIndex);
    console.log("added rowIndex = " + rowIndex);
    row.innerHTML = htmlText;

    /*
    // This approach didn't work
    var fragment = createElementFromHTML(htmlStr);
    // You can use native DOM methods to insert the fragment:
    // document.body.insertBefore(fragment, document.body.childNodes[0]);
    table.insertBefore(fragment, lastRow);
    */
}
