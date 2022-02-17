<template>
  <v-row justify="center" >
    <v-col 
      cols="1"
     ></v-col>
         <v-col 
      cols="10">
      <v-row>
  <v-card v-for="item in listOfVolunteer" :key="item.id"
    class="mx-auto"
    max-width="344"
    outlined
  >
    <v-list-item three-line>
      <v-list-item-content>
                <v-row justify="center">
                  <v-col></v-col>
                  <v-col>
          <v-img :src="item.url_img" width="150" height="150"></v-img>
          </v-col>
          <v-col></v-col>
        </v-row>
        <div class="text-overline mb-4">
          {{ item.name }} - {{ item.date }}
        </div>
        <v-list-item-title class="text-h5 mb-1">
          {{ item.explaination}}
        </v-list-item-title>
        <v-list-item-subtitle> {{ item.location }} </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar
        tile
        size="80"
        color="grey"
      ></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-checkbox
      @click="addToList(item)"
      class="ma-2"
      
      label="אני רוצה להתנדב לכאן!!"
      color="green"
      >
      <!-- <v-icon> mdi-checkbox-marked-circle</v-icon> -->
        בא לי כאן!!
      </v-checkbox>
    </v-card-actions>
  </v-card>
  </v-row>
         </v-col>
  <v-btn @click="SaveRequest">Submit</v-btn>
  </v-row>
</template>

<script>
import axios from 'axios';
import Swal from 'sweetalert';
  export default {
    data(){
      return{
        listOfVolunteer:[],
        listRequest: []
      }
    },
    methods:{
      SaveRequest(){
                    const path = 'http://localhost:5000/addReq';
            let x;
            let newListWithId =[];
            this.listRequest.forEach((req) =>{
              x = Math.random() * 100;
              newListWithId.push({
                "id" : x.toString(),
                name : req.name,
                count : this.$store.state.capacity,
                date: req.date,
                army_unit: this.$store.state.unit
              })
            })
                            axios.post(path,newListWithId )
                .then(() => {
    Swal("הצלחה!", "בקשה נשלחה לעמותה!", "success").then(()=>{
      this.$router.push('/')
    })
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
                });
      },
      addToList(item){
        this.listRequest.push(item)
      }
    },
    created()
    {
                  const path = 'http://localhost:5000/getAssociations';
                  
                  let dates = this.$store.state.datesPick
            let obj = { "dates": JSON.stringify(dates) }
            axios.get(path,  {params: obj })
                .then((value) => {
                  console.log(value.data)
                  let listOfAmotot = value.data;
                  let amotoDates =[]
                  listOfAmotot.forEach(amota =>{
                    amota.dates.forEach((dat)=>{
                      amotoDates.push({"date": dat,
                                                ...amota})
                    })
                  })

                  this.$store.state.datesPick.forEach((d) =>{
                    amotoDates.forEach((datesAmo) =>{
                      if(datesAmo.date == d){
                        this.listOfVolunteer.push(datesAmo)
                      }
                    })
                  })
                  
                  // this.listOfVolunteer = value.data
    // Swal("הצלחה!", "העמותה שרשמת נרשמה במערכת!", "success")
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
                });
    }
  }
</script>

