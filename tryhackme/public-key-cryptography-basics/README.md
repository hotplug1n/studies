# Public Key Cryptography Basics

> Categoria: Cryptography
> Plataforma: TryHackMe
> Status: ✅ Estudado / evidenciado

## Objetivo
Entender criptografia assimétrica e suas aplicações em RSA, Diffie-Hellman, SSH, certificados e PGP/GPG.

## Conceitos aprendidos
- pares de chaves
- RSA
- troca de chaves Diffie-Hellman
- autenticação com SSH
- certificados e TLS
- assinatura digital
- PGP/GPG

## Comandos importantes
```bash
ssh-keygen -t ed25519
ssh-keygen -lf ~/.ssh/id_ed25519.pub
openssl s_client -connect example.com:443
```

## O que eu aprendi
RSA e Diffie-Hellman já foram estudados no processo anterior de aprendizagem de criptografia. A room não é marcada como oficialmente concluída.

## Lições importantes
Criptografia assimétrica não é apenas “criptografar com chave pública”; ela também sustenta autenticação, troca de chaves e assinaturas.

## Referências
- https://tryhackme.com/room/publickeycrypto
- https://www.openssl.org/docs/
