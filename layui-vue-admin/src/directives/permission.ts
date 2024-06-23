import { Directive } from 'vue';
import { useUserStore } from '../store/user';

export const permission: Directive = {
    mounted(el, binding) {
        toolPermission(el, binding);
    },
    updated(el, binding) {
        toolPermission(el, binding);
    }
}

const toolPermission = (el:any, binding:any) => {
    const { value } = binding;
    const userInfoStore = useUserStore();
    const permissions = userInfoStore.permissions;
    if (value && typeof value === 'object') {
        // const hasPermission = permissions.some((permission) => {
        //     return value.includes(permission);
        // })
        console.log(value)
        // console.log(permissions)
        const exists = permissions.some(permission =>
            Object.keys(value).every(key =>
                Object.keys(permission).includes(key) && permission[key] === value[key]
            )
        );
        console.log(exists)

        if (!exists) {
            el.parentNode && el.parentNode.removeChild(el);
        }
    }
}