<template>
  <v-flex xs12 sm8 md4>
    General Page
    <v-btn to="/admin">Admin</v-btn>
  </v-flex>
</template>

<script>
export default {
  middleware: 'auth'
}
</script>