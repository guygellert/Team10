<template>
  <v-row justify="center" >
    <v-col 
      cols="4"
     ></v-col>
  <v-card v-for="item in listOfVolunteer" :key="item.id"
    class="mx-auto"
    max-width="344"
    outlined
  >
    <v-list-item three-line>
      <v-list-item-content>
        <div class="text-overline mb-4">
          {{ item.name }}
        </div>
        <v-list-item-title class="text-h5 mb-1">
          {{ item.explaination}}
        </v-list-item-title>
        <v-list-item-subtitle>{{ item.date }} </v-list-item-subtitle>
      </v-list-item-content>

      <v-list-item-avatar
        tile
        size="80"
        color="grey"
      ></v-list-item-avatar>
    </v-list-item>

    <v-card-actions>
      <v-btn
      @click="addToList(item)"
        outlined
        rounded
        text
        center
      >
      <v-icon> mdi-checkbox-marked-circle</v-icon>
        Button
      </v-btn>
    </v-card-actions>
  </v-card>

  <v-btn @click="SaveRequest">Submit</v-btn>
  </v-row>
</template>

<script>
import axios from 'axios';
// import Swal from 'sweetalert';
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
                date: new Date().toLocaleDateString(),
                army_unit: 'mamram'
              })
            })
                            axios.post(path,newListWithId )
                .then(() => {
    // Swal("הצלחה!", "העמותה שרשמת נרשמה במערכת!", "success")
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
                  
                  let dates = ["17.02.2022", "31.12.2022"]
            let obj = { "dates": JSON.stringify(dates) }
            axios.get(path,  {params: obj })
                .then((value) => {
                  console.log(value.data)
                  this.listOfVolunteer = value.data
    // Swal("הצלחה!", "העמותה שרשמת נרשמה במערכת!", "success")
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
                });
    }
  }
</script>

