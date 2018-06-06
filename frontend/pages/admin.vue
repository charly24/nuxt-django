<template>
  <v-flex xs12 sm8 md4>
    <p>
    Admin Page
    </p>
    <p v-if="this.$auth.hasScope('admin')">
      Secret Area
    </p>
  </v-flex>
</template>

<script>
export default {
  middleware: 'auth'
}
</script>