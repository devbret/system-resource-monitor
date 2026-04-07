async function fetchData() {
  const response = await fetch("/api/resource");
  return response.json();
}

function createChart(id, title, valueId, yDomain = [0, 100]) {
  const margin = { top: 40, right: 20, bottom: 40, left: 60 };
  const width = 600 - margin.left - margin.right;
  const height = 400 - margin.top - margin.bottom;

  const svg = d3
    .select(`#${id}`)
    .append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
    .append("g")
    .attr("transform", `translate(${margin.left},${margin.top})`);

  svg
    .append("text")
    .attr("x", width / 2)
    .attr("y", -10)
    .attr("text-anchor", "middle")
    .style("font-size", "24px")
    .style("font-weight", "bold")
    .text(title);

  const data = [{ time: 0, value: 0 }];

  const x = d3.scaleLinear().domain([0, 50]).range([0, width]);
  const y = d3.scaleLinear().domain(yDomain).range([height, 0]);

  const line = d3
    .line()
    .x((d) => x(d.time))
    .y((d) => y(d.value))
    .curve(d3.curveMonotoneX);

  const xAxis = d3
    .axisBottom(x)
    .ticks(10)
    .tickSize(-height)
    .tickFormat((d) => d);

  const yAxis = d3
    .axisLeft(y)
    .ticks(10)
    .tickSize(-width)
    .tickFormat((d) => d);

  svg
    .append("g")
    .attr("transform", `translate(0,${height})`)
    .call(xAxis)
    .selectAll(".tick line")
    .style("stroke", "gold")
    .style("stroke-width", 0.5);

  svg
    .append("g")
    .call(yAxis)
    .selectAll(".tick line")
    .style("stroke", "gold")
    .style("stroke-width", 0.5);

  const path = svg
    .append("path")
    .datum(data)
    .attr("fill", "none")
    .attr("stroke", "magenta")
    .attr("stroke-width", 2)
    .attr("d", line);

  function updateChart(newValue) {
    if (data.length >= 50) {
      data.shift();
      data.forEach((d) => d.time--);
    }

    data.push({ time: data.length, value: newValue });
    path.datum(data).attr("d", line);

    document.getElementById(valueId).innerText =
      `Current Value: ${newValue.toFixed(2)}`;
  }

  return updateChart;
}

document.addEventListener("DOMContentLoaded", () => {
  const updateCpuChart = createChart("cpu-chart", "CPU Usage", "cpu-value");
  const updateMemoryChart = createChart(
    "memory-chart",
    "Memory Usage",
    "memory-value",
  );
  const updateDiskChart = createChart("disk-chart", "Disk Usage", "disk-value");
  const updateSwapChart = createChart("swap-chart", "Swap Usage", "swap-value");
  const updateCpuFreqChart = createChart(
    "cpu-freq-chart",
    "CPU Frequency",
    "cpu-freq-value",
    [0, 7000],
  );
  const updateCpuCoresChart = createChart(
    "cpu-cores-chart",
    "CPU Cores",
    "cpu-cores-value",
    [0, 16],
  );
  const updateCpuThreadsChart = createChart(
    "cpu-threads-chart",
    "CPU Threads",
    "cpu-threads-value",
    [0, 32],
  );
  const updateLoadAvgChart = createChart(
    "load-avg-chart",
    "Load Average",
    "load-avg-value",
    [0, 10],
  );
  const updateUptimeChart = createChart(
    "uptime-chart",
    "Uptime (s)",
    "uptime-value",
    [0, 100000],
  );

  async function updateData() {
    const data = await fetchData();

    updateCpuChart(data.cpu);
    updateMemoryChart(data.memory);
    updateDiskChart(data.disk);
    updateSwapChart(data.swap);
    updateCpuFreqChart(data.cpu_freq);
    updateCpuCoresChart(data.cpu_cores);
    updateCpuThreadsChart(data.cpu_threads);
    updateLoadAvgChart(data.load_avg[0]);
    updateUptimeChart(data.uptime);

    setTimeout(updateData, 1000);
  }

  updateData();
});
