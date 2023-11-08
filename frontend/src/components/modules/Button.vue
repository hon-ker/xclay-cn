<template>
    <svg v-if="isActive1" @click="toggleActive(1)" class="svg-container with-icon_icon__MHUeb" data-testid="geist-icon"
      fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round"
      stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24" aria-hidden="true"
      style="color:currentColor;width:20px;height:20px">
      <path
        d="M6 17C4.89543 17 4 16.1046 4 15V5C4 3.89543 4.89543 3 6 3H13C13.7403 3 14.3866 3.4022 14.7324 4M11 21H18C19.1046 21 20 20.1046 20 19V9C20 7.89543 19.1046 7 18 7H11C9.89543 7 9 7.89543 9 9V19C9 20.1046 9.89543 21 11 21Z">
      </path>
    </svg>
    <svg v-if="isActive2" @click="toggleActive(2)" class="svg-container with-icon_icon__MHUeb" data-testid="geist-icon"
      fill="none" height="24" shape-rendering="geometricPrecision" stroke="currentColor" stroke-linecap="round"
      stroke-linejoin="round" stroke-width="1.5" viewBox="0 0 24 24" width="24" aria-hidden="true"
      style="color:currentColor;width:20px;height:20px">
      <path d="M20 6L9 17l-5-5"></path>
    </svg>
</template>
  
<script setup>
import { ref } from 'vue';

const isActive1 = ref(true);
const isActive2 = ref(false);

function toggleActive(svgIndex) {
  if (svgIndex === 1) {
    isActive1.value = !isActive1.value;
    isActive2.value = !isActive1.value;
  } else if (svgIndex === 2) {
    isActive2.value = !isActive2.value;
    isActive1.value = !isActive2.value;
  }
}
</script>
  
<style>
.svg-container {
  position: relative !important;
  width: 100px;
  ;
  height: 100px;
  ;
}

svg {
  position: absolute !important;
  ;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  transition: transform 0.3s ease !important;
  ;
  transform-origin: center !important;
  ;
}

.active {
  z-index: 1;
  transform: scale(1.2) !important;
  ;
}</style>