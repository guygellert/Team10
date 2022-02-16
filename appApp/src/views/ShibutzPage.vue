<template>
  <v-data-table
    :headers="headers"
    :items="shibuzim"
    :items-per-page="5"
    class="elevation-1"
  ></v-data-table>
</template>



<script>
  export default {
    data () {
      return {
        headers: [
          {
            text: 'כמות אנשים',
            align: 'start',
            sortable: false,
            value: 'count',
          },
          { text: 'יחידה ששובצה', value: 'army_unit' },
          { text: 'תאריך', value: 'date' },
          { text: 'עמותה', value: 'name' },
        ],
        shibuzim: [
          {
            name: 'Help Edan Davidai',
            date: '35/5/2022',
            army_unit: 'matkal',
            count: '73'
          },
          {
            name: 'Help Edan Davidai',
            date: '35/5/2022',
            army_unit: 'matkal',
            count: '73'
          },
          {
            name: 'Help Edan Davidai',
            date: '35/5/2022',
            army_unit: 'matkal',
            count: '73'
          },
          {
            name: 'Help Edan Davidai',
            date: '35/5/2022',
            army_unit: 'matkal',
            count: '73'
          },
          {
            name: 'Help Edan Davidai',
            date: '35/5/2022',
            army_unit: 'matkal',
            count: '73'
          },
        ],
      }
    },
  }
</script>
