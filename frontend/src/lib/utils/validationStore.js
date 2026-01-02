// src/lib/validationStore.js
import { writable } from 'svelte/store';

// Create a store to manage validation messages
const validationMessages = writable({});

export function setValidationMessage(field: any, message: any) {
  // Set validation message for a specific field
  // validationMessages.update(messages => ({
  //   ...messages,
  //   [field]: message
  // }));
}

export function clearValidationMessages() {
  // Clear all validation messages
  // validationMessages.set({});
}

export { validationMessages };