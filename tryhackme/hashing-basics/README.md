# Hashing Basics

> Categoria: Cryptography
> Plataforma: TryHackMe
> Status: ✅ Estudado / evidenciado

## Objetivo
Entender funções de hash, uso em integridade e autenticação, identificação de formatos e limites do armazenamento inseguro de senhas.

## Conceitos
- saída de tamanho fixo
- determinismo
- colisões
- salt
- password hashing
- integridade de arquivos

## Comandos importantes
```bash
sha256sum arquivo
md5sum arquivo
printf '%s' 'texto' | sha256sum
```

## O que eu aprendi
Hashing e SHA-256 já apareceram nos estudos anteriores, inclusive cálculo e interpretação de hashes. A conclusão oficial da room não é afirmada.

## Lições importantes
MD5/SHA-256 podem ser úteis para integridade, mas não são substitutos de um password hash moderno e adequado para senhas.

## Referências
- https://tryhackme.com/room/hashingbasics
- https://csrc.nist.gov/projects/hash-functions
