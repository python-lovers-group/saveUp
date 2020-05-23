import {Bar, mixins} from 'vue-chartjs'

const {reactiveProp} = mixins

export default {
    extends: Bar,
    mixins: [reactiveProp],
    props: {
        options: {
            title: {
                text: "Places",
                display: true
            },
            legend: {
                labels: {
                    fontColor: '#e5e5e5'
                }
            }
        }
    },
    mounted() {
        // this.chartData is created in the mixin.
        // If you want to pass options please create a local options object
        this.renderChart(this.chartData, this.options)
    },
}