<script>
import { Pie } from "vue-chartjs";

export default {
  extends: Pie,
  data() {
    return {
      datacollection: null
    };
  },
  methods: {
    fillData() {
      this.datacollection = {
        labels: ["Food", "Health", "Other"],
        datasets: [
          {
            backgroundColor: ["#028090", "#00a896", "#02c39a"],
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
          text: "Categories",
          display: true,
          fontColor: "#e5e5e5",
          fontSize: 15
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
