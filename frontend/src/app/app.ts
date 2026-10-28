import { Component, afterNextRender, inject, signal } from '@angular/core';
import { NonNullableFormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { RouterOutlet } from '@angular/router';
import { ActivityLevel, Sex, User, UsersService } from './users.service';

@Component({
  imports: [RouterOutlet, ReactiveFormsModule],
  selector: 'app-root',
  styleUrl: './app.css',
  templateUrl: './app.html',
})
export class App {
  private readonly usersService = inject(UsersService);
  private readonly fb = inject(NonNullableFormBuilder);

  protected readonly users = signal<User[]>([]);
  protected readonly error = signal<string | null>(null);

  protected readonly form = this.fb.group({
    name: ['', Validators.required],
    surname: ['', Validators.required],
    email: ['', [Validators.required, Validators.email]],
    birth_date: ['', Validators.required],
    weight_kg: [70, [Validators.required, Validators.min(1), Validators.max(499)]],
    height_cm: [175, [Validators.required, Validators.min(1), Validators.max(299)]],
    activity: ['moderate' as ActivityLevel, Validators.required],
    sex: ['male' as Sex, Validators.required],
  });

  constructor() {
    afterNextRender(() => this.loadUsers());
  }

  private loadUsers() {
    this.usersService.list().subscribe({
      next: (users) => this.users.set(users),
      error: () => this.error.set('Failed to load users'),
    });
  }

  protected submit() {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }
    this.usersService.create(this.form.getRawValue()).subscribe({
      next: (user) => {
        this.users.update((list) => [...list, user]);
        this.form.reset();
        this.error.set(null);
      },
      error: (err) =>
        this.error.set(err.status === 409 ? 'This email is already taken' : 'Failed to add user'),
    });
  }
}