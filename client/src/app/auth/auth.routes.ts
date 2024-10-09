import { Routes } from '@angular/router';

// Rutas hijas de 'auth'
export default [
    {
        path: '', // Ruta raíz dentro de 'auth'
        redirectTo: 'login',
        pathMatch: 'full'
    },
    {
        path: 'login',
        loadComponent: () => import('./features/login/login.component')
    },
    {
        path: 'sign-up',
        loadComponent: () => import('./features/sign-up/sign-up.component')
    }
] as Routes;