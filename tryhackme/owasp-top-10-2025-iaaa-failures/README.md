# OWASP Top 10 2025 — IAAA Failures

> Categoria: Web Security / OWASP
> Plataforma: TryHackMe
> Status: 🔎 Conteúdo pesquisado

## Objetivo
Estudar as categorias A01, A07 e A09 do OWASP Top 10:2025 pela lente de Identity, Authentication, Authorisation e Accountability.

## Conceitos
- **Identity:** qual conta/identidade está atuando.
- **Authentication:** como a identidade é comprovada.
- **Authorisation:** o que aquela identidade pode fazer.
- **Accountability:** como ações são registradas e alertadas.

## Pontos de segurança
- autorização deve ser validada no servidor em cada requisição relevante;
- autenticação precisa resistir a abuso de credenciais e sessões;
- logs devem permitir reconstruir o ciclo de autenticação e ações importantes;
- alertas precisam ser afinados para reduzir ruído.

## Conteúdo pesquisado
A room pública atual apresenta A01 Broken Access Control, A07 Authentication Failures e A09 Logging & Alerting Failures, com exercícios de apoio.

## Lições importantes
Confundir autenticação com autorização é um erro comum. Uma sessão válida não significa que o usuário possa acessar qualquer recurso.

## Referências
- https://tryhackme.com/room/owasptopten2025one
- https://owasp.org/Top10/
