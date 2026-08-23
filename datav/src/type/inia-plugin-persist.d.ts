declare module 'pinia-plugin-persist' {
  import { PiniaPlugin } from 'pinia';

  interface PersistOptions {
    key?: string;
    storage?: Storage;
    paths?: string[];
  }

  export function createPersistedState(options?: PersistOptions): PiniaPlugin;
}