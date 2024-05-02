
## 1
### docker-compose up
swagger http://localhost:8000/docs

env приложен в ознакомительных целях
## 2
```
create table short_names (name text not null, status int not null, primary key (name));
create table full_names (name text not null, status int, primary key (name));

insert into short_names (name, status)
select
    'test' || i,
    round(random())
from
    generate_series(1, 500000) as i
limit 500000;

insert into full_names (name)
select
    'test' || i || '.mp3'
from
    generate_series(1, 700000) as i
limit 700000;

update full_names
set status = short_names.status
from short_names
where split_part(full_names.name, '.', 1) = short_names.name;
```

или

```
update full_names fn
set status = sn.status
from short_names sn
where regexp_replace(fn.name, E'\\.[^.]+$', '') = sn.name;

если есть . в имени файла
```