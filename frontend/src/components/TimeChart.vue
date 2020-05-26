<script>
import { Line } from "vue-chartjs";

export default {
  extends: Line,
  data() {
    return {
      datacollection: null
    };
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt()],
        datasets: [
          {
            label: "April",
            borderColor: "#028090",
            data: [
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt()
            ]
          },
          {
            label: "May",
            borderColor: "#00a896",
            data: [
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt()
            ]
          },
          {
            label: "June",
            borderColor: "#02c39a",
            data: [
              this.getRandomInt(),
              this.getRandomInt(),
              this.getRandomInt()
            ]
          }
        ]
      };
      this.options = {
        title: {
          text: "Bills Summary",
          display: true,
          fontColor: "#e5e5e5",
          fontSize: 15
        },
        scales: {
          yAxes: [
            {
              ticks: {
                fontColor: "#e5e5e5"
              }
            }
          ],
          xAxes: [
            {
              ticks: {
                fontColor: "#e5e5e5"
              }
            }
          ]
        },
        legend: {
          labels: {
            fontColor: "#e5e5e5"
          }
        }
      };
    },
    getRandomInt() {
      return Math.floor(Math.random() * (50 - 5 + 1)) + 5;
    }
  },
  mounted() {
    this.fillData();
    this.renderChart(this.datacollection, this.options);
  }
};
</script>
