<template>
    <div>
        <div v-if="!dataVisible">
            <b-spinner style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
        </div>
        <div v-if="dataVisible">
            <h1>Doctor {{this.prescriberLeft[0]['Doctor Id']}}</h1>
            <div style="display:grid; grid-template: auto auto/auto auto;">
                <div class="info-table">
                    <b-table stacked :bordered=true :items="prescriberLeft"></b-table>
                </div>
                <div class="info-table">
                    <b-table stacked :bordered=true :items="prescriber"></b-table>
                </div>
            </div>
        </div>
        <div class="container chart-container">
            <h3 v-if="dataVisible">Top {{drugsInGraph}} Drugs Prescribers by Doctor {{this.prescriber[0]['Doctor Id']}}</h3>
            <bar-chart
            v-if="dataVisible"
            :chartdata="chartdata"
            :options="options"
            />
        </div>
        <div v-if="dataVisible">
            <h4>All Drugs Prescribed by Doctor {{this.prescriber[0].doctorid}}</h4>
            <b-table
                id="my-table"
                :items="prescriberDrugsList"
                :fields="fields"
                :per-page="perPage"
                :current-page="currentPage"
                :sort-by.sync="sortBy"
                :sort-desc.sync="sortDesc"
                :filter='filterText'
                :striped = 'true'
                :bordered = 'true'
            >
                <template slot="opioids__drugname" slot-scope="data">
                    <a class="related-drug-link" :href="'/drugs#/items/' + data.item.opioids__id">
                        {{data.item.opioids__drugname}}
                    </a>
                </template>
                <template slot="opioids__isopioid" slot-scope="data">
                    {{data.item.opioids__isopioid == 1 ? 'Yes' : 'No'}}
                </template>
            </b-table>

            <b-pagination
            v-model="currentPage"
            :total-rows="prescriberDrugsList.length"
            :per-page="perPage"
            aria-controls="my-table"
            ></b-pagination>
        </div>
        
        
        
    </div>
</template>

<script>
    import axios from 'axios';
    axios.defaults.withCredentials = true;
    import BarChart from './BarChart.vue'
    export default {
        name: 'Prescirber',
        //fields: ['Drug Id', 'Drug Name', 'Opioid', 'Total Times Prescribed'],
        components: { BarChart },
        data() {
            return {
                test: 3,
                relatedItems: [],
                currentPage: 1,
                drugsInGraph: 5,
                sortBy: 'qty',
                sortDesc: true,
                filterText: '',
                perPage: 10,
                fields: [
          { key: 'opioids__drugname', label: 'Drug Name', sortable: true },
          { key: 'qty', label: 'Number of Prescriptions', sortable: true },
          { key: 'opioids__isopioid', label: 'Is Opioid', sortable: true },
        ],
                relatedItemsVisible: false,
                prescriberDrugsList: [],
                prescriber: [],
                prescriberLeft: [],
                dataVisible: false,
                loaded: false,
                chartdata: {
        labels: [],
        datasets: [{
            label: '# of Times Prescribed',
            data: [],
            backgroundColor: [
                'rgba(255, 99, 132, 0.2)',
                'rgba(54, 162, 235, 0.2)',
                'rgba(255, 206, 86, 0.2)',
                'rgba(75, 192, 192, 0.2)',
                'rgba(153, 102, 255, 0.2)',
                'rgba(255, 159, 64, 0.2)',
                'rgba(34,139,34, 0.2)',
                'rgba(128, 0, 0, 0.2)',
                'rgba(128, 128, 128, 0.2)',
                'rgba(0,255,255, 0.2)'
            ],
            borderColor: [
                'rgba(255, 99, 132, 1)',
                'rgba(54, 162, 235, 1)',
                'rgba(255, 206, 86, 1)',
                'rgba(75, 192, 192, 1)',
                'rgba(153, 102, 255, 1)',
                'rgba(255, 159, 64, 1)',
                'rgba(34,139,34, 1)',
                'rgba(128, 0, 0, 1)',
                'rgba(128, 128, 128, 1)',
                'rgba(0,255,255, 1)'
            ],
            borderWidth: 1
        }]
    },
    options: {
        scales: {
            yAxes: [{
                ticks: {
                    beginAtZero: true
                }
            }]
        },
         onClick: function(event, i){
             console.log('it worked!!!!!!')
             console.log(event)
             console.log(i)
              let e = i[0];
            console.log(e._index)
            var x_value = this.data.labels[e._index];
            var y_value = this.data.datasets[0].data[e._index];
            console.log(x_value);
            console.log(y_value);
         }
    }
            }
        },
        created(){
            this.getData()
        },
        watch: {
            '$route' (to, from) {
                this.getData();
            }
        },
        methods: {
            getRandomInt () {
                return Math.floor(Math.random() * (50 - 5 + 1)) + 5
            },
            getData(){
                this.dataVisible = false;
                this.chartdata.labels = []
                this.chartdata.datasets[0].data = []
                axios.get('/prescribers/index.prescriber/'+this.$route.params.id).then(res => {
                    let pdataLeft = {
                        'Doctor Id': res.data.PrescriberDataLeft[0].doctorid,
                        'First Name': res.data.PrescriberDataLeft[0].fname,
                        'Last Name': res.data.PrescriberDataLeft[0].lname,
                        'Total Prescriptions': res.data.PrescriberDataLeft[0].totalprescriptions,
                        'Opioids Prescribed': res.data.PrescriberDataLeft[0].numberofopioidsprescribed,
                        'Credentials': res.data.PrescriberDataLeft[0].credentials,
                    }
                    let pdata = {
                        'Gender': res.data.PrescriberData[0].gender,
                        'State': res.data.PrescriberData[0].overdoses__abbrev,
                        'Specialty': res.data.PrescriberData[0].specialties__specialty,
                        'Opioid Prescriber': res.data.PrescriberData[0].opioid_prescriber == 1 ? 'Yes': 'No',
                        'Risk Rank': res.data.PrescriberData[0].risk_rank,
                        'High Risk': res.data.PrescriberData[0].isoutlier == true ? 'Yes': 'No'
                    }
                    this.prescriber = [];
                    this.prescriberLeft = [];
                    this.prescriber.push(pdata);
                    this.prescriberLeft.push(pdataLeft);
                    this.prescriberDrugsList = res.data.drugs;

                    let countTo = res.data.drugs.length;
                    if (countTo > 10) 
                            countTo = 10;
                    
                    this.drugsInGraph = countTo

                    for (let i = 0; i < countTo; i++){
                        this.chartdata.labels.push(res.data.drugs[i].opioids__drugname);
                        this.chartdata.datasets[0].data.push(res.data.drugs[i].qty)
                    }
                    this.dataVisible = true;   
            }).catch(err => {
                console.log(err);
            })
            },
            
        },
    }
</script>

<style scoped>
.chart-container{
    width: 45%;
}
.info-table{
    margin-bottom: 50px;
}
.card-container{
    display: grid;
    grid-template: auto auto auto auto auto/ auto auto auto auto auto;
    grid-column-gap: 5px;
}
.related-drug-link{
    color: black;
    text-decoration: none;
}
.related-drug-link:hover{
    text-decoration: underline;
}
</style>