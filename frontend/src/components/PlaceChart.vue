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
            groupedPlaces() {
                let billsPlaces = this.billing.bills.map(function (bill) {
                    return {place: bill.where, price: bill.price}
                });

                let groupedPlaces = billsPlaces.reduce((group, singlePlace) => {
                    group[singlePlace.place] = (group[singlePlace.place] || []).concat(singlePlace);
                    return group;
                }, {});

                return groupedPlaces;
            },

            sumPlacesPrice() {
                function add(accumulator, place) {
                    return accumulator + place.price;
                }

                let placePricesSum = {};
                for (const place in this.groupedPlaces) {
                    placePricesSum[place] = this.groupedPlaces[place].reduce(add, 0);
                }
                return placePricesSum;
            },


            fiveMostImportantPlaces() {
                let placesToSort = [];
                for (let place in this.sumPlacesPrice) {
                    placesToSort.push([place, this.sumPlacesPrice[place]]);
                }

                let sortedPlaces = placesToSort
                if (sortedPlaces.length > 5) {
                    sortedPlaces = sortedPlaces.sort(function (a, b) {
                        return b[1] - a[1];
                    }).slice(0, 5);
                }

                let result = {};
                for (let place in sortedPlaces){
                    result[sortedPlaces[place][0]] = sortedPlaces[place][1];
                }

                return result;
            },
        },
        beforeCreate() {
            this.$store.dispatch("getBilling");
        },
        methods: {
            fillData() {
                // console.log(Object.keys(this.fiveMostImportantPlaces))
                this.datacollection = {
                    labels: Object.keys(this.fiveMostImportantPlaces),
                    datasets: [
                        {
                            backgroundColor: ["#028090", "#00a896", "#02c39a", "#028090", "#00a896"],
                            data: Object.values(this.fiveMostImportantPlaces)
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
