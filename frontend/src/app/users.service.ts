import { HttpClient } from '@angular/common/http';
import { Injectable, inject } from '@angular/core';
import { API_URL } from '../environments/api-url';

export type ActivityLevel = 'sedentary' | 'light' | 'moderate' | 'active' | 'very_active';
export type Sex = 'male' | 'female' | 'other';

export interface NewUser {
  name: string;
  surname: string;
  email: string;
  birth_date: string;
  weight_kg: number;
  height_cm: number;
  activity: ActivityLevel;
  sex: Sex;
}

export interface User extends NewUser {
  id: string;
  bmi: number;
  created_at: string;
}

@Injectable({ providedIn: 'root' })
export class UsersService {
  private readonly http = inject(HttpClient);

  list() {
    return this.http.get<User[]>(`${API_URL}/users`);
  }

  create(user: NewUser) {
    return this.http.post<User>(`${API_URL}/users`, user);
  }
}