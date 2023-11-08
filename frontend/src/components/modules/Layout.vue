<template>
  <header>
    <slot name="header">
      <Header></Header>
    </slot>
  </header>
  <main>
    <slot name="main">
      <Main></Main>
    </slot>

  </main>
  <footer>
    <slot name="footer">
      <Footer></Footer>
    </slot>
  </footer>
</template>
<script setup>
import { NLayoutHeader, NLayoutContent, NLayoutFooter, NLayout } from 'naive-ui';
import Header from './Header.vue';
import Footer from './Footer.vue';
import Main from './Main.vue';
</script>
  
<style scoped></style>