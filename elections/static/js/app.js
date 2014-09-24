var nbn = nbn || {};
nbn.charts = nbn.charts || {};

data_url = 'http://elections.huffingtonpost.com/pollster/api/charts/';

nbn.charts.init = function(opts) {
  options = opts;
  url = data_url + encodeURIComponent(options.race_slug);
  proxyUrl = '/proxy/' + url;
  console.log(proxyUrl);
  handleD3(proxyUrl);
};

function handleD3(url) {
  d3.json(url, function(json) { drawChart(json); });

  function drawChart(json) {
    console.log(json);
  }
}
