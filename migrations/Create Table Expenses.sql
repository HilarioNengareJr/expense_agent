create table if not exists expenses (
  id bigint primary key generated always as identity,
  amount float not null,
  category text not null,
  date date not null,
  inserted_at timestamp with time zone default timezone('utc', now())
)