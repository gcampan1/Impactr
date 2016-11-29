
$.get("/api/impact", null, function(data, textStatus, jqXHR) {
console.log(data)

a_xs = []
a_ys = []
a_zs = []
a_combined = []
for (var i = 0; i < data.length; i++) { 
  a_combined.push((data[i].a_y) * (data[i].a_x) * (data[i].a_z))
}

var svg = d3.select("svg"),
    margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = +svg.attr("width") - margin.left - margin.right,
    height = +svg.attr("height") - margin.top - margin.bottom,
    g = svg.append("g").attr("transform", "translate(" + margin.left + "," + margin.top + ")");

var parseTime = d3.timeParse("%d-%b-%y");

var x = d3.scaleTime()
    .rangeRound([0, width]);

var y = d3.scaleLinear()
    .rangeRound([height, 0]);

var line = d3.line()
    .x(function(d) { return x(d.date); })
    .y(function(d) { return y(d.close); });

/*d3.tsv("data.tsv", function(d) {
  d.date = parseTime(d.date);
  d.close = +d.close;
  return d;
}, function(error, data) {
  if (error) throw error;*/

  x.domain(d3.extent(a_combined, function(d) { return d.date; }));
  y.domain(d3.extent(a_combined, function(d) { return d.close; }));

  g.append("g")
      .attr("class", "axis axis--x")
      .attr("transform", "translate(0," + height + ")")
      .call(d3.axisBottom(x));

  g.append("g")
      .attr("class", "axis axis--y")
      .call(d3.axisLeft(y))
    .append("text")
      .attr("fill", "#000")
      .attr("transform", "rotate(-90)")
      .attr("y", 6)
      .attr("dy", "0.71em")
      .style("text-anchor", "end")
      .text("Price ($)");

  g.append("path")
      .datum(a_combined)
      .attr("class", "line")
      .attr("d", line);
});