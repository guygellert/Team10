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
    </v-card-actions>
  </v-card>
  </v-row>
         </v-col>
  </v-row>
</template>

<script>
import axios from 'axios';
  export default {
    data(){
      return{
        listOfVolunteer:[],
        listRequest: []
      }
    },
    methods:{
          addToList(item){
        this.listRequest.push(item)
      }
    },
    created()
    {
                  const path = 'http://localhost:5000/allAssociations';
                //   let asocciations =[]
                //   let dates = [ "01.02.2022" , ]
            // let obj = { "dates": JSON.stringify(dates) }
            axios.get(path)
                .then((value) => {
                  console.log(value.data)
                //   asocciations = value.data;
                  this.listOfVolunteer = value.data
                 
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
                });
    }
  }
</script>

