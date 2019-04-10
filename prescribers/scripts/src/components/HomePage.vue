<template>
  <div class="app">
    <div class="homepage">
      <h1>Prescribers</h1>
      <div>
        Sorting By: <b>{{ sortBy }}</b>, Sort Direction:
        <b>{{ sortDesc ? 'Descending' : 'Ascending' }}</b>
      </div>
       <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>
    <div style="text-align: left; max-width: 65px; padding-bottom: 5px;">
      <select class="custom-select" v-model="perPage" name="" id="">
        <option>25</option>
        <option>50</option>
        <option>100</option>
      </select>
      <button v-if="dataLoaded" @click="ExportCSV" style="margin-top: 10px; margin-bottom: 10px;" class="btn btn-info">Download <i class="fas fa-file-csv"></i></button>
    </div>
    <div style="margin:auto; max-width: 800px; padding-bottom: 5px; grid-template: auto auto auto/auto auto auto; display: grid; grid-column-gap: 10px;">
        <label style="padding: 0; margin: auto;" for="FilterText">Drug Name:</label>
        <label style="padding: 0; margin: auto;" for="FilterText">#Presciptions:</label>
        <label style="padding: 0; margin: auto;" for="FilterText">Opioid:</label>
        <input type="text" v-model="filterString" id='FilterText' class="form-control" aria-describedby="search" placeholder="Search">
        <input type="number" v-model="filterNumber" id='FilterText' class="form-control" aria-describedby="search" placeholder="Search">
        <select class="custom-select" v-model="filterBool" name="" id="">
          <option value="0">-</option>
          <option value="Yes">Yes</option>
          <option value="No">No</option>
        </select>

    </div>
       <b-table
        id="my-table"
        :items="items"
        :per-page="perPage"
        :current-page="currentPage"
        :fields="fields"
        :sort-by.sync="sortBy"
        :sort-desc.sync="sortDesc"
        :filter='filterText'
        :striped = 'true'
        :bordered = 'true'
        @filtered="onFiltered"
      >
        <template slot="doctorid" slot-scope="data">
          <router-link :to="{ name: 'Prescriber', params: {id: data.item.id}}">
            {{data.item.doctorid}}
          </router-link>          
        </template>
      
      </b-table>
      <div v-if="!dataLoaded">
        <b-spinner style="width: 4rem; height: 4rem;" label="Loading..."></b-spinner>
      </div>
      <b-pagination
      v-model="currentPage"
      :total-rows="rows"
      :per-page="perPage"
      aria-controls="my-table"
    ></b-pagination>
    <div style="text-align: left; max-width: 65px; padding-bottom: 5px;">
      <select class="custom-select" v-model="perPage" name="" id="">
        <option>25</option>
        <option>50</option>
        <option>100</option>
      </select>
    </div>
      
    </div>
  </div>
</template>

<script>
import { ExportToCsv } from 'export-to-csv';
export default {
  name: 'HomePage',
  data() {
      return {
        currentPage: 1,
        sortBy: 'risk_rank',
        perPage: 25,
        sortDesc: true,
        filterString: '',
        filterNumber: '',
        //rows: 1,
        filterBool: '',
        fields: [
          { key: 'doctorid', label: 'Doctor Id', sortable: true },
          { key: 'fname', label: 'First Name', sortable: true },
          { key: 'lname', label: 'Last Name', sortable: true },
          { key: 'gender', label: 'Gender', sortable: true },
          { key: 'overdoses__abbrev', label: 'State', sortable: true },
          { key: 'credentials', label: 'Credentials', sortable: true },
          { key: 'risk_rank', label: 'Risk Rank', sortable: true },
          { key: 'isoutlier', label: 'Over Prescriber', sortable: true },
          { key: 'totalprescriptions', label: 'Total Prescriptions', sortable: true },
          { key: 'numberofopioidsprescribed', label: 'Opioids Prescribed', sortable: true },
          { key: 'specialties__specialty', label: 'Specialty', sortable: true }
        ],
      }
    },
  computed: {
    userName() {
      return this.$store.getters.userName
    },
    items() {
      return this.$store.getters.prescribersList;
    },
    dataLoaded(){
      return this.$store.getters.prescribersList.length > 0
    },
    rows(){
      return this.$store.getters.prescribersList.length;
    },
    filterText(){
      if (this.filterString != '')
        return this.filterString;
      else if (this.filterNumber != '' && this.filterNumber !=0)
        return (this.filterNumber)
      else if(this.filterBool != '')
        return this.filterBool
    }

  },
  created(){
    this.$store.dispatch('getPrescribers');
  },
  mounted(){
    this.rows = this.items.length;
  },
  methods: {
    customFilter(item, filterText) {
      let numfilter = false;
      let boolfilter = false;
      let stringfilter = false;


      if (this.filterString == '' || item.drugname.toLowerCase().includes(this.filterString.toLowerCase()))
      {
        stringfilter = true;
      }

      if(this.filterBool == 0 || item.isopioid == this.filterBool)
      {
        boolfilter = true;
      }
      if(this.filterNumber == '' || item.total_prescriptions > this.filterNumber)
      {
        numfilter = true;
      }

      if(stringfilter && boolfilter && numfilter)
      {
        return true;
      }
      return false
    },
    onFiltered(filteredItems) {
        this.rows = filteredItems.length
        this.currentPage = 1
        console.log('testing')
      },
      ExportCSV(){
        let data = this.items;

        const options = { 
          fieldSeparator: ',',
          quoteStrings: '"',
          decimalSeparator: '.',
          showLabels: true, 
          showTitle: true,
          title: 'My Awesome CSV',
          useTextFile: false,
          useBom: true,
          useKeysAsHeaders: true,
          // headers: ['Column 1', 'Column 2', etc...] <-- Won't work with useKeysAsHeaders present!
        };
 
      const csvExporter = new ExportToCsv(options);
 
      csvExporter.generateCsv(data);
      }
  },
  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
