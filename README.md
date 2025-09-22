# Old Dragon - Criador de Personagens com Flask

## Sobre o Projeto

Este projeto é uma aplicação web desenvolvida em Python com o microframework Flask, que serve como um gerador de fichas de personagem para o sistema de RPG "Old Dragon". A aplicação guia o usuário através de um processo simples e intuitivo para criar um personagem, desde a escolha do nome, raça e classe, até a definição de seus atributos de acordo com diferentes métodos de rolagem de dados.

-----

## Funcionalidades

  * **Criação de Personagem**: Formulário simples para definir nome, raça (Anão, Elfo, Humano, Halfling) e classe (Ladrão, Guerreiro, Clérigo).
  * **Três Métodos de Geração de Atributos**:
    1.  **Clássico**: Gera 6 valores aleatórios somando 3 dados de 6 lados (3d6) para cada atributo.
    2.  **Aventureiro**: Rola 6 conjuntos de 3d6 e permite que o jogador distribua os valores gerados entre os atributos.
    3.  **Heróico**: Rola 6 conjuntos de 4 dados de 6 lados, descarta o menor de cada conjunto e permite a distribuição dos valores restantes.
  * **Distribuição de Atributos Interativa**: Interface para atribuir os valores rolados aos 6 atributos (Força, Destreza, Constituição, Inteligência, Sabedoria, Carisma), com validação em JavaScript para impedir a atribuição de um mesmo valor a múltiplos atributos.
  * **Ficha de Personagem Final**: Apresenta uma ficha de personagem com o nome, descrição da raça, os atributos definidos e uma imagem que representa a classe escolhida.
  * **Backend com POO**: A lógica do backend é estruturada usando Programação Orientada a Objetos, com classes definidas para `Personagem`, `Raca` e `Classe`, tornando o código modular e escalável.

-----

## Interface da Aplicação

A interface foi projetada com uma temática escura, inspirada na fantasia medieval dos jogos de RPG.

| Criação do Personagem | Atribuição de Valores | Ficha de Personagem |
| :---: | :---: | :---: |
| ![Criação de Personagem](https://i.imgur.com/MqdAIB5.png) | ![Atribuição de valores](https://i.imgur.com/ka346jO.png) | ![Ficha de Personagem Final](https://i.imgur.com/XZlBxKK.png) |
| *Tela onde o usuário cria o personagem.* |*Tela onde o usuário distribui os valores gerados entre os seis atributos principais.* | *Tela final que exibe a ficha completa do personagem, com seus dados e uma arte representativa.* |

-----

## Tecnologias Utilizadas

  * **Backend**:
      * **Python 3.10**
      * **Flask**: Para o roteamento, gerenciamento de sessões e renderização de templates.
  * **Frontend**:
      * **HTML5**
      * **CSS3**: Para estilização e layout, utilizando Flexbox.
      * **JavaScript**: Para validação dinâmica no formulário de atribuição valores para os atributos.
  * **Estrutura de Projeto**:
      * **Programação Orientada a Objetos (POO)**: Para modelar as entidades do RPG (Personagens, Raças, Classes).

-----

## Estrutura do Projeto

O repositório está organizado da seguinte forma para garantir a separação de responsabilidades:

```
/
|-- app.py                  # Arquivo principal da aplicação Flask (rotas e lógica central)
|-- models/                 # Contém as classes que modelam os dados da aplicação
|   |-- personagem.py
|   |-- classe/
|   |   |-- classe.py       # Classe base abstrata
|   |   |-- guerreiro.py
|   |   |-- ...
|   |-- raca/
|   |   |-- raca.py         # Classe base abstrata
|   |   |-- anao.py
|   |   |-- ...
|-- static/                 # Arquivos estáticos (CSS, imagens)
|   |-- style.css
|   |-- images/
|-- templates/              # Arquivos de template HTML para o Flask
|   |-- index.html          # Página inicial de criação
|   |-- atribuir.html       # Página para distribuir atributos
|   |-- ficha.html          # Página final da ficha
|-- uteis/                  # Módulos de utilidades
|   |-- dado.py             # Lógica para rolar os dados
```

-----

## Como Executar o Projeto

Para executar este projeto localmente, siga os passos abaixo:

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/JhullyKF/Old-Dragon_Flask
    cd old-dragon_flask
    ```

2.  **Crie e ative um ambiente virtual (recomendado):**

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    O único requisito principal é o Flask.

    ```bash
    pip install Flask
    ```

4.  **Execute a aplicação:**

    ```bash
    python app.py
    ```

5.  **Acesse a aplicação:**
    Abra seu navegador e acesse `http://127.0.0.1:5000`.

-----
