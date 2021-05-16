# Vueuse
> [docs](https://vueuse.org/)
- collection of vue utilities

## UseCookies
```js
import { useCookies } from '@vueuse/integrations'

const cookies = useCookies(['locale'])
const csrftoken = cookies.get('csrftoken')
```