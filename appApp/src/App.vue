<template>
  <div id="app">
    <div id="nav">
          <v-app-bar
      color="green"
      dense
      dark
    >
    <v-app-bar-nav-icon></v-app-bar-nav-icon>
          <v-toolbar-title>עמותותות</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-heart</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>
      <router-link to="/">דף הבית</router-link> |
      <router-link to="/about">העמותות</router-link>|
      <router-link to="/shibuz">שיבוצים לשבוע הקרוב</router-link>
      </v-app-bar>
    </div>
    <router-view/>
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
