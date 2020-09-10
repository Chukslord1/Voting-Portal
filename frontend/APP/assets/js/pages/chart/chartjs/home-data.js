$(function () {
  chart1();
  chart2();
});

function chart1() {
  var options = {
    chart: {
      height: 400,
      type: "line",
      shadow: {
        enabled: true,
        color: "#000",
        top: 18,
        left: 7,
        blur: 10,
        opacity: 1,
      },
      toolbar: {
        show: false,
      },
    },
    colors: ["#786BED", "#999b9c"],
    dataLabels: {
      enabled: true,
    },
    stroke: {
      curve: "smooth",
    },
    series: [
      {
        name: "High - 2019",
        data: [19, 15, 14, 24, 25, 19, 22, 24, 25],
      },
      {
        name: "Low - 2019",
        data: [7, 11, 22, 18, 31, 13, 26, 16, 31],
      },
    ],
    grid: {
      borderColor: "#e7e7e7",
      row: {
        colors: ["#f3f3f3", "transparent"], // takes an array which will be repeated on columns
        opacity: 0.0,
      },
    },
    markers: {
      size: 6,
    },
    xaxis: {
      categories: [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "july",
        "aug",
        "sep",
      ],

      labels: {
        style: {
          colors: "#9aa0ac",
        },
      },
    },
    yaxis: {
      title: {
        text: "Income",
      },
      labels: {
        style: {
          color: "#9aa0ac",
        },
      },
      min: 5,
      max: 40,
    },
    legend: {
      position: "top",
      horizontalAlign: "right",
      floating: true,
      offsetY: -25,
      offsetX: -5,
    },
  };

  var chart = new ApexCharts(document.querySelector("#chart1"), options);

  chart.render();
}
function chart2() {
  var options = {
    chart: {
      height: 400,
      type: "area",
      toolbar: {
        show: false,
      },
    },
    colors: ["#999b9c", "#4CC2B0"], // line color
    fill: {
      colors: ["#999b9c", "#4CC2B0"], // fill color
    },
    dataLabels: {
      enabled: false,
    },
    stroke: {
      curve: "smooth",
    },
    markers: {
      colors: ["#999b9c", "#4CC2B0"], // marker color
    },
    series: [
      {
        name: "series1",
        data: [31, 40, 28, 51, 22, 64, 80],
      },
      {
        name: "series2",
        data: [11, 32, 67, 32, 44, 52, 41],
      },
    ],
    legend: {
      show: false,
    },
    xaxis: {
      categories: ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "July"],
      labels: {
        style: {
          colors: "#9aa0ac",
        },
      },
    },
    yaxis: {
      labels: {
        style: {
          color: "#9aa0ac",
        },
      },
    },
  };

  var chart = new ApexCharts(document.querySelector("#chart2"), options);

  chart.render();
}
