<template>

  <head>
      <meta charset="utf-8">
      <link rel="shortcut icon" type="image/png" href="require('../assets/favicon.png')"/>
      <title>Jobify</title>
  </head>

  <router-view/>
</template>

<script>
export default {
  name: 'App',
  watch: {
    $route: {
      immediate: true,
      handler (to, from) {
        document.title = to.meta.title || 'Jobify'
      }
    }
  }
}
</script>

<style>
#app {
  font-family: 'Work Sans', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
@font-face {
  font-family: "Work Sans";
  src: local("Work Sans"),
  url(./fonts/WorkSans/WorkSans-Regular.ttf) format("truetype");
}
@font-face {
  font-family: "Work Sans SemiBold";
  src: local("Work Sans SemiBold"),
  url(./fonts/WorkSans/WorkSans-SemiBold.ttf) format("truetype");
}
@font-face {
  font-family: "Montserrat";
  src: local("Montserrat"),
  url(./fonts/Montserrat/Montserrat-SemiBold.ttf) format("truetype");
}
@font-face {
  font-family: "Vollkorn";
  src: local("Vollkorn"),
  url(./fonts/Vollkorn/Vollkorn-ExtraBold.ttf) format("truetype");
}
@font-face {
  font-family: "Bright";
  src: local("Bright"),
  url(./fonts/Bright/Bright.otf) format("truetype");
}
</style>
