drop table if exists todo;
create table todo (
  id integer primary key autoincrement,
  title text not null,
  description text not null
);