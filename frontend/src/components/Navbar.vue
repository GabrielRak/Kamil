<template>
  <nav class="navbar flex items-center justify-between p-4">
    <div class="text-white text-lg font-bold">
      <span class="brand">
        <router-link to="/">KAMIL</router-link>
      </span>
    </div>
    <ul class="flex gap-4">
      <li><router-link class="text-white" to="/blog">Home</router-link></li>
      <li><router-link class="text-white" to="/about">About</router-link></li>
      <li>
        <router-link class="text-white" to="/dashboard">Carrers</router-link>
      </li>
    </ul>
    <div class="flex gap-4">
      <router-link class="text-white" to="/sign_in">Sign In</router-link>
      <router-link class="bg-blue-500 text-white" to="/sign_up"
        >Create</router-link
      >
    </div>
  </nav>
</template>

<script>
export default {
  name: "Navbar",
};
</script>

<style scoped>
.brand {
  text-transform: uppercase;
  font-family: "Poppins", sans-serif;
  font-style: normal;
  font-weight: 800;
  font-size: 32px;
  line-height: 48px;
  letter-spacing: 0.02em;
  background: linear-gradient(95.74deg, #9b51e0 -13.51%, #3081ed 144.21%);
  -webkit-text-fill-color: transparent;
  background-clip: text;

  flex: none;
  order: 0;
  flex-grow: 0;
}

.navbar ul {
  list-style: none;
  display: flex;
  gap: 1rem;
  margin: 0;
  padding: 0;
}

.navbar li {
  color: white;
}

.navbar a {
  color: white;
  text-decoration: none;
}

.navbar a:hover {
  text-decoration: underline;
}
</style>
