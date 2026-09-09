# Public Key Cryptography Basics

> Categoria: Cryptography
> Status: ✅ Concluída — evidência visual no perfil

## Objetivo
Entender criptografia assimétrica e suas aplicações.

## Conceitos aprendidos
- pares público/privado
- RSA
- Diffie-Hellman
- SSH
- certificados e assinaturas
- PGP/GPG

## Ferramentas
`openssl`, `ssh`, `gpg` e terminal.

## Comandos importantes
```bash
openssl genpkey -algorithm RSA -out key.pem
ssh-keygen
 gpg --version
```

## Metodologia
Separar chave pública/privada → identificar uso → verificar autenticação/integridade → relacionar com PKI.

## O que aprendi
Entendi melhor por que assimetria é especialmente útil para autenticação e estabelecimento de confiança.

## Documentação de apoio
https://tryhackme.com/room/publickeycrypto · https://www.openssl.org/docs/

## Evidência
Room concluída no perfil apresentado.