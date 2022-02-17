<template>
  <v-row justify="center">
    <v-col
      cols="4"
    ></v-col>
    <v-col
      cols="4"
    >
    <h1>רישום היחידות שרוצות להתנדב</h1>
      <v-card ref="form">
        <v-card-text>
            <v-form v-model="valid">
          <v-text-field
            ref="unit"
            v-model="unit"
            :rules="[() => !!unit || 'This field is required']"
            :error-messages="errorMessages"
            label="שם היחידה"
            required
          ></v-text-field>
          <v-text-field
            ref="people_num"
            v-model="people_num"
            :rules="[() => !!people_num || 'This field is required', addressCheck]"
            label="כמות האנשים"
            required
          ></v-text-field>
          <v-text-field
            ref="explanition"
            v-model="explanition"
            :error-messages="errorMessages"
            label="דרישות היחידה במידה ויש"
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
            @click="submit"
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
import Swal from 'sweetalert';
  export default {
    data: () => ({
      errorMessages: '',
      name: null,
      location: null,
      people_num: null,
      activity_kind: null,
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
          phone_num: this.phone_num,
          explanition: this.explanition,
          valid:true
        }
      },
    },

    watch: {
      name () {
        this.errorMessages = ''
        
      },
    },

    methods: {
      resetForm () {
        this.errorMessages = []
        this.formHasErrors = false

        Object.keys(this.form).forEach(f => {
          this.$refs[f].reset()
        })
      },
      submit () {
          if(this.valid == false){
              Swal("נכשל!", "יש להזין את שדות החובה במערכת!", "error")
              return
          }
           this.$store.state.datesPick = []
        this.formHasErrors = false
        this.$store.commit("changeUnit",this.unit)
        this.$store.state.capacity = this.people_num
                    this.dates.forEach((dat)=>{
                this.$store.state.datesPick.push(new Date(dat).toLocaleDateString());
            })
        // this.$store.state.datesPick = this.dates
        this.$router.push('/ChooseAssociations')
        Object.keys(this.form).forEach(f => {
          if (!this.form[f]) this.formHasErrors = true

          this.$refs[f].validate(true)
        })
      },
    },
  }
</script>
