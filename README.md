# Sistema de Login em Python

1. Este projeto apresenta um pequeno sistema de **login** em Python, utilizando comparações de strings, laços de repetição e validação de credenciais. O objetivo é praticar **condicionais**, **loops** e **entradas de usuário**.

---

## Objetivo

* Solicitar nome de usuário e senha
* Validar os dados digitados
* Repetir a solicitação enquanto houver erro
* Exibir mensagem de acesso concedido ao final

---

## Funcionamento do Código

### **1 – Definição das credenciais**

O programa começa declarando o usuário e a senha corretos:

```python
senha = "1234"
usuario = "Murilo"
```

* Tanto o usuário quanto a senha são tratados como **strings**, facilitando a comparação.

---

### **2 – Entrada inicial do usuário**

O programa solicita que o usuário digite suas credenciais:

```python
usuariod = input("Digite seu nome de usuário: ")
senhad = input("Digite a senha: ")
```

**Aprendizado:** Uso de `input()` para capturar dados do teclado.

---

### **3 – Validação com loop**

Enquanto o usuário **errar o nome ou a senha**, o programa continua pedindo novamente:

```python
while usuariod != usuario or senhad != senha:
    print("Acesso negado! Tente novamente...")
    usuariod = input("Digite seu nome de usuário: ")
    senhad = input("Digite a senha: ")
```

* O operador `or` é utilizado para verificar se **qualquer** informação está incorreta.
* O loop só termina quando os dados estão corretos.

---

### **4 – Login bem-sucedido**

Quando as credenciais estão certas:

```python
print(f"Acesso concedido! Seja bem-vindo, usuário {usuario}!")
```

* O programa exibe uma mensagem de sucesso usando **f-string**.

---

## Exemplo de Execução

```
Digite seu nome de usuário: João
Digite a senha: 1111
Acesso negado! Tente novamente...
Digite seu nome de usuário: Murilo
Digite a senha: 1234
Acesso concedido! Seja bem-vindo, usuário Murilo!
```
