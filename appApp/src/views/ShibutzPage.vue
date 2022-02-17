<template>
<v-card>
  <v-data-table
    :headers="headers"
    :items="shibuzim"
    :items-per-page="5"
    class="elevation-1"
    :loading="loading"
  ></v-data-table>
<v-btn @click="submitMe()">שיבוץ חכם</v-btn>
</v-card>
</template>
<script>
import axios from 'axios';
  export default {
      

    data () {
      return {
        loading:false,
        headers: [
          {
            text: 'כמות אנשים',
            align: 'start',
            sortable: false,
            value: 'COUNT',
          },
          { text: 'יחידה ששובצה', value: 'UNIT' },
          { text: 'תאריך', value: 'DATE' },
          { text: 'עמותה', value: 'NAME' },
        ],
        shibuzim:[],
        // shibuzim: [
        //   {
        //     name: 'Help Edan Davidai',
        //     date: '35/5/2022',
        //     army_unit: 'matkal',
        //     count: '73'
        //   },
        //   {
        //     name: 'Help Edan Davidai',
        //     date: '35/5/2022',
        //     army_unit: 'matkal',
        //     count: '73'
        //   },
        //   {
        //     name: 'Help Edan Davidai',
        //     date: '35/5/2022',
        //     army_unit: 'matkal',
        //     count: '73'
        //   },
        //   {
        //     name: 'Help Edan Davidai',
        //     date: '35/5/2022',
        //     army_unit: 'matkal',
        //     count: '73'
        //   },
        //   {
        //     name: 'Help Edan Davidai',
        //     date: '35/5/2022',
        //     army_unit: 'matkal',
        //     count: '73'
        //   },
        // ],
      }
    },
            methods:{
            submitMe(){
                this.loading = true;
                                  const path = 'http://localhost:5000/getZivuog';
                  
            axios.get(path)
                .then((value) => {
                  console.log(value.data)
                  this.shibuzim = value.data
                  this.loading = false;
    // Swal("הצלחה!", "העמותה שרשמת נרשמה במערכת!", "success")
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
                this.loading = false;
                });
            }
        }
  }
</script>
