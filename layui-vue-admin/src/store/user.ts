import { defineStore } from 'pinia'
import { menu, permission } from "../api/module/user";

export const useUserStore = defineStore({
  id: 'user',
  state: () => {
    return {
      token: '',
      userInfo: {},
      permissions: [],
      menus: [],
    }
  },
  actions: {
    async loadMenus(){
      const data = await menu();
      if(data.status == 200) {
        this.menus = data.result;
      }
    },
    async loadPermissions(){
      const data = await permission();
      if(data.status == 200) {
        this.permissions = data.result;
      }
    }
  },
  persist: {
    storage: localStorage,
    paths: ['token', 'userInfo', 'permissions', 'menus' ],
  }
})