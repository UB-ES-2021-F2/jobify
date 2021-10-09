<template>
  <router-view/>
</template>

<script>
export default {
  name: 'App'
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
  url(./fonts/WorkSans/WorkSans-Medium.ttf) format("truetype");
}
@font-face {
  font-family: "Work Sans SemiBold";
  src: local("Work Sans"),
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
</style>
