<template>
  <div id="app" class="hero-image">
    <div id="nav">
          <v-app-bar
      dense
      dark
      absolute
      color="#fcb69f"
      scroll-target="#scrolling-techniques-2"
    >
<v-row justify="center">
  <v-col cols=3>
  <v-tab><router-link to="/shibuz">שיבוצים לשבוע הקרוב</router-link></v-tab>
  </v-col>
  <v-col cols=3>
  <v-tab><router-link to="/about">העמותות</router-link></v-tab>
  </v-col>
  <v-col cols=3>
  <v-tab><router-link to="/EductaionKatzin">הכנסת בקשות היחידות</router-link></v-tab>
  </v-col>
  <v-col cols=3>
  <v-tab><router-link to="/">דף הבית</router-link></v-tab>
  </v-col>

  
</v-row>

      
      
      </v-app-bar>
      
      
    </div>
    <v-content>
      <router-view/>
    </v-content>


  <v-footer
    color="primary lighten-1"
    padless
  >
    <v-row
      justify="center"
      no-gutters
    >
      <v-btn
        v-for="link in links"
        :key="link"
        color="white"
        text
        rounded
        class="my-2"
      >
        {{ link }}
      </v-btn>
      <v-col
        class="primary lighten-2 py-4 text-center white--text"
        cols="12"
      >
        <strong>TEAM 10</strong>
      </v-col>
    </v-row>
  </v-footer>

  </div>
</template>

<style lang="scss">

.hero-image {
  background-image: url("https://www.canadahelps.org/media/5-Reasons-Why-You-Should-Donate-to-Charity.jpg"); /* The image used */
  background-color: #eb1212; /* Used if the image is unavailable */
  height: 1000px; /* You must set a specified height */
  background-position: center; /* Center the image */
  background-repeat: no-repeat; /* Do not repeat the image */
  background-size: cover; /* Resize the background image to cover the entire container */
  }

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: black;
  font-family:monospace;
}
div.b{
  font-size: xx-large;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: white;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
