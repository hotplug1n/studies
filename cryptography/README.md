# 🔑 Cryptography

## Objetivo
Entender como criptografia, hashes, assinaturas e troca de chaves sustentam confidencialidade, integridade e autenticidade.

## Conceitos
- cifra vs hash
- simétrica vs assimétrica
- RSA e Diffie-Hellman
- chaves públicas/privadas
- certificados e TLS
- assinaturas digitais
- integridade e salt em armazenamento de senhas

## Comandos úteis
```bash
sha256sum arquivo
md5sum arquivo
openssl dgst -sha256 arquivo
openssl s_client -connect example.com:443
```

## Boas práticas
Não confundir hashing com criptografia reversível. Senhas devem ser armazenadas com funções de password hashing apropriadas e salt, não com SHA-256 puro.

## TryHackMe relacionado
- Cryptography Basics
- Public Key Cryptography Basics
- Hashing Basics
- John the Ripper: The Basics

## Status
**Estudado / em andamento.** Conceitos de RSA, Diffie-Hellman e hashes já fizeram parte dos estudos anteriores.