<template>
    <div small>
        <line-chart :chart-data="datacollection"></line-chart>
        <button @click="fillData()">Randomize</button>
    </div>
</template>

<script>
    import LineChart from '../assets/charts/LineChart.js'

    export default {
        components: {
            LineChart
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
                    labels: [this.getRandomInt(), this.getRandomInt()],
                    datasets: [
                        {
                            label: 'April',
                            borderColor: '#00ffe4',
                            data: [this.getRandomInt(), this.getRandomInt()]
                        }, {
                            label: 'May',
                            borderColor: '#00a896',
                            data: [this.getRandomInt(), this.getRandomInt()]
                        }, {
                            label: 'June',
                            borderColor: '#006e5c',
                            data: [this.getRandomInt(), this.getRandomInt()]
                        }
                    ],
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
