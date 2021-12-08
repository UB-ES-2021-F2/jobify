<template>
  <div>
    <head>
        <meta charset="utf-8">
        <link rel="shortcut icon" type="image/png" href="require('../assets/favicon.png')"/>
        <title>Jobify</title>
    </head>
    <router-view style="min-height: 100vh"/>
    <b-card-footer footer-bg-variant="dark" footer-text-variant="white" title="Footer" style="font-family:'Work Sans', Helvetica, Arial, sans-serif; margin-top: 20px">
      <div style="padding-inline: 10%">
        <b-container>
          <b-row>
            <b-col style="flex-grow: 0">
              <img style="max-width: 150px" :src="require('./assets/logoWhite.png')">
            </b-col>
            <b-col align-self="center" >
              <b-card-text>
                <p style="margin-bottom: 0.3rem">
                  This website has been created for educational purposes only.
                </p>
                <p style="margin: 0">
                  If you have any questions or suggestions, please don't hesitate to <b><a style="color: white" href="#" @click="onAboutUs" >contact us.</a></b>
                </p>
              </b-card-text>
            </b-col>
          </b-row>
        </b-container>
        <hr style="background-color: #ffc107" />
        <div align="center">
          <b>Jobify 2021</b> - University of Barcelona
        </div>
      </div>
    </b-card-footer>
  </div>
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
  },
  methods: {
    onAboutUs () {
      this.$router.push('/about_us')
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
