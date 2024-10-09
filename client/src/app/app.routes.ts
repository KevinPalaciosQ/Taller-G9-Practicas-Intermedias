import { Routes } from '@angular/router';

// Rutas Padres
export const routes: Routes = [
    {
        path: '', // Ruta raíz (predeterminada)
        redirectTo: '/auth',
        pathMatch: 'full'
    },
    {
        path: 'auth',
        loadChildren: () => import('./auth/auth.routes')
    },
    {
        path: 'dashboard',
        loadComponent: () => import('./dashboard/home/home.component').then(m => m.default)
    },
    {
        path: '**', // Cualquier ruta no encontrada
        redirectTo: '/dashboard'
    }
];
