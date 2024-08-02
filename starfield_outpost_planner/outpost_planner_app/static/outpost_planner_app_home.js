

function outpostModuleSelectionChanged(id, moduleName, moduleCount){
    // TODO
    var moduleTag = document.getElementById(id);
}

function addOutpostModuleLine(){
    var table = document.getElementById("itemizationTable");
    var row = table.insertRow();
    var rowIndex = row.rowIndex();
    console.log("added rowIndex = " + rowIndex);
}

function deleteOutpostModuleLine(rowIndex){
    console.log('test')
    console.log("deleting rowIndex = " + rowIndex);
    rowIndex = parseInt(rowIndex);
    var table = document.getElementById("itemizationTable");
    table.deleteRow(rowIndex);
}
