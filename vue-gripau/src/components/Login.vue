<template>
  <div id="app">
    <div class = 'container'>
      <div class = 'row justify-content-center'>
        <div class= 'content-table'>
          <div class  = 'content-table-cell'>
            <div class = 'col-5 login-container '>
             <div>
               <img style="max-width: 150px" :src="require('../assets/logo.svg')">
             </div>
              <div>
                <input type = 'text' placeholder="Username">
              </div>
              <div>
                <input type = 'password' placeholder="Password">
              </div>
              <div>
                <button class='btn-login'> Login </button>
              </div>
            </div>
          </div>
        </div>

      </div>
    </div>

  </div>
</template>

<script>
export default {
  name: 'Login'
}
</script>

<style scoped>
</style>
