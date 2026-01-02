import { writable } from "svelte/store";
import { bubble, listen } from "svelte/internal";
export default function clickedOutside() {
  if (!window) return writable(false);

  const store = writable(false);

  return {
    subscribe: store.subscribe,
    action: function(node) {
      const onClick = ({ target }) => store.set(!node.contains(target));

      window.addEventListener("click", onClick);

      return {
        destroy: () => window.removeEventListener("click", onClick)
      };
    }
  };
}

export function getEventsAction(component) {
  return node => {
    const events = Object.keys(component.$$.callbacks);
    const listeners = [];
    events.forEach(event =>
      listeners.push(listen(node, event, e => bubble(component, e)))
    );
    return {
      destroy: () => {
        listeners.forEach(listener => listener());
      }
    };
  };
}