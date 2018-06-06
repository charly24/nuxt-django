<template>
  <v-app>
    <v-content>
      <v-container fluid fill-height>
        <v-layout align-center justify-center>
          <nuxt/>
          <v-btn v-if="$auth.loggedIn" @click="logout()" href="#">Logout</v-btn>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
export default {
  methods: {
    logout () {
      this.$auth.logout()
      this.$nuxt.$router.push('/')
    }
  }
}
</script>
