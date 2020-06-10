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
                function isFromThisMonth(bill) {
                    let bill_date = new Date(bill.created_at);
                    if (bill_date.getMonth() === this) {
                        return bill;
                    }
                }

                function isToThisDay(bill) {
                    let bill_date = new Date(bill.created_at);
                    if (bill_date.getDay() <= this) {
                        return bill;
                    }
                }

                function add(accumulator, bill) {
                    return accumulator + bill.price;
                }

                function calcDailySum(monthNumber, billing) {
                    let thisMonthBills = billing.bills.filter(isFromThisMonth, monthNumber);
                    let dailyBillsSum = Array(31).fill().map((x, dayNumber) =>
                        thisMonthBills.filter(isToThisDay, dayNumber).reduce(add, 0)
                    );
                    return dailyBillsSum;
                }

                let result = this.lastThreeMonthsNumbers.map(monthNumber =>
                    calcDailySum(monthNumber, this.billing));
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
                            data: this.getMonthDailyBillsSum[0]

                        },
                        {
                            label: this.lastThreeMonthsNames[1],
                            borderColor: "#00a896",
                            data: this.getMonthDailyBillsSum[1]

                        },
                        {
                            label: this.lastThreeMonthsNames[2],
                            borderColor: "#02c39a",
                            data: this.getMonthDailyBillsSum[2]

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
