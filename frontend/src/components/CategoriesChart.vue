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
            categoriesNames() {
                let result = [];
                this.categories.forEach(category => result.push(category.name));
                return result;
            },
            categoriesTotals() {
                let result = [];
                this.categories.forEach(category => result.push(category.category_total));
                console.log(result);
                return result;
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
                        // backgroundColor: ['#028090', '#00a896', '#02c39a']
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
