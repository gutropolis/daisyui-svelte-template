 
import { writable } from "svelte/store"
import { browser } from "$app/environment"

export const authToken = writable(browser && localStorage.getItem('authToken') || '');
export const refreshToken = writable(browser && localStorage.getItem('refreshToken') || '');

export function setTokens(token, refresh) {
    authToken.set(token);
    refreshToken.set(refresh);
    localStorage.setItem('authToken', token);
    localStorage.setItem('refreshToken', refresh);
}

export function clearTokens() {
    authToken.set('');
    refreshToken.set('');
    localStorage.removeItem('authToken');
    localStorage.removeItem('refreshToken');
}



