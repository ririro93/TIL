# transitions
> [vue docs](https://vuejs.org/v2/guide/transitions.html) <br>
> [youtube tutorial](https://www.youtube.com/watch?v=X4I6zUEM40A&list=PL4cUxeGkcC9ghm7-iTfS9n468Kp7l9Ipu&index=12)

## transition names
- `name-<enter, leave>-<from, to, active>`
- most times `name-enter-to` and `name-leave-from` are unneccessary because it's usually default
```html
<template>
    <transition name="fade">
        <h1>hello</h1>
    </transition>
</template>

<style>
.fade-enter-from, 
.fade-leave-to {
  opacity: 0;
}
.fade-enter-active,
.fade-leave-active {
  transition: all 2s ease;
}
</style>]
```

## transition-group, js hooks
- gsap can be used easily with js hooks
```html
<template>
    <transition-group 
      tag="ul"
      appear
      @before-enter="beforeEnter"
      @enter="enter"
    >
      <li v-for="(icon, idx) in icons" :key="icon.name" :data-idx="idx">
        <span class="material-icons">{{ icon.name }}</span>
        <div>{{ icon.text }}</div>
      </li>
    </transition-group>
</template>

<script>
import { ref } from 'vue'
import gsap from 'gsap'

export default {
  setup() {
    const icons = ref([
      { name: 'alternate_email', text: 'by email'},
      { name: 'local_phone', text: 'by phone'},
      { name: 'local_post_office', text: 'by post'},
      { name: 'local_fire_department', text: 'by smoke signal'},
    ])

    const beforeEnter = (ele) => {
      ele.style.opacity = 0
      ele.style.transform = 'translateY(100px)'
    }

    const enter = (ele, done) => {
      gsap.to(ele, {
        opacity: 1,
        y: 0,
        duration: 1,
        onComplete: done,
        delay: ele.dataset.idx * 0.2
      })
    }

    return {
      icons, 
      beforeEnter, enter
    }
  }
}
</script>
```

## route transitions
```html
<!-- App.vue -->

<template>
  <div id="nav">
    <router-link to="/">Home</router-link> |
    <router-link to="/about">About</router-link> | 
    <router-link to="/contact">Contact</router-link>
  </div>

  <router-view v-slot="{ Component }">
    <transition name="route" mode="out-in">
      <component :is="Component"></component>
    </transition>
  </router-view>
</template>

<style>
body {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin: 0;
  background: #f2f2f2;
}
#nav {
  padding: 30px;
}
#nav a {
  font-weight: bold;
  color: #2c3e50;
}
#nav a.router-link-exact-active {
  color: #42b983;
}

/* route transitions */
.route-enter-from {
  opacity: 0;
  transform: translateX(100px);
}
.route-enter-active {
  transition: all 0.3s ease-out;
}
.route-leave-to {
  opacity: 0;
  transform: translateX(-100px);
}
.route-leave-active {
  transition: all 0.3s ease-in;
}
</style>
```

