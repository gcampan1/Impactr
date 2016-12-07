

// d3.tsv("seed_data.tsv", function(error, data) {
//     data.forEach(function(d) {
//         d.date = parseDate(d.date);
//         d.close = d.close;
//     });
    $.get("/api/impact", null, function(data, textStatus, jqXHR) {
console.log(data)

a_xs = []
a_ys = []
a_zs = []
a_combined = []
adddata = []
data2 = []
for (var i = 0; i < data.length; i++) { 
  a_combined.push((data[i].a_y) * (data[i].a_x))
  data2.push(data[i])
}
var date1 = data.map(function (i) {return Date.parse(i.date)})
console.log(date1)
for(var i = 0; i < date1.length; i++){
    if(date1[i] !== date1[i + 1])
    {
        a_data = []
        a_data.push(adddata)
        var lenghtofdates = a_data.length 
    }
    else{
            adddata.push((data2)) //i want to add a_y to an array and then put that array into an array

        }
//console.log(data2)
    }
console.log(lenghtofdates)
var formatCount = d3.format(",.0f");

var svg = d3.select("svg"),
    margin = {top: 30, right: 20, bottom: 30, left: 50},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");
 

var x = d3.scaleLinear()
    .rangeRound([0, width]);
// x and y are functions
// svg, g, and bar are some object (but the same type)

var bins = d3.histogram() //this is where you calculate the number of bins (histogram bars) and what to stuff them with which would be the data calculated in the add data array
     .domain(x.domain())
    .thresholds(x.ticks(lenghtofdates))
    (a_combined);   


// bins is an array of arrays (x0, x1) pairs

var y = d3.scaleLinear()
    .domain([0, d3.max(bins, function(d) { return d.length; })])
    .range([height, 0]);

//var yAxisLeft = d3.svg.axis().scale(y).ticks(10).orient("left");   

var bar = g.selectAll(".bar")
  .data(bins)
  .enter().append("g")
    .attr("class", "bar")
    .attr("transform", function(d) { return "translate(" + x(d.x0) + "," + y(d.length) + ")"; });


bar.append("rect")
    .attr("x", 1)
    .attr("width", x(bins[0].x1) - x(bins[0].x0) - 1)
    .attr("height", function(d) { return height - y(d.length); });


bar.append("text")
    .attr("dy", ".75em")
    .attr("y", 6)
    .attr("x", (x(bins[0].x1) - x(bins[0].x0)) / 2)
    .attr("text-anchor", "middle")
    .text(function(d) { return formatCount(d.length); });

g.append("g")
    .attr("class", "axis axis--x")
    .attr("transform", "translate(0," + height + ")")
    .call(d3.axisBottom(x));
 

})

/*
// set the dimensions and margins of the graph
var margin = {top: 10, right: 30, bottom: 30, left: 40},
    width = 960 - margin.left - margin.right,
    height = 500 - margin.top - margin.bottom;

// parse the date / time
var parseDate = d3.timeParse("%d-%m-%Y");

// set the ranges
var x = d3.scaleTime()
          .domain([new Date(2010, 6, 3), new Date(2017, 0, 1)])
          .rangeRound([0, width]);
var y = d3.scaleLinear()
          .range([height, 0]);

// set the parameters for the histogram
var histogram = d3.histogram()
    .value(function(d) { return d.date; })
    .domain(x.domain())
    .thresholds(x.ticks(d3.timeDay));

// append the svg object to the body of the page
// append a 'group' element to 'svg'
// moves the 'group' element to the top left margin
var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform", 
          "translate(" + margin.left + "," + margin.top + ")");

// get the data
$.get("/api/impact", null, function(data, textStatus, jqXHR) {
console.log(data)

a_xs = []
a_ys = []
a_zs = []
a_combined = []
for (var i = 0; i < data.length; i++) { 
  a_combined.push((data[i].a_y) * (data[i].a_x) * (data[i].a_z))
}
console.log(a_combined)

  // group the data for the bars
  var bins = d3.histogram()
    .domain(x.domain())
    .thresholds(x.ticks(100))
    (a_combined);


  // Scale the range of the data in the y domain
  y.domain([0, d3.max(bins, function(d) { return d.length; })]);

  // append the bar rectangles to the svg element
  svg.selectAll("rect")
      .data(bins)
    .enter().append("rect")
      .attr("class", "bar")
      .attr("x", 1)
      .attr("transform", function(d) {
          return "translate(" + x(d.x0) + "," + y(d.length) + ")"; })
      .attr("width", function(d) { return x(d.x1) - x(d.x0) -1 ; })
      .attr("height", function(d) { return height - y(d.length); });

  // add the x Axis
  svg.append("g")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  // add the y Axis
  svg.append("g")
      .call(d3.axisLeft(y));
      
});
*/