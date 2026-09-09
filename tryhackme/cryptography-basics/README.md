# Cryptography Basics

> Categoria: Cryptography
> Plataforma: TryHackMe
> Status: ✅ Estudado / evidenciado

## Objetivo
Entender terminologia criptográfica, cifras clássicas, criptografia simétrica e noções matemáticas básicas.

## Conceitos aprendidos
- confidencialidade, integridade e autenticidade
- cifra vs codificação vs hash
- Caesar cipher
- criptografia simétrica
- criptografia assimétrica em visão geral

## Ferramentas
OpenSSL, terminal e bibliotecas criptográficas em contexto de estudo.

## Comandos importantes
```bash
openssl rand -hex 16
openssl dgst -sha256 arquivo
```

## Metodologia
Identificar o objetivo de segurança → escolher o primitivo correto → entender chaves e fluxo → validar em laboratório.

## O que eu aprendi
Criptografia já foi estudada anteriormente, incluindo conceitos usados para entender comunicação segura. Não afirmar conclusão oficial da room.

## Lições importantes
Hash não é criptografia reversível; criptografia simétrica e assimétrica resolvem problemas diferentes.

## Referências
- https://tryhackme.com/room/cryptographybasics
- https://www.nist.gov/cryptography
