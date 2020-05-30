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
            // categoriesNames() {
            //     let result = this.categories.map(category => {
            //         return category.name
            //     })
            //     return result
            // },
            // categoriesTotals() {
            //     let result = this.categories.map(category => {
            //         return category.category_total
            //     })
            //     return result
            // }
            lastThreeMonthsNames() {
                const monthNames = ["January", "February", "March", "April", "May", "June",
                    "July", "August", "September", "October", "November", "December" ];
                let currentMonth = Date.now().getMonth();
                console.log(currentMonth);

                let monthsList = [monthNames[currentMonth - 2],monthNames[currentMonth - 1], monthNames[currentMonth]];
                // console.log(monthsList);
                return monthsList;
            }
        },
        beforeCreate() {
            this.$store.dispatch("getBilling");
        },
        methods: {
            fillData() {
                this.datacollection = {
                    labels: Array(31).fill().map((x, i) => i),
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
