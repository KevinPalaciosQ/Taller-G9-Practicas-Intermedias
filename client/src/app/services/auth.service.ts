import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  private apiUrl = 'http://192.168.0.15:3001';

  constructor(
    private http: HttpClient
  ) { }

  register(body:any): Promise<any> {
    return this.http.post(`${this.apiUrl}/register`, body).toPromise();
  }

  login(body:any): Promise<any> {
    console.log(body);
    return this.http.post(`${this.apiUrl}/login`, body).toPromise();
  }

}
