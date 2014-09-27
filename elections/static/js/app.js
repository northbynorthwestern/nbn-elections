var nbn = nbn || {};
nbn.charts = nbn.charts || {};

nbn.charts.init = function(opts) {
  options = opts;
  proxyUrl = '/proxy/' + encodeURIComponent(options.race_slug);
  handleD3(proxyUrl, options);
};

function handleD3(url, options) {

  $width = $('.chart .graph').width();
  $height = $('.chart .graph').height();

  d3.json(url, function(json) { drawChart(json, options); });

  function drawChart(json, options) {
    var DATA = processData(json);

    var margin = {top: 15, right: 15, bottom: 20, left: 30};
    var width = $width - margin.left - margin.right;
    var height = $height - margin.top - margin.bottom;

    var x = d3.time.scale()
      .range([0, width]);

    var y = d3.scale.linear()
      .rangeRound([height, 0]);

    var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");

    var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left");

    var line = d3.svg.line()
      .interpolate('bundle')
      .x(function(d) { return x(d[0]); })
      .y(function(d) { return y(d[1]); })
      .defined(function(d) { return !isNaN(d[1]); });

    generateChart();

    function generateChart() {

      var formatPercent = d3.format("%");

      x.domain([getLowerXDomain(DATA), getUpperXDomain(DATA)]);
      y.domain([getLowerYDomain(DATA), getUpperYDomain(DATA)]);

      var svg = d3.select("[data-race=" + options.slug_without_number + "] .graph").append("svg")
          .attr("width", width + margin.left + margin.right)
          .attr("height", height + margin.top + margin.bottom)
      .append("g")
          .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

      var candidates = svg.selectAll(".candidate")
        .data(DATA)
      .enter()
        .append("g")
        .attr("class", "candidate")
        .attr("data-party", function(d) {return d.party || d.choice; });

      var path = candidates.append("path")
        .attr("class", "line")
        .attr("d", function(d) { return line(d.estimates_by_date); })
        .attr("stroke", function(d) {
          a = d.party || d.choice;

          if (a.toLowerCase().charAt(0) == 'd') { return 'blue'; }
          else if (a.toLowerCase().charAt(0) == 'r') {return 'red'; }
          else { return 'green'; }
        })
        .attr("opacity", .5)
        .attr("stroke-width", 1.5)
        .attr("fill", "none")



      svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);

      svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor", "end")
        .tickFormat(formatPercent);

    }

    function processData(json) {
      data = [];

      for (var i = 0; i < json.estimates.length; i++) {
        json.estimates[i].estimates_by_date = []
        data.push(json.estimates[i])

        for (var j= 0; j < json.estimates_by_date.length; j++) {
          if (json.estimates_by_date[j].estimates[i].choice != "Undecided") {
            data[i].estimates_by_date.push(
              [new Date(json.estimates_by_date[j].date.replace('-', ' ')),
              json.estimates_by_date[j].estimates[i].value]
            )
          }
        };
      }
      return data
    }

    function getLowerXDomain(dataset) {
      var xValues = [];
      for (var i = dataset.length - 1; i >= 0; i--) {
        for (var j = dataset[i].estimates_by_date.length - 1; j >= 0; j--) {
            xValues.push(dataset[i].estimates_by_date[j][0]);
        };
      };
      min = d3.min(xValues);
      return min;
    }
    function getUpperXDomain(dataset) {
      var xValues = [];
      for (var i = dataset.length - 1; i >= 0; i--) {
        for (var j = dataset[i].estimates_by_date.length - 1; j >= 0; j--) {
            xValues.push(dataset[i].estimates_by_date[j][0]);
        };
      };
      max = d3.max(xValues);
      return max
    }

    function getLowerYDomain(dataset) {
      var yValues = [];
      for (var i = dataset.length - 1; i >= 0; i--) {
        for (var j = dataset[i].estimates_by_date.length - 1; j >= 0; j--) {
            yValues.push(dataset[i].estimates_by_date[j][1]);
        };
      };
      min = d3.min(yValues);
      return min - (min/15);
    }
    function getUpperYDomain(dataset) {
      var yValues = [];
      for (var i = dataset.length - 1; i >= 0; i--) {
        for (var j = dataset[i].estimates_by_date.length - 1; j >= 0; j--) {
            yValues.push(dataset[i].estimates_by_date[j][1]);
        };
      };
      max = d3.max(yValues);
      return max + (max/15);
    }

    $(window).on('resize', function(){
      var $width = $('.chart .graph').width();
      var width = $width - margin.left - margin.right;

      var svg = d3.select("[data-race=" + options.slug_without_number + "] .graph svg")
        .attr("width", width + margin.left + margin.right);

      x = d3.time.scale().range([0, width]);
      xAxis.scale(x);

      d3.select("[data-race=" + options.slug_without_number + "] .graph svg").remove();

      generateChart();

    });

  }
}
