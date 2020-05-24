<template>
    <v-container>
        <v-row>
            <v-col :md="4" :sm="12" :xs="12">
                <Card>
                    <div class="pr-2">
                        <span class="font-weight-light display-2 mr-2">${{billing.total_bills}}</span>
                        <span class="headline font-weight-light">My Ballance</span>
                        <p v-if="toLimit > 0" class="font-weight-light">It's ${{toLimit}} below your limit!</p>
                        <p v-else class="font-weight-light">It's ${{Math.abs(toLimit)}} above your limit!</p>
                    </div>
                </Card>
            </v-col>
            <v-col :md="4" :sm="12" :xs="12">
                <Card>
                    <div class="pr-2">
                        <span class="font-weight-light display-2 mr-2">${{billing.limit}}</span>
                        <span class="headline font-weight-light">Limit</span>
                        <p class="font-weight-light">You can easily change your limit!</p>
                    </div>
                </Card>
            </v-col>
            <v-col :md="4" :sm="12" :xs="12">
                <Card>
                    <div class="pr-2">
                        <span class="font-weight-light display-2 mr-2">${{dailyTotal}}</span>
                        <span class="headline font-weight-light">Daily total</span>
                        <p class="font-weight-light">Your daily total expenses!</p>
                    </div>
                </Card>
            </v-col>
            <BillForm/>
        </v-row>
        <v-row justify="center">
            <v-col :md="4" :sm="12">
                <Card>
                    <div class="p-2">
                        <LineChart/>
                    </div>
                </Card>
            </v-col>
            <v-col :md="4" :sm="12">
                <Card>
                    <div class="p-2">
                        <BarChart/>
                    </div>
                </Card>
            </v-col>
            <v-col :md="4" :sm="12">
                <Card>
                    <div class="p-2">
                        <PieChart/>
                    </div>
                </Card>
            </v-col>
        </v-row>
    </v-container>
</template>

<script>
    import {mapGetters} from "vuex";
    import BillForm from "../components/BillForm";
    import Card from "../components/Card";
    import LineChart from "../components/TimeChart";
    import PieChart from "../components/PlaceChart";
    import BarChart from "../components/CategoriesChart";

    export default {
        name: "Dashboard",
        components: {Card, BillForm, PieChart, BarChart, LineChart},
        data: () => ({
            dialog: false,
        }),
        computed: {
            ...mapGetters({
                user: "getUser",
                loading: "loading",
                message: "getMessage",
                billing: "billing",
            }),
            toLimit() {
                return this.billing.limit - this.billing.total_bills;
            },

            dailyTotal() {
                if (!this.billing.total_daily) return 0;
                let result = 0;
                this.billing.total_daily.forEach(bill => result += bill.price);
                return result;
            }
        },
    }
</script>

<style scoped>
</style>