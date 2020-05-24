<script>
    import {Bar} from 'vue-chartjs'

    export default {
        extends: Bar,
        type: 'horizontalBar',
        data() {
            return {
                datacollection: null
            }
        },
        methods: {
            fillData() {
                this.datacollection = {
                    labels: ['Krakow', 'Warszawa', 'Others'],
                    datasets: [{
                        indexLabelFontColor: "red",
                        label: "Cities",
                        data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt()],
                        backgroundColor: ['#028090', '#00a896', '#02c39a']
                    }],
                };
                this.options =
                    {
                        title: {
                            text: "Places",
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
            getRandomInt() {
                return Math.floor(Math.random() * (50 - 5 + 1)) + 5
            }
        },
        mounted() {
            this.fillData()
            this.renderChart(this.datacollection, this.options)
        }
    }
</script>
