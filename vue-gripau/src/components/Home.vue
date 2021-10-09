<template>
  <div id="app">
    <h1> {{ message }} </h1>
    <button class="btn btn-primary btn-lg" @click="onUserProfile()"> User Profile </button>
    <button class="btn btn-primary btn-lg"> Register </button>
  </div>
</template>

<script>

export default {
  data () {
    return {
      message: 'Home'
    }
  },
  methods: {
    onUserProfile () {
      this.$router.replace({ path: '/user' })
    }
  }
}

</script>
