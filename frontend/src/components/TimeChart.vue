<script>
    import {Line} from "vue-chartjs";
    import {mapGetters} from "vuex";

    export default {
        extends: Line,
        data() {
            return {
                datacollection: null
            };
        },
        computed: {
            ...mapGetters({
                billing: "billing",
            }),

            monthName(monthNumber) {
                const monthNames = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"];
                return monthNames[monthNumber];
            },

            lastThreeMonthsNames() {

                let currentDate = new Date();
                let currentMonth = currentDate.getMonth();
                let lastMonth = currentMonth - 1;
                let lastButOneMonth = currentMonth - 2;

                return [this.monthName[lastMonth], this.monthName[lastButOneMonth], this.monthName[currentMonth]];
            },
            getThisMonthDailyBillsSum(monthNumber) {
                function isFromThisMonth(bill) {
                    if (bill.created_at.getMonth() === monthNumber) {
                        return bill;
                    }
                }

                let thisMonthBills = this.billing.bills.filter(isFromThisMonth);
                let dailyBillsSum = Array(31).fill().map((x, i) => {

                });
            }

        },
        beforeCreate() {
            this.$store.dispatch("getBilling");
        },
        methods: {
            fillData() {
                this.datacollection = {
                    labels: Array(31).fill(31).map((x, i) => i + 1),
                    datasets: [
                        {
                            label: this.lastThreeMonthsNames[0],
                            borderColor: "#028090",
                            data: [
                                5, 6, 3
                            ]
                        },
                        {
                            label: this.lastThreeMonthsNames[1],
                            borderColor: "#00a896",
                            data: [
                                3, 4, 5
                            ]
                        },
                        {
                            label: this.lastThreeMonthsNames[2],
                            borderColor: "#02c39a",
                            data: [
                                2, 3, 4
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
        },
        mounted() {
            this.fillData();
            this.renderChart(this.datacollection, this.options);
        }
    };
</script>
