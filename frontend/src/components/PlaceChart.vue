<script>
    import {Pie} from "vue-chartjs";
    import {mapGetters} from "vuex";

    export default {
        extends: Pie,
        data() {
            return {
                datacollection: null
            };
        },
        computed: {
            ...mapGetters({
                billing: "billing",
            }),
            places() {
                let billsPlaces = this.billing.bills.map(function (bill) {
                    return {place: bill.where, price: bill.price}
                });

                let groupedPlaces = billsPlaces.reduce((group, singlePlace) => {
                    group[singlePlace.place] = (group[singlePlace.place] || []).concat(singlePlace);
                    return group;
                }, {});

                return groupedPlaces;
            },

            groupedPlacesPrice() {
                // let dailyBillsSum = Array(31).fill().map((x, dayNumber) =>
                //         thisMonthBills.filter(isToThisDay, dayNumber).reduce(add, 0)
                //     );

                // function add(accumulator, place) {
                //     return accumulator + place.price;
                // }

                // console.log(this.places[Object.keys(this.places)[2]]);
                // console.log(this.places[Object.keys(this.places)[2]].reduce(add, 0));

                // let placePricesSum = Object.keys(this.places).map(function (place) {
                //         return {
                //             place: Object.keys(this.places)[place],
                //             // price: Object.keys(this.places)[place].reduce(add, 0)
                //         }
                //     }
                // );

                // console.log(Object.keys(this.places).length);

                let placePricesSum = Array(Object.keys(this.places).length).fill().map(function (placeNumber) {
                        console.log(placeNumber)
                        return {
                            place: Object.keys(this.places)[placeNumber],
                            // price: Object.keys(this.places)[place].reduce(add, 0)
                        }
                    }
                );


                console.log(placePricesSum);

                return 0;
            },


            fiveMostImportantPlaces() {
                function comparePlaces(a, b) {
                    return b.place_total - a.place_total
                }

                let result = this.groupedPlacesPrice;
                // if (result.length > 5) {
                result = result.sort(comparePlaces()).slice(0, 5)
                // }
                return result
            },
        },
        beforeCreate() {
            this.$store.dispatch("getBilling");
        },
        methods: {
            fillData() {
                this.datacollection = {
                    labels: ["Krakow", "Warszawa", "Other"],
                    datasets: [
                        {
                            backgroundColor: ["#028090", "#00a896", "#02c39a"],
                            data: [
                                this.fiveMostImportantPlaces,
                                this.getRandomInt(),
                                this.getRandomInt()
                            ]
                        }
                    ]
                };
                this.options = {
                    title: {
                        text: "Places",
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
        },
        mounted() {
            this.fillData();
            this.renderChart(this.datacollection, this.options);
        }
    };
</script>
