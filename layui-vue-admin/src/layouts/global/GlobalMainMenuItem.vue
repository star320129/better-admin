<template>
  <template v-for="(menu, index) in menus" :key="index">
    <lay-menu-item :id="menu.path">
      <template #icon>
        <lay-icon :type="menu.icon"></lay-icon>
      </template>
      <template #title>{{ menu.name }}</template>
    </lay-menu-item>
  </template>
</template>

<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  name: "GlobalMainMenuItem",
  props: {
    menus: {
      type: Object,
    },
  },
});
</script>
