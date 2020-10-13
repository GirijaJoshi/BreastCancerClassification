// import the data from data.js
const tableData = data;

// Reference the HTML table using d3
var tbody = d3.select("tbody");

function buildTable(data) {
  // First, clear out any existing data
  tbody.html("");

  // Next, loop through each object in the data
  // and append a row and cells for each value in the row
  data.forEach((dataRow) => {
    // Append a row to the table body
    let row = tbody.append("tr");

    // Loop through each field in the dataRow and add
    // each value as a table cell (td)
    Object.values(dataRow).forEach((val) => {
      let cell = row.append("td");
      cell.text(val);
    });
  });
}

// Keep track of all filters
var filters = {};

// This function will replace your handleClick function
// will call filterTable at the end
function updateFilters() {

  //resetting filter variable
  filters = {}

  // Save the element, value, and id of the filter that was changed
  let date = d3.select("#datetime").property("value");
  let city = d3.select('#city').property("value")
  let state = d3.select('#state').property("value")
  let country = d3.select('#country').property("value")
  let shape = d3.select('#shape').property("value")

  // If a filter value was entered then add that filter Id and value
  // to the filters list. Otherwise, clear that filter from the filters object
  if (date === "" ) {
      delete date
      }
    else {filters["datetime"] = date}
  if (city === "" ) {
      delete city
      }
    else {filters["city"] = city}
  if (state === "" ) {
      delete state
      }
    else {filters["state"] = state}
  if (country === "" ) {
      delete country
      }
    else {filters["country"] = country}
  if (shape === "" ) {
      delete shape
      }
    else {filters["shape"] = shape}

  // Call function to apply all filters and rebuild the table
  filterTable(filters);
}

// this function will return table with filtered data
function filterTable() {

  // Set the filteredData to the tableData
  filteredData = tableData
console.log(filteredData, 'line 78')
  // Loop through all of the filters and keep any data that
  // matches the filter values
  Object.entries(filters).forEach(([key,value]) => {
    filteredData = filteredData.filter(row => row[key] === value);
  })

  // Finally, rebuild the table using the filtered Data
  buildTable(filteredData);
}

// Attach an event to listen for changes to each filter
// calls updateFilters function
d3.selectAll("#filter-btn").on("click", updateFilters);

// Build the table when the page loads
buildTable(tableData);
