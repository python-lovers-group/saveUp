<template>
    <div small>
        <pie-chart :chart-data="datacollection"></pie-chart>
        <button @click="fillData()">Randomize</button>
    </div>
</template>

<script>
    import PieChart from '../assets/charts/PieChart.js'

    export default {
        components: {
            PieChart
        },
        data() {
            return {
                datacollection: null
            }
        },
        mounted() {
            this.fillData()
        },
        methods: {
            fillData() {
                this.datacollection = {
                    labels: ['Food', 'Health', 'Other'],
                    datasets: [
                        {
                            backgroundColor: [
                                '#00ffe4','#00a896','#006e5c'
                            ],
                            data: [this.getRandomInt(), this.getRandomInt(), this.getRandomInt()]
                        }
                    ]
                }
            },
            getRandomInt() {
                return Math.floor(Math.random() * (50 - 5 + 1)) + 5
            }
        }
    }
</script>

<style>
    .small {
        max-height: 300px;
        max-width: 600px;
        margin: 150px auto;
    }
</style>
