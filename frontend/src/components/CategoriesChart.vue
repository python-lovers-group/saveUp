<script>
    import {Bar} from 'vue-chartjs'
    import {mapGetters} from "vuex";

    export default {
        extends: Bar,
        type: 'horizontalBar',
        data() {
            return {
                datacollection: null
            }
        },
        computed: {
            ...mapGetters({
                categories: "categories",
            }),
            categoriesToDisplay() {
                function isUsed(category) {
                    if (category.category_total > 0) {
                        return category;
                    }
                }

                function compareCategories(a, b) {
                    return b.category_total - a.category_total
                }

                let result = this.categories.filter(isUsed);
                console.log(result);
                if (result.length > 5) {
                    result = result.sort(compareCategories).slice(0, 5)
                }
                return result
            },
            categoriesNames() {
                let result = this.categoriesToDisplay.map(category => {
                    return category.name
                })
                return result
            },
            categoriesTotals() {
                let result = this.categoriesToDisplay.map(category => {
                    return category.category_total
                })
                return result
            }
        },
        beforeCreate() {
            this.$store.dispatch("getCategories");
        },
        methods: {
            fillData() {
                this.datacollection = {
                    labels: this.categoriesNames,
                    datasets: [{
                        label: "Categories",
                        data: this.categoriesTotals,
                        backgroundColor: ['#02c39a', '#028090', '#00a896', '#028090', '#00a896']
                    }],
                };
                this.options =
                    {
                        title: {
                            text: "Categories",
                            display: true,
                            fontColor: "#e5e5e5",
                            fontSize: 15
                        },
                        scales: {
                            yAxes: [{
                                ticks: {
                                    fontColor: "#e5e5e5",
                                }
                            }],
                            xAxes: [{
                                ticks: {
                                    fontColor: "#e5e5e5",
                                }
                            }]
                        },
                        legend: {
                            labels: {
                                fontColor: "#e5e5e5"
                            }
                        }
                    }
            },
        },
        mounted() {
            this.fillData()
            this.renderChart(this.datacollection, this.options)
        }
    }
</script>
