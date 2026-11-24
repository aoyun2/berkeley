create table books as
  select 'Dune' as title, 'Herbert' as author, 1965 as year, 412 as pages union
  select 'Emma', 'Austen', 1815, 474 union
  select 'Persuasion', 'Austen', 1817, 249 union
  select 'Ubik', 'Dick', 1969, 202 union
  select 'Valis', 'Dick', 1981, 271 union
  select 'Kindred', 'Butler', 1979, 264 union
  select 'Dawn', 'Butler', 1987, 248;
create table loans as
  select 'Dune' as title, 'Ana' as member, 14 as days union all
  select 'Emma', 'Ben', 21 union all
  select 'Dune', 'Chen', 7 union all
  select 'Ubik', 'Ana', 10 union all
  select 'Kindred', 'Ben', 14 union all
  select 'Kindred', 'Dev', 30 union all
  select 'Dawn', 'Ana', 5;
