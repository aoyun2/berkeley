-- CS 61A Week 13 exercises: solutions. Tables are in ../exercises/data.sql.

-- E1. Titles of books with more than 260 pages, longest first; break equal-page ties by title.
create table e1 as
  select title from books where pages > 260 order by pages desc, title;

-- E2. Each author with number of books and total pages (authors with at least two books), by author.
create table e2 as
  select author, count(*) as n, sum(pages) as total from books
    group by author having count(*) >= 2 order by author;

-- E3. For each loan: member, title, author.
create table e3 as
  select member, l.title, author from loans as l join books as b on l.title = b.title;

-- E4. Pairs of different books by the same author, each pair once.
create table e4 as
  select a.title as first, b.title as second from books as a, books as b
    where a.author = b.author and a.title < b.title;

-- E5. The member with the most total loan days, and the total; break ties alphabetically by member.
create table e5 as
  select member, sum(days) as total from loans group by member order by total desc, member limit 1;

-- E6. Authors whose books were borrowed by at least two different members.
create table e6 as
  select author from books as b join loans as l on b.title = l.title
    group by author having count(distinct member) >= 2;

-- E7. Decade of each book with the number of books from it, oldest first.
create table e7 as
  select year/10*10 as decade, count(*) as n from books group by decade order by decade;

-- E8. Transfer: titles never borrowed, alphabetically. Use a method that still works if a loan has a NULL title.
create table e8 as
  select b.title from books as b where not exists (select 1 from loans as l where l.title = b.title) order by b.title;
