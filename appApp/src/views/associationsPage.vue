<template>
  <v-row justify="center">
    <v-col
      cols="4"
    ></v-col>
    <v-col
      cols="4"
    >
    <h1> הירשמו אלינו</h1>
      <v-card ref="form">
        <v-card-text>
            <v-form v-model="valid">
          <v-text-field
            ref="name"
            v-model="name"
            
            :error-messages="errorMessages"
            label="*שם העמותה"
            required
            :rules="nameRules"
          ></v-text-field>
          <v-text-field
            ref="location"
            v-model="location"
            :rules="[() => !!location|| 'This field is required']"
            :error-messages="errorMessages"
            label="*מיקום ההתנדבות"
            required
          ></v-text-field>
          <v-text-field
            ref="people_num"
            v-model="people_num"
            :rules="[() => !!people_num || 'This field is required', addressCheck]"
            label="כמות מתנדבים דרושה"
            required
          ></v-text-field>
          <v-text-field
            ref="activity_kind"
            v-model="activity_kind"
            :rules="[() => !!activity_kind || 'This field is required']"
            label="סוג הפעילות"
            required
          ></v-text-field>
          <v-text-field
            ref="phone_num"
            v-model="phone_num"
            :rules="[() => !!phone_num || 'This field is required']"
            label="מספר טלפון ליצירת קשר*"
            required
          ></v-text-field>
          <v-text-field
            ref="explanition"
            v-model="explanition"
            :rules="[() => !!explanition || 'This field is required']"
            :error-messages="errorMessages"
            label="הסבר קצר על העמותה"
            required
          ></v-text-field>
            <v-text-field
            ref="url"
            v-model="url"
            :error-messages="errorMessages"
            label="נתיב לתמונה ברשת"
            required
          ></v-text-field>
          <v-date-picker
            v-model="dates"
            multiple
          ></v-date-picker>
          <v-menu
            ref="menu"
            v-model="menu"
            :close-on-content-click="false"
            :return-value.sync="dates"
            transition="scale-transition"
            offset-y
            min-width="auto"
          >
            <template v-slot:activator="{ on, attrs }">
              <v-combobox
                v-model="dates"
                multiple
                chips
                small-chips
                label="Multiple picker in menu"
                prepend-icon="mdi-calendar"
                readonly
                v-bind="attrs"
                v-on="on"
              ></v-combobox>
            </template>
            <v-date-picker
              v-model="dates"
              multiple
              no-title
              scrollable
            >
              <v-spacer></v-spacer>
              <v-btn
                text
                color="primary"
                @click="menu = false"
              >
                Cancel
              </v-btn>
              <v-btn
                text
                color="primary"
                @click="$refs.menu.save(dates)"
              >
                OK
              </v-btn>
            </v-date-picker>
          </v-menu>
          </v-form>
        </v-card-text>
        <v-divider class="mt-12"></v-divider>
        <v-card-actions>
          <v-btn text>
            Cancel
          </v-btn>
          <v-spacer></v-spacer>
          <v-slide-x-reverse-transition>
            <v-tooltip
              v-if="formHasErrors"
              left
            >
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  icon
                  class="my-0"
                  v-bind="attrs"
                  @click="resetForm"
                  v-on="on"
                >
                  <v-icon>mdi-refresh</v-icon>
                </v-btn>
              </template>
              <span>Refresh form</span>
            </v-tooltip>
          </v-slide-x-reverse-transition>
          <v-btn
            color="primary"
            text
            @click="getMessage"
          >
            Submit
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-col>
    <v-col
      cols="12"
    ></v-col>
  </v-row>
</template>


<script>
import axios from 'axios';
import Swal from 'sweetalert';

  export default {
    components:{ },
    data: () => ({
      errorMessages: '',
      name: null,
      location: null,
      nameRules: [ v => !!v || 'Name is required'],
      people_num: null,
      activity_kind: null,
      url:null,
      valid:true,
      phone_num: null,
      explanition: null,
      formHasErrors: false,
      dates: [],
      menu: false,
    }),

    computed: {
      form () {
        return {
          name: this.name,
          location: this.location,
          people_num: this.people_num,
          activity_kind: this.activity_kind,
          url: this.url,
          phone_num: this.phone_num,
          explanition: this.explanition,
        }
      },
    },

    watch: {
      name () {
        this.errorMessages = ''
      },
    },

    methods: {
        getMessage() {
            if( this.valid == false){
                Swal("נכשל!", "יש להזין את שדות החובה במערכת!", "error")
                return
                
            }
            const path = 'http://localhost:5000/add';
            let x = Math.random() * 100;
            let dateFormat = []
            this.dates.forEach((dat)=>{
                dateFormat.push(new Date(dat).toLocaleDateString());
            })
            let obj = { "id": x.toString() , "name" : this.name , "location" : this.location, 
            "pepole_num" : this.people_num , "activity_kind" : this.activity_kind ,
            "phone_num" : this.phone_num , "explaination" : this.explanition,
            "dates" : dateFormat, "url_img": this.url }
            axios.post(path,obj )
                .then(() => {
    Swal("הצלחה!", "העמותה שרשמת נרשמה במערכת!", "success").then(() =>{
        this.$router.push('/')
    })
                })
                .catch((error) => {
                // eslint-disable-next-line
                console.log(error);
                });
},
        getMessages() {
            const path = 'http://localhost:5000/ping';
            axios.get(path).then((res) => 
            {
                this.msg = res.data;
            })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
      resetForm () {
        this.errorMessages = []
        this.formHasErrors = false

        Object.keys(this.form).forEach(f => {
          this.$refs[f].reset()
        })
      },
      submit () {
        this.formHasErrors = false

        Object.keys(this.form).forEach(f => {
          if (!this.form[f]) this.formHasErrors = true

          this.$refs[f].validate(true)
        })
      },
    },
  }
</script>
