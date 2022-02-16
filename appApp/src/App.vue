<template>
  <div id="app">
    <div id="nav">
          <v-app-bar
      dense
      dark
      absolute
      color="#fcb69f"
      src="https://picsum.photos/1920/1080?random"
      scroll-target="#scrolling-techniques-2"
    >

      <router-link to="/">דף הבית</router-link> |
      <router-link to="/about">העמותות</router-link>|
      <router-link to="/shibuz">שיבוצים לשבוע הקרוב</router-link>
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
        {{ new Date().getFullYear() }} — <strong>Vuetify</strong>
      </v-col>
    </v-row>
  </v-footer>

  <v-parallax
    height="300"
    src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
  ></v-parallax>
  </div>
</template>

<style lang="scss">
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;

  a {
    font-weight: bold;
    color: #2c3e50;

    &.router-link-exact-active {
      color: #42b983;
    }
  }
}
</style>
