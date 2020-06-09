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

            lastThreeMonthsNames() {
                const monthNames = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December"];

                let result = this.lastThreeMonthsNumbers.map(month => {
                    return monthNames[month]
                })
                return result
            },
            lastThreeMonthsNumbers() {
                let currentDate = new Date();
                let currentMonth = currentDate.getMonth();
                let lastMonth = currentMonth - 1;
                let lastButOneMonth = currentMonth - 2;

                return [lastButOneMonth, lastMonth, currentMonth];
            },
            getMonthDailyBillsSum() {
                function isFromThisMonth(monthNumber, bill) {
                    if (bill.created_at.getMonth() === monthNumber) {
                        return bill;
                    }
                }

                function isFromThisDay(dayNumber, bill) {
                    if (bill.created_at.getDay() === dayNumber) {
                        return bill;
                    }
                }

                function add(accumulator, a) {
                    return accumulator + a;
                }

                function calcDailySum(monthNumber) {
                    let thisMonthBills = this.billing.bills.filter(isFromThisMonth.bind(this, monthNumber));
                    let dailyBillsSum = Array(31).fill().map((x, dayNumber) => {
                        thisMonthBills.filter(isFromThisDay.bind(this, dayNumber)).reduce(add, 0);
                    });
                    return dailyBillsSum;
                }

                let result = this.lastThreeMonthsNumbers.map(monthNumber => calcDailySum(monthNumber));

                console.log("OKKK");
                return result;
            }
        },
        beforeCreate() {
            this.$store.dispatch("getBilling");
        },
        methods: {
            fillData() {

                this.datacollection = {
                    labels: Array(31).fill().map((x, dayNumber) => dayNumber + 1),
                    datasets: [
                        {
                            label: this.lastThreeMonthsNames[0],
                            borderColor: "#028090",
                            data: [
                                this.getMonthDailyBillsSum[0]
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
