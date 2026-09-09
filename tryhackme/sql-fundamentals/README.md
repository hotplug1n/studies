# SQL Fundamentals

> Categoria: Web Security / SQL
> Plataforma: TryHackMe
> Status: 🔎 Conteúdo pesquisado

## Objetivo
Aprender fundamentos de bancos relacionais e SQL antes de estudar SQL injection.

## Conceitos
- database, table, row e column
- SELECT e filtros
- INSERT, UPDATE, DELETE
- CREATE/ALTER/DROP
- cláusulas e operadores
- funções e agregação

## Comandos importantes
```sql
SELECT * FROM users;
SELECT username FROM users WHERE id = 1;
INSERT INTO users (username) VALUES ('alice');
UPDATE users SET username = 'bob' WHERE id = 1;
DELETE FROM users WHERE id = 1;
```

## Conteúdo pesquisado
A página pública da room lista bancos, SQL, CRUD, cláusulas, operadores e funções como objetivos centrais.

## Lições importantes
SQL injection nasce de uma combinação de entrada controlável e construção insegura de consultas; consultas parametrizadas são uma defesa fundamental.

## Referências
- https://tryhackme.com/room/sqlfundamentals
- https://owasp.org/www-community/attacks/SQL_Injection
