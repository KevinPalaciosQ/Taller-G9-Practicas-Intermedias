import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = 'http://localhost:3000';

  constructor(
    private http: HttpClient
  ) { }

  register(body:any): Promise<any> {
    return this.http.post(`${this.apiUrl}/register`, body).toPromise();
  }

  login(body:any): Observable<any> {
    return this.http.post(`${this.apiUrl}/login`, body);
  }

}
